# Plan de Garantía de Calidad

El Plan SQA conserva objetivos, responsables por rol, métricas con meta, pruebas, revisiones y auditorías. No declara ejecución de PSIREG.

## Métricas

| ID | Medida | Cálculo | Meta | Evidencia | Rol |
|---|---|---|---|---|---|
| MC-01 | Cobertura RF | RF con CU, CP y EV / 19 × 100 | 100 % (19 de 19) | Matriz maestra | Responsable de requisitos |
| MC-02 | Cobertura RNF | RNF con CP y EV / 22 × 100 | 100 % (22 de 22) | Matriz maestra | Responsable de requisitos |
| MC-03 | Trazabilidad | Relaciones completas / relaciones requeridas × 100 | 100 % antes de aprobar | Matriz y revisión | Revisor de calidad |
| MC-04 | Disponibilidad | Tiempo disponible / tiempo observado × 100 | Sin indisponibilidad no planificada; mantenimiento con 48 h | Monitoreo | Responsable técnico |
| MC-05 | Respuesta | Tiempo de cada operación | Entre 1 y 10 segundos | Registro de tiempos | Responsable de pruebas |
| MC-06 | Recursos | Máximo observado de CPU y RAM | CPU ≤ 60 % y RAM ≤ 50 % | Monitoreo | Responsable técnico |
| MC-07 | Accesibilidad | Criterios WCAG AA conformes / aplicables × 100 | Todos los criterios AA aplicables | Reporte WCAG | Revisor de calidad |
| MC-08 | Precisión OCR | Campos coincidentes / campos comparados × 100 | 100 % en la muestra definida | Fuente y resultado OCR | Responsable de pruebas |
| MC-09 | Observaciones | Observaciones abiertas por artefacto | 0 para Aprobado o Cerrado | Issues | Responsable del artefacto |
| MC-10 | Evidencia de cierre | Artefactos cerrados con evidencia / cerrados × 100 | 100 % | Dashboard | Coordinador del proceso |

## Casos funcionales

| Caso | RF | CU | Resultado esperado | EV | Estado |
|---|---|---|---|---|---|
| CP-F01 | RF-01 | CU-01 | Permitir el registro mediante correo institucional y los datos personales requeridos por la DNOP. | EV-001 | Pendiente |
| CP-F02 | RF-02 | CU-02 | Validar cédula o correo institucional y contraseña, y dirigir al usuario según su perfil. | EV-001 | Pendiente |
| CP-F03 | RF-03 | CU-03 | Permitir seleccionar psicólogo, fecha y hora disponibles, y registrar el motivo de la solicitud. | EV-002 | Pendiente |
| CP-F04 | RF-04 | CU-04 | Mostrar las opciones disponibles para el estamento del usuario con fecha, hora, lugar y estado. | EV-003 | Pendiente |
| CP-F05 | RF-05 | CU-05 | Mostrar tema, fecha, hora, lugar, público objetivo, requisitos y método de inscripción. | EV-003 | Pendiente |
| CP-F06 | RF-06 | CU-06 | Registrar la inscripción, impedir duplicados y cerrar el registro cuando no existan cupos. | EV-003 | Pendiente |
| CP-F07 | RF-07 | CU-07 | Crear un expediente para quien utiliza por primera vez los servicios y evitar registros duplicados. | EV-004 | Pendiente |
| CP-F08 | RF-08 | CU-08 | Buscar y mostrar expedientes y la información asociada al usuario atendido. | EV-004 | Pendiente |
| CP-F09 | RF-09 | CU-09 | Agregar, modificar o eliminar información autorizada del expediente y confirmar el guardado. | EV-004 | Pendiente |
| CP-F10 | RF-10 | CU-10 | Registrar en el expediente la asignación del Programa de Acompañamiento Psicológico cuando corresponda. | EV-004 | Pendiente |
| CP-F11 | RF-11 | CU-11 | Generar el expediente en PDF para su impresión por personal autorizado. | EV-004 | Pendiente |
| CP-F12 | RF-12 | CU-12 | Escanear expedientes y documentos físicos mediante una librería OCR y asociarlos con la información correspondiente. | EV-005 | Pendiente |
| CP-F13 | RF-13 | CU-13 | Modificar una cita existente y reflejar el nuevo estado o fecha dentro del calendario. | EV-002 | Pendiente |
| CP-F14 | RF-14 | CU-14 | Visualizar citas, actividades, horarios ocupados y disponibilidad antes de realizar una asignación. | EV-002 | Pendiente |
| CP-F15 | RF-15 | CU-15 | Registrar y dar seguimiento a talleres, campañas, visitas, actividades psicoeducativas y otras acciones de la DNOP. | EV-003 | Pendiente |
| CP-F16 | RF-16 | CU-16 | Permitir la consulta del documento asociado al expediente por parte del personal con acceso. | EV-005 | Pendiente |
| CP-F17 | RF-17 | CU-17 | Conservar las actividades y cambios realizados en el sistema para su consulta por personal autorizado. | EV-006 | Pendiente |
| CP-F18 | RF-18 | CU-18 | Generar reportes sobre citas, expedientes, actividades, programas y otros datos autorizados, con exportación a formatos estándar. | EV-006 | Pendiente |
| CP-F19 | RF-19 | CU-19 | Administrar las cuentas autorizadas y aplicar los permisos correspondientes a cada perfil institucional. | EV-001 | Pendiente |

