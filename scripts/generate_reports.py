import sys
from collections import Counter, defaultdict
from pathlib import Path

from vsest_common import (
    BASE,
    field,
    issue_state,
    issue_type,
    list_issues,
    load_config,
    markdown,
)


def write(path, lines):
    destination = BASE / Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def assignees(issue):
    names = [assignee.get("login", "") for assignee in issue.get("assignees", [])]
    return ", ".join(filter(None, names)) or "Por asignar"


def generate(issues, config):
    reports = config["reports"]
    rows = defaultdict(list)
    counts = {
        type_name: Counter()
        for type_name in config["issue_types"]
    }

    for issue in issues:
        type_name = issue_type(issue, config)
        if not type_name:
            continue

        body = issue.get("body") or ""
        title = issue.get("title") or ""
        code = field(body, "Codigo") or f'ISSUE-{issue.get("number")}'
        state = issue_state(issue, config)
        phase = field(body, "Fase") or "Pendiente"
        evidence = field(body, "Evidencia") or "Pendiente"
        module = field(body, "Modulo") or "General"
        observation = field(body, "Observacion")
        counts[type_name][state] += 1

        if type_name == "riesgo":
            rows["risks"].append(
                f'| {markdown(code)} | {markdown(field(body, "Riesgo"), title)} | '
                f'{markdown(field(body, "Probabilidad"))} | {markdown(field(body, "Impacto"))} | '
                f'{markdown(field(body, "Prioridad"))} | {markdown(field(body, "Mitigacion"))} | '
                f'{markdown(state)} |'
            )
        elif type_name == "zap":
            rows["security"].append(
                f'| {markdown(code)} | {markdown(title)} | {markdown(field(body, "Severidad"))} | '
                f'{markdown(field(body, "Confianza"))} | {markdown(module)} | {markdown(evidence)} | '
                f'{markdown(field(body, "Prioridad"))} | {markdown(state)} | '
                f'{markdown(field(body, "Accion correctiva"))} |'
            )
        elif type_name == "evaluacion":
            rows["evaluation"].append(
                f'| {markdown(code)} | {markdown(field(body, "Caracteristica"))} | '
                f'{markdown(field(body, "Criterio"), title)} | {markdown(evidence)} | '
                f'{markdown(field(body, "Resultado"), "0")} | {markdown(observation, "")} |'
            )
        else:
            rows["traceability"].append(
                f'| {markdown(code)} | {markdown(title)} | {markdown(module)} | {markdown(phase)} | '
                f'{markdown(field(body, "Artefacto"), "Issue")} | {markdown(evidence)} | '
                f'{markdown(state)} | {markdown(field(body, "Resultado"))} | '
                f'{markdown(observation, "")} |'
            )
            rows["board"].append(
                f'| {markdown(title)} | {markdown(phase)} | {markdown(state)} | '
                f'{markdown(assignees(issue))} | {markdown(evidence)} | '
                f'{markdown(field(body, "Proxima accion"))} |'
            )

    write(
        reports["traceability"],
        [
            "# Matriz de ejecucion y trazabilidad",
            "",
            "| ID | Requisito / tarea | Modulo | Fase | Artefacto | Evidencia | Estado | Resultado | Observacion |",
            "|---|---|---|---|---|---|---|---|---|",
            *rows["traceability"],
        ],
    )
    write(
        reports["risks"],
        [
            "# Matriz de riesgos",
            "",
            "| ID | Riesgo | Probabilidad | Impacto | Prioridad | Mitigacion | Estado |",
            "|---|---|---|---|---|---|---|",
            *rows["risks"],
        ],
    )
    write(
        reports["security"],
        [
            "# Reporte OWASP ZAP",
            "",
            "| ID | Hallazgo | Severidad | Confianza | Modulo | Evidencia | Prioridad | Estado | Accion correctiva |",
            "|---|---|---|---|---|---|---|---|---|",
            *rows["security"],
        ],
    )
    write(
        reports["evaluation"],
        [
            "# Instrumento de evaluacion del producto",
            "",
            "| ID | Caracteristica | Criterio | Evidencia | Resultado | Observacion |",
            "|---|---|---|---|---|---|",
            *rows["evaluation"],
        ],
    )
    write(
        reports["board"],
        [
            "# Tablero VSEST-Lite",
            "",
            "| Tarea | Fase | Estado | Responsable | Evidencia | Proxima accion |",
            "|---|---|---|---|---|---|",
            *rows["board"],
        ],
    )

    states = config["states"]
    header = "| Tipo | Total | " + " | ".join(states) + " |"
    separator = "|---|---:|" + "|".join("---:" for _ in states) + "|"
    dashboard_rows = []
    for type_name, type_config in config["issue_types"].items():
        type_counts = counts[type_name]
        total = sum(type_counts.values())
        values = " | ".join(str(type_counts[state]) for state in states)
        dashboard_rows.append(
            f'| {type_config["display_name"]} | {total} | {values} |'
        )
    write(
        reports["dashboard"],
        [
            "# Dashboard VSEST-Lite",
            "",
            "> Generado automaticamente desde los issues estructurados. No editar manualmente.",
            "",
            header,
            separator,
            *dashboard_rows,
        ],
    )


def main():
    try:
        config = load_config()
        issues = list_issues(config)
        generate(issues, config)
    except Exception as exc:
        print(f"Error de ejecucion: {exc}", file=sys.stderr)
        return 2
    print("Reportes generados desde issues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
