# Instrumento de evaluacion del producto

| ID | Caracteristica | Criterio | Evidencia | Resultado | Observacion |
|---|---|---|---|---|---|
| EV-005 | Mantenibilidad | El repositorio separa metodologia, trazabilidad, riesgos, SQA, seguridad, evaluacion y cierre en artefactos localizables. | README.md | 2 - Cumple | La estructura documental permite localizar y actualizar artefactos por modulo del proceso. |
| EV-004 | Seguridad | El proceso documenta el protocolo de auditoria OWASP ZAP y registra la limitacion de no ejecucion por ausencia de host funcional. | docs/05_seguridad/README.md | 1 - Cumple parcialmente | La auditoria esta preparada documentalmente, pero no puede ejecutarse como prueba dinamica real porque PSIREG no esta implementado. |
| EV-003 | Gestion de riesgos | El proceso registra riesgos con probabilidad, impacto, prioridad, mitigacion y estado. | docs/03_riesgos/README.md | 2 - Cumple | La matriz de riesgos se alimenta desde issues estructurados de tipo riesgo. |
| EV-002 | Trazabilidad | El proceso vincula issues estructurados, artefactos, evidencias y matrices generadas automaticamente. | docs/02_trazabilidad/matriz_ejecucion.md | 2 - Cumple | La matriz se genera desde issues y permite seguir el estado documental de los artefactos. |
| EV-001 | Seguridad | El proceso documenta controles esperados de autenticacion, autorizacion y auditoria de seguridad. | docs/05_seguridad/README.md | 1 - Cumple parcialmente | Se documenta el criterio, pero no se puede validar sobre sistema funcional porque PSIREG no esta implementado. |
