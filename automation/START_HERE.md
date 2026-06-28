# Inicio de trabajo VSEST-Lite

## Estado actual

El repositorio ya contiene la estructura documental y los scripts base para generar reportes desde issues.

## Para activar Actions

Copiar estos archivos:

- `automation/workflows/generate_reports.yml` hacia `.github/workflows/generate_reports.yml`
- `automation/workflows/validate_issues.yml` hacia `.github/workflows/validate_issues.yml`

## Para activar formularios de issues

Copiar las plantillas desde:

- `automation/issue_templates/`

hacia:

- `.github/ISSUE_TEMPLATE/`

## Flujo de trabajo

1. Crear issue.
2. Completar campos del artefacto.
3. Mover issue en GitHub Project.
4. Ejecutar workflow de validacion.
5. Ejecutar workflow de reportes.
6. Revisar matrices generadas en `docs/`.
