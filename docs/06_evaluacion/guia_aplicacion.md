# Guía de aplicación del instrumento de evaluación

El instrumento mide la calidad del producto PSIREG. La calidad documental de VSEST-Lite se controla mediante artefactos, riesgos y tablero; no se suma al resultado del producto.

## Escala de resultados

| Resultado | Regla de decisión |
|---|---|
| Cumple | La verificación fue ejecutada, es reproducible, satisface el criterio y no mantiene observaciones críticas. |
| Cumple parcialmente | La verificación fue ejecutada y satisface parte del criterio, pero la cobertura es incompleta o mantiene observaciones no críticas. |
| No cumple | La verificación fue ejecutada y el resultado contradice el criterio, o la capacidad requerida no está implementada. |
| No evaluado | El criterio todavía no fue aplicado, aunque existe una vía razonable para ejecutarlo posteriormente. No equivale a falla. |
| No ejecutable | La verificación no puede realizarse en el estado actual por ausencia de host, interfaz, código, endpoint, datos, permisos o configuración. Debe registrarse la causa y la próxima acción. |

## Campos obligatorios por criterio

Cada issue de Evaluación debe conservar: Código, Característica, Criterio, Requisito, Caso de prueba, Método, Resultado, Evidencia, Estado y Observación. Los valores válidos de Resultado son exclusivamente los cinco definidos en esta guía.

## Procedimiento

1. Confirmar el RF o RNF y el caso de prueba asociado en la matriz maestra.
2. Preparar el entorno, los datos y los permisos.
3. Ejecutar el método definido.
4. Conservar evidencia reproducible.
5. Seleccionar el resultado conforme a la regla de decisión.
6. Registrar observación, limitación y próxima acción cuando corresponda.
7. Regenerar el instrumento y el dashboard mediante GitHub Actions.

## Interpretación inicial

Mientras PSIREG no disponga de una versión funcional evaluable, los criterios permanecen en **No evaluado** o **No ejecutable** según la causa. No se calcula una calificación global a partir de criterios sin ejecución y no se infiere que el producto cumple o falla.