## Verificaciones no funcionales

| Caso | RNF | Meta | EV | Estado |
|---|---|---|---|---|
| CP-NF01 | RNF-01 | La interfaz debe presentar una organización clara, lógica y coherente. | EV-011 | Pendiente |
| CP-NF02 | RNF-02 | Las funciones básicas deben poder aprenderse después de un máximo de 15 minutos de exploración o guía. | EV-012 | Pendiente |
| CP-NF03 | RNF-03 | Las funciones más frecuentes deben estar disponibles en dos clics o menos desde el menú principal. | EV-011 | Pendiente |
| CP-NF04 | RNF-04 | La interfaz debe cumplir al menos el nivel AA de WCAG. | EV-013 | Pendiente |
| CP-NF05 | RNF-05 | Guardar, enviar o modificar datos debe producir una confirmación visible entre 1 y 5 segundos. | EV-013 | Pendiente |
| CP-NF06 | RNF-06 | La interfaz debe permitir cerrar sesión y bloquear la pantalla después de 5 minutos de inactividad. | EV-016 | Pendiente |
| CP-NF07 | RNF-07 | El sistema debe orientar la entrada de datos y presentar información suficiente para completar cada operación. | EV-011 | Pendiente |
| CP-NF08 | RNF-08 | La información sensible solo debe ser accesible para los perfiles autorizados. | EV-016 | Pendiente |
| CP-NF09 | RNF-09 | El servicio debe estar disponible 24 horas al día y 7 días a la semana, salvo mantenimiento notificado con al menos 48 horas. | EV-014 | Pendiente |
| CP-NF10 | RNF-10 | Los datos registrados o digitalizados mediante OCR deben ser correctos, completos y coherentes. | EV-015 | Pendiente |
| CP-NF11 | RNF-11 | El tratamiento de datos debe cumplir la Ley 81 de protección de datos personales y las condiciones éticas aplicables. | EV-018 | Pendiente |
| CP-NF12 | RNF-12 | Las actualizaciones deben evitar pérdida de datos y permitir corregir errores y cambios regulatorios. | EV-019 | Pendiente |
| CP-NF13 | RNF-13 | Las operaciones deben responder entre 1 y 10 segundos según la condición de red. | EV-007 | Pendiente |
| CP-NF14 | RNF-14 | La operación no debe superar 60 % de CPU ni 50 % de RAM en el entorno de prueba definido. | EV-008 | Pendiente |
| CP-NF15 | RNF-15 | El sistema debe funcionar como aplicación web en equipos de escritorio o portátiles con Windows 10 o superior y navegador actualizado, sin instalación adicional; el uso móvil no forma parte del alcance inicial. | EV-020 | Pendiente |
| CP-NF16 | RNF-16 | El sistema debe permitir soporte y mantenimiento por personal técnico autorizado. | EV-019 | Pendiente |
| CP-NF17 | RNF-17 | La solución debe facilitar cambios y extensiones sin afectar las funciones existentes. | EV-019 | Pendiente |
| CP-NF18 | RNF-18 | Las librerías externas deben ser de código abierto o compatibles con el uso institucional, la privacidad y la licencia del sistema. | EV-009 | Pendiente |
| CP-NF19 | RNF-19 | La información sensible debe almacenarse de forma segura, cifrada y bajo control de acceso. | EV-017 | Pendiente |
| CP-NF20 | RNF-20 | El sistema debe ofrecer guía de usuario, preguntas frecuentes, soporte y materiales de ayuda. | EV-012 | Pendiente |
| CP-NF21 | RNF-21 | La comunicación cliente-servidor debe utilizar HTTPS y TLS dentro de la infraestructura institucional; no se contempla operación sin conexión. | EV-017 | Pendiente |
| CP-NF22 | RNF-22 | El sistema debe operar inicialmente de forma autónoma, permitir exportación PDF o Excel y conservar capacidad de integración futura mediante API. | EV-010 | Pendiente |

## Revisiones y auditorías

| Actividad | Momento | Responsable | Criterio de salida |
|---|---|---|---|
| Revisión de línea base | Antes de aprobar diseño o pruebas | Responsable de requisitos y revisor | Sin diferencias abiertas. |
| Revisión de artefacto | Al pasar a En revision | Responsable del artefacto y revisor | Aprobado o Con observaciones. |
| Revisión de evidencia | Antes de Aprobado o Cerrado | Responsable de pruebas y revisor | Evidencia reproducible y relacionada. |
| Auditoría de seguridad | Cuando exista host funcional | Responsable técnico y revisor | Reporte ZAP o causa No ejecutable. |
| Auditoría documental | Antes de consolidar | Coordinador y revisor | Formato y trazabilidad sin observaciones críticas. |
