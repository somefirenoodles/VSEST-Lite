# Uso operativo de VSEST-Lite

VSEST-Lite convierte issues estructurados en matrices, registros y un dashboard documental. Las salidas demuestran control del proceso; no demuestran funcionamiento de PSIREG.

## Flujo

1. Crear o actualizar el issue estructurado correspondiente.
2. Completar los campos obligatorios y utilizar un código único.
3. Asignar manualmente la tarjeta del GitHub Project a la columna que coincida con el campo Estado.
4. Ejecutar Validate VSEST-Lite Issues.
5. Corregir cualquier campo inválido.
6. Ejecutar Generate VSEST-Lite Reports.
7. Comprobar matriz, riesgos, instrumento, tablero y dashboard.

## Resultados del instrumento

- Cumple.
- Cumple parcialmente.
- No cumple.
- No evaluado.
- No ejecutable; requiere causa en Observacion.

## Reglas

- Las fases y estados deben pertenecer a `vsest-lite.config.yml`.
- Un artefacto Cerrado requiere evidencia verificable.
- Un ZAP No ejecutable requiere causa.
- La calidad documental no modifica el resultado del producto.
- El GitHub Project se actualiza manualmente; la versión actual no sincroniza sus columnas desde los issues.
