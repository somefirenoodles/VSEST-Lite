# Estados de artefactos

## Escala de estados

| Estado | Criterio de uso | Evidencia mínima |
|---|---|---|
| Pendiente | Artefacto identificado, no iniciado. | Registro en matriz o issue. |
| En elaboración | Artefacto en construcción. | Archivo creado o issue activo. |
| En revisión | Artefacto completo, pendiente de validación. | Checklist de revisión. |
| Con observaciones | Artefacto revisado con ajustes requeridos. | Observación registrada. |
| Aprobado | Artefacto cumple criterios mínimos. | Evidencia vinculada. |
| Cerrado | Artefacto aprobado y asociado al cierre de fase. | Commit, acta o resultado final. |

## Regla de consistencia

Un artefacto no puede pasar a `Aprobado` si no tiene evidencia mínima. Un artefacto no puede pasar a `Cerrado` si no aparece vinculado en la matriz de trazabilidad o en el registro de ejecución.
