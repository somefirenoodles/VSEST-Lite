# Matriz de riesgos

| ID | Riesgo | Probabilidad | Impacto | Prioridad | Mitigación | Estado |
|---|---|---|---|---|---|---|
| R-001 | PSIREG no dispone de una versión funcional evaluable. | Alta | Alto | Critica | Mantener pruebas como pendientes o No ejecutable y no declarar cumplimiento del producto. | En revision |
| R-002 | Un cambio de actores, RF o RNF puede romper la continuidad con casos de uso, pruebas y evaluación. | Media | Alto | Alta | Usar la matriz maestra y revisar relaciones antes de aprobar. | Pendiente |
| R-003 | Los reportes pueden quedar desactualizados después de modificar issues. | Media | Medio | Media | Validar issues y regenerar matriz, tablero y dashboard. | Pendiente |
| R-004 | Los controles dinámicos de seguridad no pueden demostrarse sin host y configuración. | Alta | Alto | Critica | Mantener ZAP como No ejecutable hasta disponer del entorno. | Pendiente |
| R-005 | Una dependencia externa puede incumplir licencia o privacidad institucional. | Media | Alto | Alta | Revisar inventario, licencia y tratamiento de datos antes de incorporarla. | Pendiente |
| R-006 | Un artefacto puede cerrarse sin evidencia verificable o con observaciones abiertas. | Alta | Medio | Alta | Bloquear el cierre hasta cumplir el criterio de salida. | Pendiente |
