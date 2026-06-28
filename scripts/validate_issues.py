import json
import os
import sys
import urllib.request

REPO = os.environ.get('GITHUB_REPOSITORY', 'somefirenoodles/VSEST-Lite')
TOKEN = os.environ.get('GITHUB_TOKEN')
VALID_STATES = {'Pendiente', 'En elaboracion', 'En revision', 'Con observaciones', 'Aprobado', 'Cerrado', 'open', 'closed'}
VALID_PHASES = {'Identificacion', 'Planificacion', 'Elaboracion', 'Revision', 'Correccion', 'Validacion', 'Cierre', 'Pendiente'}


def api(path):
    url = f'https://api.github.com/repos/{REPO}{path}'
    headers = {'Accept': 'application/vnd.github+json'}
    if TOKEN:
        headers['Authorization'] = f'Bearer {TOKEN}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode('utf-8'))


def main():
    errors = []
    issues = api('/issues?state=all&per_page=100')
    for issue in issues:
        if 'pull_request' in issue:
            continue
        body = issue.get('body') or ''
        title = issue.get('title') or ''
        if '[' not in title or ']' not in title:
            errors.append(f'Issue #{issue.get("number")}: titulo sin prefijo')
        if 'Codigo' not in body and 'codigo' not in body.lower():
            errors.append(f'Issue #{issue.get("number")}: sin codigo en cuerpo')
        if 'Cerrado' in body and 'Evidencia' not in body:
            errors.append(f'Issue #{issue.get("number")}: cerrado sin evidencia')

    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print('Validacion documental completada')


if __name__ == '__main__':
    main()
