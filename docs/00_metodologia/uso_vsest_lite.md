# Uso operativo de VSEST-Lite

VSEST-Lite convierte issues estructurados de GitHub en registros verificables,
matrices y un dashboard documental. Sus reglas se definen en
`vsest-lite.config.yml`; los documentos generados no deben editarse manualmente.

## Flujo de trabajo

1. Crear un issue con el formulario correspondiente: Artefacto, Riesgo, ZAP o
   Evaluacion.
2. Completar todos los campos obligatorios. Cada `Codigo` debe ser unico en el
   repositorio.
3. Incorporar el issue al GitHub Project y asignarle la columna que corresponda
   a su campo `Estado`.
4. Ejecutar **Validate VSEST-Lite Issues** desde la pestaña Actions.
5. Si falla, corregir los campos señalados en el log y volver a ejecutar Validate.
6. Ejecutar **Generate VSEST-Lite Reports**.
7. Revisar las matrices y el dashboard bajo `docs/`, incluida la coherencia entre
   los issues, sus evidencias y el estado visual del Project.

## Reglas principales

- Los prefijos, campos obligatorios, estados, fases y valores permitidos se
  mantienen en `vsest-lite.config.yml`.
- Todo issue estructurado requiere `Codigo`, y no puede repetir el de otro issue.
- Los estados y fases declarados deben pertenecer a las escalas configuradas.
- La prioridad de un riesgo debe ser `Baja`, `Media`, `Alta` o `Critica`.
- Un resultado de evaluacion debe comenzar por `0`, `1` o `2`.
- Un ZAP con estado `No ejecutable` debe explicar la causa en `Causa` u
  `Observacion`.
- Un artefacto `Cerrado` debe identificar evidencia verificable.

## Ejecucion local

Se requiere Python 3.11 o posterior.

```bash
python -m pip install -r requirements.txt
python scripts/validate_issues.py
python scripts/generate_reports.py
```

Por defecto, los scripts consultan el repositorio configurado. Las variables
`GITHUB_REPOSITORY`, `GITHUB_TOKEN` y `VSEST_CONFIG` permiten cambiar el
repositorio, el token y la ruta de configuracion.

## Salidas generadas

- `docs/02_trazabilidad/matriz_ejecucion.md`
- `docs/03_riesgos/README.md`
- `docs/05_seguridad/README.md`
- `docs/06_evaluacion/instrumento_producto.md`
- `docs/08_tablero/tablero_vsest_lite.md`
- `docs/10_dashboard/resumen_estado.md`

El Project Kanban sigue siendo un control visual manual. Su columna debe coincidir
con el campo `Estado` del issue; automatizar esa sincronizacion queda fuera de la
version 0.1.
