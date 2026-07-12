# Diseño del sistema PSIREG

Las pantallas y vistas arquitectónicas se identifican como **diseño propuesto, no implementado**. Proceden del Documento de Arquitectura y Diseño de Software de PSIREG y sirven para preparar pruebas; no constituyen evidencia de ejecución.

| ID | Pantalla | RF | RNF | CU | EV | CP | Fuente |
|---|---|---|---|---|---|---|---|
| DS-01 | Digitalización de documentos | RF-12; RF-16 | RNF-01; RNF-05; RNF-07; RNF-08; RNF-10 | CU-12; CU-16 | EV-005; EV-013; EV-015; EV-016 | CP-F12; CP-F16; CP-NF10 | Documento de Arquitectura, p. 32 |
| DS-02 | Creación de actividades | RF-15 | RNF-01; RNF-05; RNF-07; RNF-08 | CU-15 | EV-003; EV-013; EV-016 | CP-F15; CP-NF05; CP-NF08 | Documento de Arquitectura, p. 35 |
| DS-03 | Agendamiento de citas | RF-03; RF-14 | RNF-01; RNF-03; RNF-05; RNF-08; RNF-13 | CU-03; CU-14 | EV-002; EV-007; EV-011; EV-013; EV-016 | CP-F03; CP-F14; CP-NF13 | Documento de Arquitectura, p. 37 |
| DS-04 | Creación de expedientes | RF-07; RF-17 | RNF-05; RNF-07; RNF-08; RNF-10; RNF-19 | CU-07; CU-17 | EV-004; EV-015; EV-016; EV-017 | CP-F07; CP-F17; CP-NF10; CP-NF19 | Documento de Arquitectura, p. 39 |
| DS-05 | Impresión y exportación de expedientes | RF-11; RF-18 | RNF-05; RNF-08; RNF-13; RNF-15; RNF-22 | CU-11; CU-18 | EV-004; EV-006; EV-007; EV-010; EV-020 | CP-F11; CP-F18; CP-NF13; CP-NF22 | Documento de Arquitectura, p. 42 |
| DS-06 | Inscripción en actividades | RF-04; RF-05; RF-06 | RNF-01; RNF-03; RNF-05; RNF-07; RNF-08 | CU-04; CU-05; CU-06 | EV-003; EV-011; EV-013; EV-016 | CP-F04; CP-F05; CP-F06 | Documento de Arquitectura, p. 45 |

## Vistas arquitectónicas recuperadas

- Vista de puesta en marcha: cliente web, servidor de aplicación y servidor de base de datos.
- Vista de procesos: autenticación, citas, expedientes, actividades y reportes.
- Vista de implementación: interfaz, servicios, acceso a datos y componentes externos.
- Dependencias: pantallas, controladores, servicios, repositorios, OCR y exportación.
- Vista de datos: usuarios, perfiles, citas, actividades, expedientes y documentos.
