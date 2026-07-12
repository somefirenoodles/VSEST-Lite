# Diseño del sistema PSIREG

Las pantallas, modelos y vistas arquitectónicas de esta sección se clasifican como **diseño propuesto, no implementado**. Proceden del Documento de Arquitectura y Diseño de Software de PSIREG. Su función es relacionar el diseño con requisitos, casos de uso, criterios de evaluación y pruebas futuras; no constituyen evidencia de ejecución.

## Representación gráfica del modelo de casos de uso

El modelo gráfico se encuentra en la página 9 del Documento de Arquitectura. Representa las interacciones previstas entre los usuarios institucionales y las funciones de acceso, citas, actividades, expedientes, documentos y administración. La versión gráfica debe insertarse en el documento final con el rótulo **Figura: Modelo de casos de uso propuesto de PSIREG**.

## Pantallas propuestas

| ID | Pantalla o grupo | RF | RNF | CU | EV | CP | Fuente |
|---|---|---|---|---|---|---|---|
| DS-01 | Digitalización de documentos | RF-12; RF-16 | RNF-01; RNF-05; RNF-07; RNF-08; RNF-10; RNF-18; RNF-19 | CU-12; CU-16 | EV-005; EV-009; EV-013; EV-015; EV-016; EV-017 | CP-F12; CP-F16; CP-NF10; CP-NF18; CP-NF19 | Documento de Arquitectura, p. 33 |
| DS-02 | Creación y validación de actividades | RF-15 | RNF-01; RNF-05; RNF-07; RNF-08 | CU-15 | EV-003; EV-011; EV-013; EV-016 | CP-F15; CP-NF01; CP-NF05; CP-NF08 | Documento de Arquitectura, pp. 34-35 |
| DS-03 | Agendamiento de citas y disponibilidad | RF-03; RF-14 | RNF-01; RNF-03; RNF-05; RNF-08; RNF-13 | CU-03; CU-14 | EV-002; EV-007; EV-011; EV-013; EV-016 | CP-F03; CP-F14; CP-NF03; CP-NF05; CP-NF13 | Documento de Arquitectura, pp. 36-37 |
| DS-04 | Consulta y creación de expedientes | RF-07; RF-08; RF-17 | RNF-05; RNF-07; RNF-08; RNF-10; RNF-19 | CU-07; CU-08; CU-17 | EV-004; EV-006; EV-015; EV-016; EV-017 | CP-F07; CP-F08; CP-F17; CP-NF10; CP-NF19 | Documento de Arquitectura, pp. 38-40 |
| DS-05 | Impresión y exportación de expedientes | RF-11; RF-18 | RNF-05; RNF-08; RNF-13; RNF-15; RNF-22 | CU-11; CU-18 | EV-004; EV-006; EV-007; EV-010; EV-016; EV-020 | CP-F11; CP-F18; CP-NF13; CP-NF15; CP-NF22 | Documento de Arquitectura, pp. 41-43 |
| DS-06 | Consulta e inscripción en actividades | RF-04; RF-05; RF-06 | RNF-01; RNF-03; RNF-05; RNF-07; RNF-08 | CU-04; CU-05; CU-06 | EV-003; EV-011; EV-013; EV-016 | CP-F04; CP-F05; CP-F06; CP-NF03; CP-NF05 | Documento de Arquitectura, pp. 44-45 |

## Componentes y vistas arquitectónicas propuestas

| ID | Vista o componente | Descripción | RF | RNF | CU | EV / CP | Fuente |
|---|---|---|---|---|---|---|---|
| ARQ-01 | Puesta en marcha | Cliente web, red institucional, servidor de aplicación y servidor de base de datos. | RF-01 a RF-19 | RNF-09; RNF-13; RNF-14; RNF-15; RNF-19; RNF-21 | CU-01 a CU-19 | EV-007; EV-008; EV-014; EV-017; EV-020 / CP-NF09; CP-NF13; CP-NF14; CP-NF15; CP-NF19; CP-NF21 | Documento de Arquitectura, p. 66 |
| ARQ-02 | Procesos | Procesos concurrentes previstos para documentos, impresión, expedientes, actividades y tareas. | RF-07; RF-11; RF-12; RF-15; RF-18 | RNF-10; RNF-12; RNF-13; RNF-14 | CU-07; CU-11; CU-12; CU-15; CU-18 | EV-004; EV-005; EV-006; EV-007; EV-008; EV-015; EV-019 / casos CP relacionados | Documento de Arquitectura, p. 67 |
| ARQ-03 | Implementación y dependencias | Interfaces, controladores, dominio, servicios, repositorios, OCR y exportación. | RF-01 a RF-19 | RNF-12; RNF-16; RNF-17; RNF-18; RNF-22 | CU-01 a CU-19 | EV-009; EV-010; EV-019 / CP-NF12; CP-NF16; CP-NF17; CP-NF18; CP-NF22 | Documento de Arquitectura, pp. 68-69 |
| ARQ-04 | Datos | Estructura propuesta para usuarios, perfiles, citas, actividades, expedientes, documentos y relaciones. | RF-01; RF-03; RF-06 a RF-10; RF-12; RF-15 a RF-19 | RNF-08; RNF-10; RNF-11; RNF-19 | CU-01; CU-03; CU-06 a CU-10; CU-12; CU-15 a CU-19 | EV-001 a EV-006; EV-015 a EV-018 / casos CP relacionados | Documento de Arquitectura, p. 70 |

## Regla de evaluación

Cada figura o pantalla solo puede utilizarse como evidencia de diseño. Para registrar **Cumple** o **Cumple parcialmente** se requiere ejecutar el caso de prueba correspondiente y adjuntar evidencia reproducible. Cuando no existe interfaz, código, endpoint o entorno, el resultado aplicable es **No evaluado** o **No ejecutable**, según la causa documentada.
