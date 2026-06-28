import json
import os
import re
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
REPO = os.environ.get('GITHUB_REPOSITORY', 'somefirenoodles/VSEST-Lite')
TOKEN = os.environ.get('GITHUB_TOKEN')
VALID_PREFIXES = ('[artefacto]', '[riesgo]', '[zap]', '[evaluacion]')
VALID_LABELS = {'artefacto', 'riesgo', 'zap', 'evaluacion'}


def api(path):
    url = f'https://api.github.com/repos/{REPO}{path}'
    headers = {'Accept': 'application/vnd.github+json'}
    if TOKEN:
        headers['Authorization'] = f'Bearer {TOKEN}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode('utf-8'))


def list_issues():
    return api('/issues?state=open&per_page=100')


def labels(issue):
    return [label.get('name', '').lower() for label in issue.get('labels', [])]


def field(body, name):
    if not body:
        return ''
    pattern = rf'### {re.escape(name)}\s*\n\s*(.+?)(?=\n### |\Z)'
    match = re.search(pattern, body, re.S | re.I)
    if match:
        return match.group(1).strip().replace('\n', ' ')
    return ''


def is_structured_issue(title, ls):
    t = (title or '').lower()
    return t.startswith(VALID_PREFIXES) or bool(VALID_LABELS.intersection(set(ls)))


def issue_type(title, ls):
    t = (title or '').lower()
    if 'riesgo' in ls or t.startswith('[riesgo]'):
        return 'riesgo'
    if 'zap' in ls or t.startswith('[zap]'):
        return 'zap'
    if 'evaluacion' in ls or t.startswith('[evaluacion]'):
        return 'evaluacion'
    return 'artefacto'


def write(path, content):
    full = BASE / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding='utf-8')


def generate(issues):
    trazas = ['# Matriz de ejecucion y trazabilidad\n', '| ID | Requisito / tarea | Modulo | Fase | Artefacto | Evidencia | Estado | Resultado | Observacion |', '|---|---|---|---|---|---|---|---|---|']
    riesgos = ['# Matriz de riesgos\n', '| ID | Riesgo | Probabilidad | Impacto | Prioridad | Mitigacion | Estado |', '|---|---|---|---|---|---|---|']
    tablero = ['# Tablero VSEST-Lite\n', '| Tarea | Fase | Estado | Responsable | Evidencia | Proxima accion |', '|---|---|---|---|---|---|']
    zap = ['# Reporte OWASP ZAP\n', '| ID | Hallazgo | Severidad | Confianza | Modulo | Evidencia | Prioridad | Estado | Accion correctiva |', '|---|---|---|---|---|---|---|---|---|']
    evaluacion = ['# Instrumento de evaluacion del producto\n', '| ID | Caracteristica | Criterio | Evidencia | Resultado | Observacion |', '|---|---|---|---|---|---|']

    for issue in issues:
        if 'pull_request' in issue:
            continue
        ls = labels(issue)
        body = issue.get('body') or ''
        title = issue.get('title') or ''
        if not is_structured_issue(title, ls):
            continue
        state = issue.get('state') or ''
        codigo = field(body, 'Codigo') or f'ISSUE-{issue.get("number")}'
        fase = field(body, 'Fase') or 'Pendiente'
        estado = field(body, 'Estado') or state
        evidencia = field(body, 'Evidencia') or 'Pendiente'
        modulo = field(body, 'Modulo') or 'General'
        obs = field(body, 'Observacion') or ''
        responsable = ', '.join(a.get('login', '') for a in issue.get('assignees', [])) or 'Por asignar'
        tipo = issue_type(title, ls)

        if tipo == 'riesgo':
            riesgos.append(f'| {codigo} | {title} | {field(body, "Probabilidad") or "Pendiente"} | {field(body, "Impacto") or "Pendiente"} | {field(body, "Prioridad") or "Pendiente"} | {field(body, "Mitigacion") or "Pendiente"} | {estado} |')
        elif tipo == 'zap':
            zap.append(f'| {codigo} | {title} | {field(body, "Severidad") or "Pendiente"} | {field(body, "Confianza") or "Pendiente"} | {modulo} | {evidencia} | {field(body, "Prioridad") or "Pendiente"} | {estado} | {field(body, "Accion correctiva") or "Pendiente"} |')
        elif tipo == 'evaluacion':
            evaluacion.append(f'| {codigo} | {field(body, "Caracteristica") or "Pendiente"} | {field(body, "Criterio") or title} | {evidencia} | {field(body, "Resultado") or "0"} | {obs} |')
        else:
            trazas.append(f'| {codigo} | {title} | {modulo} | {fase} | {field(body, "Artefacto") or "Issue"} | {evidencia} | {estado} | {field(body, "Resultado") or "Pendiente"} | {obs} |')
            tablero.append(f'| {title} | {fase} | {estado} | {responsable} | {evidencia} | {field(body, "Proxima accion") or "Pendiente"} |')

    write('docs/02_trazabilidad/matriz_ejecucion.md', '\n'.join(trazas) + '\n')
    write('docs/03_riesgos/README.md', '\n'.join(riesgos) + '\n')
    write('docs/05_seguridad/README.md', '\n'.join(zap) + '\n')
    write('docs/06_evaluacion/instrumento_producto.md', '\n'.join(evaluacion) + '\n')
    write('docs/08_tablero/tablero_vsest_lite.md', '\n'.join(tablero) + '\n')


if __name__ == '__main__':
    generate(list_issues())
    print('Reportes generados desde issues')
