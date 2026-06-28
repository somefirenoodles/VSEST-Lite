import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path

import yaml


BASE = Path(__file__).resolve().parents[1]
EMPTY_VALUES = {"", "_no response_", "no response", "_sin respuesta_"}


def load_config(path=None):
    config_path = Path(
        path or os.environ.get("VSEST_CONFIG", BASE / "vsest-lite.config.yml")
    )
    if not config_path.is_absolute():
        config_path = BASE / config_path

    with config_path.open(encoding="utf-8") as stream:
        config = yaml.safe_load(stream)

    required_sections = {"project", "github", "issue_types", "states", "phases", "rules", "reports"}
    missing = required_sections.difference(config or {})
    if missing:
        raise ValueError(
            "Configuracion incompleta; faltan secciones: " + ", ".join(sorted(missing))
        )
    return config


def repository(config):
    return os.environ.get("GITHUB_REPOSITORY") or config["github"]["repository"]


def api(path, config):
    url = f"https://api.github.com/repos/{repository(config)}{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "VSEST-Lite",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def list_issues(config):
    state = config["github"].get("issue_state", "all")
    issues = []
    page = 1
    while True:
        params = urllib.parse.urlencode(
            {"state": state, "per_page": 100, "page": page}
        )
        batch = api(f"/issues?{params}", config)
        issues.extend(issue for issue in batch if "pull_request" not in issue)
        if len(batch) < 100:
            return issues
        page += 1


def field(body, name):
    if not body:
        return ""
    pattern = rf"^###\s+{re.escape(name)}\s*\r?\n(.*?)(?=^###\s+|\Z)"
    match = re.search(pattern, body, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def is_empty(value):
    return (value or "").strip().casefold() in EMPTY_VALUES


def issue_type(issue, config):
    title = (issue.get("title") or "").strip()
    for type_name, type_config in config["issue_types"].items():
        prefix = type_config["prefix"]
        if title.casefold().startswith(prefix.casefold()):
            return type_name
    return None


def issue_state(issue, config):
    value = field(issue.get("body") or "", "Estado")
    if value:
        return value
    return "Cerrado" if issue.get("state") == "closed" else "Pendiente"


def markdown(value, fallback="Pendiente"):
    text = str(value or fallback).replace("\r", " ").replace("\n", " ")
    return re.sub(r"\s+", " ", text).strip().replace("|", r"\|")
