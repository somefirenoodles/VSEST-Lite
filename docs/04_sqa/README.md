# Plan de Garantía de Calidad

El Plan SQA conserva objetivos, responsables por rol, métricas con meta, pruebas, revisiones y auditorías. No declara ejecución de PSIREG.

## Métricas

| ID | Medida | Cálculo | Meta o criterio de aceptación | Evidencia | Rol responsable |
|---|---|---|---|---|---|
| MC-01 | Cobertura RF | RF con CU, CP y EV / 19 × 100 | 100 %: 19 de 19 RF relacionados antes de aprobar la línea base | Matriz maestra | Responsable de requisitos |
| MC-02 | Cobertura RNF | RNF con CU, CP y EV / 22 × 100 | 100 %: 22 de 22 RNF relacionados antes de aprobar la línea base | Matriz maestra | Responsable de requisitos |
| MC-03 | Trazabilidad | Relaciones completas / relaciones requeridas × 100 | 100 % antes de pasar un artefacto a Aprobado | Matriz y checklist | Revisor de calidad |
| MC-04 | Disponibilidad | Tiempo disponible / tiempo observado × 100 | Operación 24/7; mantenimiento anunciado con 48 horas, conforme a RNF-09 | Monitoreo | Responsable técnico |
| MC-05 | Respuesta | Tiempo observado por operación | Entre 1 y 10 segundos, conforme a RNF-13 | Registro de tiempos | Responsable de pruebas |
| MC-06 | Recursos | Máximo observado de CPU y RAM | CPU ≤ 60 % y RAM ≤ 50 %, conforme a RNF-14 | Monitoreo | Responsable técnico |
| MC-07 | Accesibilidad | Criterios WCAG AA conformes / aplicables × 100 | 100 % de criterios AA aplicables sin observaciones críticas | Reporte WCAG | Revisor de calidad |
| MC-08 | Precisión OCR | Campos coincidentes / campos comparados × 100 | 100 % de coincidencia en la muestra definida o desviación documentada | Fuente y resultado OCR | Responsable de pruebas |
| MC-09 | Observaciones | Observaciones abiertas por artefacto | 0 observaciones críticas para Aprobado o Cerrado | Issues | Responsable del artefacto |
| MC-10 | Evidencia de cierre | Artefactos cerrados con evidencia / artefactos cerrados × 100 | 100 % | Dashboard | Coordinador del proceso |

## Casos de prueba funcionales

Los casos CP-F01 a CP-F19 se mantienen vinculados uno a uno con RF-01 a RF-19 y CU-01 a CU-19. Todos permanecen pendientes hasta disponer de una versión evaluable. El resultado esperado corresponde a la descripción del RF de la línea base.

## Verificaciones no funcionales

Las verificaciones CP-NF01 a CP-NF22 se mantienen vinculadas uno a uno con RNF-01 a RNF-22 y con EV-007 a EV-020 según la matriz maestra. Las metas se conservan sin sustituirlas por resultados no ejecutados.

## Detalle de los casos prioritarios

| Caso | Precondición | Datos o preparación | Pasos mínimos | Criterio de aceptación | Evidencia | Rol |
|---|---|---|---|---|---|---|
| CP-F02 / CU-02 | Cuenta habilitada y perfil registrado | Credenciales válidas e inválidas | Iniciar sesión con ambos conjuntos; verificar redirección y rechazo | Acceso solo con credenciales válidas y funciones limitadas al perfil | Capturas, respuesta y registro de sesión | Responsable de pruebas |
| CP-F03 / CU-03 | Usuario autenticado; horarios configurados | Psicólogo, fecha, hora y motivo | Consultar disponibilidad; seleccionar horario; guardar; repetir con horario ocupado | La primera cita se registra y la segunda selección ocupada se rechaza | Capturas, registro de cita y calendario | Responsable de pruebas |
| CP-F07 / CU-07 | Actor autorizado; persona identificada | Datos completos y registro duplicado | Crear expediente; repetir con la misma persona | Se crea un único expediente y se impide el duplicado | Capturas y consulta del expediente | Responsable de pruebas |
| CP-F12 / CU-12 | Expediente seleccionado; dispositivo o archivo disponible | Documento legible e ilegible | Capturar/cargar; ejecutar OCR; revisar; guardar; repetir con error | Documento legible asociado; error o ilegibilidad sin modificación incorrecta | Imagen fuente, resultado OCR y asociación | Responsable de pruebas |
| CP-F18 / CU-18 | Actor autorizado; datos disponibles | Tipo de reporte y filtros | Generar consulta; validar datos; exportar | Reporte coherente con filtros y archivo exportado cuando corresponda | Captura, archivo y comparación de datos | Responsable de pruebas |
| CP-F19 / CU-19 | Actor con privilegios de administración | Cuenta nueva, duplicada y perfil permitido | Crear/asignar perfil; intentar duplicado y perfil no autorizado | Cuenta única, permisos correctos y rechazo de operaciones no autorizadas | Capturas, registro de cuenta e historial | Responsable de pruebas |

## Revisiones, auditorías y acciones correctivas

| Actividad | Momento | Alcance | Responsable | Criterio de salida |
|---|---|---|---|---|
| Revisión de línea base | Antes de aprobar diseño o pruebas | Actores, 19 RF, 22 RNF, 19 CU y fuentes | Responsable de requisitos y revisor de calidad | Sin diferencias ni elementos sin fuente |
| Revisión de artefacto | Al pasar a En revision | Contenido, formato, trazabilidad y estado | Responsable del artefacto y revisor de calidad | Aprobado o Con observaciones con hallazgos registrados |
| Revisión de evidencia | Antes de Aprobado o Cerrado | Reproducibilidad, entorno, resultado y relación con CP/EV | Responsable de pruebas y revisor de calidad | Evidencia suficiente o causa documentada de No ejecutable |
| Auditoría documental | Antes de consolidar la entrega | Numeración, Arial 12, doble espacio, tablas, figuras, APA 7 y consistencia | Coordinador del proceso y revisor de calidad | Sin observaciones críticas abiertas |
| Auditoría de seguridad | Cuando exista host funcional | Autenticación, autorización, sesión, comunicaciones y hallazgos ZAP | Responsable técnico y revisor de calidad | Reporte reproducible; mientras no exista host, estado No ejecutable |
| Auditoría de trazabilidad VSEST-Lite | Después de modificar issues y antes del cierre | Coincidencia entre issues, matriz, tablero, instrumento y dashboard | Coordinador del proceso | Reportes regenerados y sin diferencias |

Una desviación genera una observación en el issue del artefacto. El responsable registra la corrección y la evidencia; el revisor confirma el resultado antes de cambiar el estado. No se cierra un artefacto con observaciones críticas o sin evidencia.
