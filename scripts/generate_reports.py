import sys
from collections import Counter, defaultdict
from pathlib import Path

from vsest_common import BASE, field, issue_state, issue_type, list_issues, load_config, markdown


def write(path, lines):
    destination = BASE / Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def assignees(issue):
    names = [a.get("login", "") for a in issue.get("assignees", [])]
    return ", ".join(filter(None, names)) or "Por asignar"


def generate(issues, config):
    reports = config["reports"]
    rows = defaultdict(list)
    counts = {name: Counter() for name in config["issue_types"]}
    for issue in issues:
        kind = issue_type(issue, config)
        if not kind:
            continue
        body = issue.get("body") or ""
        title = issue.get("title") or ""
        code = field(body, "Codigo") or f"ISSUE-{issue.get('number')}"
        state = issue_state(issue, config)
        evidence = field(body, "Evidencia") or "Pendiente"
        counts[kind][state] += 1
        if kind == "riesgo":
            rows["risks"].append(f"| {markdown(code)} | {markdown(field(body, 'Riesgo'), title)} | {markdown(field(body, 'Probabilidad'))} | {markdown(field(body, 'Impacto'))} | {markdown(field(body, 'Prioridad'))} | {markdown(field(body, 'Mitigacion'))} | {markdown(state)} |")
        elif kind == "zap":
            rows["security"].append(f"| {markdown(code)} | {markdown(title)} | {markdown(field(body, 'Severidad'))} | {markdown(field(body, 'Confianza'))} | {markdown(field(body, 'Modulo'))} | {markdown(evidence)} | {markdown(field(body, 'Prioridad'))} | {markdown(state)} | {markdown(field(body, 'Accion correctiva'))} |")
        elif kind == "evaluacion":
            rows["evaluation"].append(f"| {markdown(code)} | {markdown(field(body, 'Caracteristica'))} | {markdown(field(body, 'Requisito'))} | {markdown(field(body, 'Criterio'), title)} | {markdown(field(body, 'Caso de prueba'))} | {markdown(field(body, 'Metodo'))} | {markdown(evidence)} | {markdown(field(body, 'Resultado'), 'No evaluado')} | {markdown(field(body, 'Observacion'), '')} |")
        else:
            phase = field(body, "Fase") or "Pendiente"
            module = field(body, "Modulo") or "General"
            rows["traceability"].append(f"| {markdown(code)} | {markdown(title)} | {markdown(module)} | {markdown(phase)} | {markdown(field(body, 'Artefacto'), 'Issue')} | {markdown(evidence)} | {markdown(state)} | {markdown(field(body, 'Resultado'))} | {markdown(field(body, 'Observacion'), '')} |")
            rows["board"].append(f"| {markdown(code)} | {markdown(title)} | {markdown(phase)} | {markdown(state)} | {markdown(assignees(issue))} | {markdown(evidence)} | {markdown(field(body, 'Proxima accion'))} |")

    write(reports["traceability"], ["# Matriz de ejecucion y trazabilidad", "", "| ID | Artefacto | Modulo | Fase | Ruta | Evidencia | Estado | Resultado | Observacion |", "|---|---|---|---|---|---|---|---|---|", *rows["traceability"]])
    write(reports["risks"], ["# Matriz de riesgos", "", "| ID | Riesgo | Probabilidad | Impacto | Prioridad | Mitigacion | Estado |", "|---|---|---|---|---|---|---|", *rows["risks"]])
    write(reports["security"], ["# Reporte OWASP ZAP", "", "| ID | Hallazgo | Severidad | Confianza | Modulo | Evidencia | Prioridad | Estado | Accion correctiva |", "|---|---|---|---|---|---|---|---|---|", *rows["security"]])
    write(reports["evaluation"], ["# Instrumento de evaluacion del producto", "", "| ID | Caracteristica | RF/RNF | Criterio | Caso de prueba | Metodo | Evidencia | Resultado | Observacion |", "|---|---|---|---|---|---|---|---|---|", *rows["evaluation"]])
    write(reports["board"], ["# Tablero VSEST-Lite", "", "| Codigo | Tarea | Fase | Estado | Responsable | Evidencia | Proxima accion |", "|---|---|---|---|---|---|---|", *rows["board"]])

    states = config["states"]
    dashboard = ["# Dashboard VSEST-Lite", "", "> Generado desde los issues estructurados. VSEST-Lite demuestra control documental y del proceso, no funcionamiento de PSIREG.", "", "| Tipo | Total | " + " | ".join(states) + " |", "|---|---:|" + "|".join("---:" for _ in states) + "|"]
    for kind, meta in config["issue_types"].items():
        values = " | ".join(str(counts[kind][state]) for state in states)
        dashboard.append(f"| {meta['display_name']} | {sum(counts[kind].values())} | {values} |")
    write(reports["dashboard"], dashboard)


def main():
    try:
        config = load_config()
        generate(list_issues(config), config)
    except Exception as exc:
        print(f"Error de ejecucion: {exc}", file=sys.stderr)
        return 2
    print("Reportes generados desde issues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
