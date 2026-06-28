# Automatizacion VSEST-Lite

Esta carpeta contiene los archivos necesarios para activar el flujo automatizado.

## Archivos creados

| Ruta | Uso |
|---|---|
| `scripts/generate_reports.py` | Genera matrices desde issues. |
| `scripts/validate_issues.py` | Valida consistencia minima de issues. |
| `automation/workflows/generate_reports.yml` | Plantilla de workflow para generar reportes. |
| `automation/workflows/validate_issues.yml` | Plantilla de workflow para validar issues. |
| `automation/issue_templates/artefacto.yml` | Base de plantilla para artefactos. |

## Activacion manual requerida

Mover los workflows a:

```text
.github/workflows/generate_reports.yml
.github/workflows/validate_issues.yml
```

Mover los formularios de issues a:

```text
.github/ISSUE_TEMPLATE/
```

## Flujo esperado

1. Crear issues como formularios de captura.
2. Usar GitHub Projects como tablero Kanban.
3. Ejecutar Actions.
4. Generar matrices en `docs/`.
