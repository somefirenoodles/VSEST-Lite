# Instrumento de evaluación del producto

Resultados permitidos: **Cumple**, **Cumple parcialmente**, **No cumple**, **No evaluado** y **No ejecutable**. Los criterios comienzan como No evaluado porque el instrumento no ha sido aplicado. VSEST-Lite controla evidencia y estado; no demuestra funcionamiento de PSIREG.

| ID | Característica | RF/RNF | Criterio | Caso de prueba | Método | Evidencia | Resultado | Observación |
|---|---|---|---|---|---|---|---|---|
| EV-001 | Adecuación funcional | RF-01, RF-02 y RF-19 | Registro, autenticación y acceso por perfil funcionan según la línea base. | CP-F01; CP-F02; CP-F19 | Vitest, Playwright y Newman | Reporte de ejecución | No evaluado | Pendiente de aplicación |
| EV-002 | Adecuación funcional | RF-03, RF-13 y RF-14 | Agendamiento, reprogramación y calendario mantienen disponibilidad y estado. | CP-F03; CP-F13; CP-F14 | Playwright y API | Reporte y capturas | No evaluado | Pendiente de aplicación |
| EV-003 | Adecuación funcional | RF-04, RF-05, RF-06 y RF-15 | Consulta, detalle, inscripción y gestión de actividades cumplen los flujos definidos. | CP-F04 a CP-F06; CP-F15 | Playwright y API | Reporte y datos | No evaluado | Pendiente de aplicación |
| EV-004 | Adecuación funcional | RF-07 a RF-11 | Creación, consulta, actualización, acompañamiento e impresión de expedientes funcionan. | CP-F07 a CP-F11 | Vitest, Playwright y API | Reporte y PDF | No evaluado | Pendiente de aplicación |
| EV-005 | Adecuación funcional | RF-12 y RF-16 | Digitalización y visualización relacionan correctamente el documento con el expediente. | CP-F12; CP-F16 | Prueba OCR y Playwright | Fuente y resultado | No evaluado | Pendiente de aplicación |
| EV-006 | Adecuación funcional | RF-17 y RF-18 | El historial y los reportes conservan operaciones autorizadas y exportación. | CP-F17; CP-F18 | Playwright y API | Bitácora y reporte | No evaluado | Pendiente de aplicación |
| EV-007 | Eficiencia de desempeño | RNF-13 | Las operaciones responden entre 1 y 10 segundos. | CP-NF13 | Playwright y Newman | Tiempos | No evaluado | Pendiente de aplicación |
| EV-008 | Eficiencia de desempeño | RNF-14 | CPU no supera 60 % y RAM no supera 50 % en el entorno definido. | CP-NF14 | Monitoreo | CPU y RAM | No evaluado | Pendiente de aplicación |
| EV-009 | Compatibilidad | RNF-18 | Los componentes externos cumplen licencia, privacidad y uso institucional. | CP-NF18 | Revisión de dependencias | Inventario y licencias | No evaluado | Pendiente de aplicación |
| EV-010 | Compatibilidad | RNF-22 | La operación autónoma, exportación y capacidad futura de integración corresponden al alcance. | CP-NF22 | Prueba y revisión | PDF, Excel e interfaz | No evaluado | Pendiente de aplicación |
| EV-011 | Usabilidad | RNF-01, RNF-03 y RNF-07 | La interfaz es clara, orienta la entrada y permite acceder a funciones frecuentes en dos clics o menos. | CP-NF01; CP-NF03; CP-NF07 | Observación y Playwright | Registro de pasos | No evaluado | Pendiente de aplicación |
| EV-012 | Usabilidad | RNF-02 y RNF-20 | Las funciones básicas se aprenden en 15 minutos y existe ayuda suficiente. | CP-NF02; CP-NF20 | Observación guiada | Guion y resultados | No evaluado | Pendiente de aplicación |
| EV-013 | Usabilidad | RNF-04 y RNF-05 | La interfaz cumple WCAG AA y confirma operaciones entre 1 y 5 segundos. | CP-NF04; CP-NF05 | Playwright y revisión WCAG | Reporte | No evaluado | Pendiente de aplicación |
| EV-014 | Fiabilidad | RNF-09 | El servicio mantiene disponibilidad 24/7 salvo mantenimiento anunciado con 48 horas. | CP-NF09 | Monitoreo | Registro de disponibilidad | No evaluado | Pendiente de aplicación |
| EV-015 | Fiabilidad | RNF-10 | Los datos registrados y digitalizados son correctos, completos y coherentes. | CP-NF10 | Comparación de datos y OCR | Muestra y diferencias | No evaluado | Pendiente de aplicación |
| EV-016 | Seguridad | RNF-06 y RNF-08 | Sesión, bloqueo y permisos impiden acceso a perfiles no autorizados. | CP-NF06; CP-NF08 | Playwright, Newman y revisión | Pruebas por perfil | No evaluado | Pendiente de aplicación |
| EV-017 | Seguridad | RNF-19 y RNF-21 | Almacenamiento, HTTPS y TLS protegen la información sensible. | CP-NF19; CP-NF21 | Revisión, Newman y ZAP | Configuración y ZAP | No evaluado | Pendiente de aplicación |
| EV-018 | Seguridad | RNF-11 | El tratamiento de datos cumple la Ley 81 y las condiciones éticas aplicables. | CP-NF11 | Checklist de privacidad | Checklist | No evaluado | Pendiente de aplicación |
| EV-019 | Mantenibilidad | RNF-12, RNF-16 y RNF-17 | Actualizaciones, soporte y cambios se realizan sin pérdida ni regresión. | CP-NF12; CP-NF16; CP-NF17 | SonarQube y prueba de cambio | Reporte y cambio | No evaluado | Pendiente de aplicación |
| EV-020 | Portabilidad | RNF-15 | El producto funciona en el entorno web de escritorio definido sin afirmar soporte móvil. | CP-NF15 | Playwright en entorno objetivo | Reporte de compatibilidad | No evaluado | Pendiente de aplicación |
