# Especificaciones de casos de uso principales

Las especificaciones siguientes completan CU-02, CU-03, CU-07, CU-12, CU-18 y CU-19. Se derivan exclusivamente de la Visión, la ERS y el Documento de Arquitectura de PSIREG. Describen comportamiento esperado y **no evidencian implementación**.

## CU-02 - Autenticar usuario

| Campo | Especificación |
|---|---|
| Objetivo | Validar la identidad del usuario y habilitar únicamente las funciones correspondientes a su perfil. |
| Fuente | ERS 3.1.2; Visión 5. |
| Actor principal | Todos los usuarios registrados. |
| Precondiciones | La cuenta existe, está habilitada y dispone de un perfil autorizado. |
| Disparador | El usuario solicita iniciar sesión. |
| Flujo básico | 1. El usuario introduce cédula o correo institucional y contraseña. 2. El sistema valida los datos. 3. El sistema identifica el perfil. 4. El sistema inicia la sesión. 5. El sistema dirige al usuario al entorno autorizado. |
| Flujos alternos y excepciones | Credenciales inválidas: se rechaza el acceso y se informa el error. Cuenta inactiva o perfil no autorizado: no se inicia sesión y se informa la restricción. |
| Postcondición | Existe una sesión activa asociada al usuario y a su perfil; en caso de error no se crea sesión. |
| Trazabilidad | RF-02; RF-19; RNF-06; RNF-08; RNF-19; RNF-21; CP-F02; EV-001; EV-016; EV-017. |

## CU-03 - Agendar cita

| Campo | Especificación |
|---|---|
| Objetivo | Registrar una cita con un psicólogo en una fecha y hora disponibles. |
| Fuente | ERS 3.1.3; Documento de Arquitectura, pp. 17-20 y 36-37. |
| Actor principal | Estudiante, docente o investigador. |
| Precondiciones | El usuario inició sesión; existen psicólogos y horarios registrados. |
| Disparador | El usuario selecciona la opción para agendar una cita. |
| Flujo básico | 1. El sistema muestra psicólogos y disponibilidad. 2. El usuario selecciona psicólogo, fecha y hora. 3. El usuario registra el motivo. 4. El sistema valida disponibilidad y datos. 5. El sistema registra la cita y muestra confirmación. |
| Flujos alternos y excepciones | Horario ocupado: el sistema rechaza la selección y solicita otro horario. Datos incompletos: se señalan los campos requeridos. |
| Postcondición | La cita queda registrada y visible en el calendario con su estado inicial. |
| Trazabilidad | RF-03; RF-14; RNF-01; RNF-03; RNF-05; RNF-08; RNF-13; CP-F03; EV-002; EV-007; EV-011; EV-013; EV-016. |

## CU-07 - Crear expediente

| Campo | Especificación |
|---|---|
| Objetivo | Crear un expediente para una persona atendida por primera vez, evitando duplicados. |
| Fuente | ERS 3.1.7; Documento de Arquitectura, pp. 21-24 y 38-40. |
| Actor principal | Psicólogo o personal administrativo autorizado. |
| Precondiciones | El actor inició sesión y dispone de permisos; la persona está identificada. |
| Disparador | El actor solicita crear un nuevo expediente. |
| Flujo básico | 1. El actor busca a la persona. 2. El sistema verifica que no exista un expediente. 3. El actor introduce los datos requeridos. 4. El sistema valida la información. 5. El sistema crea el expediente y confirma el guardado. |
| Flujos alternos y excepciones | Expediente existente: el sistema impide el duplicado y muestra el registro disponible. Datos incompletos o inválidos: no se guarda y se señalan los campos. |
| Postcondición | Existe un expediente único asociado a la persona y a las operaciones registradas. |
| Trazabilidad | RF-07; RF-17; RNF-05; RNF-07; RNF-08; RNF-10; RNF-19; CP-F07; EV-004; EV-015; EV-016; EV-017. |

## CU-12 - Digitalizar documentos con OCR

| Campo | Especificación |
|---|---|
| Objetivo | Capturar un documento físico o cargar un archivo, obtener su contenido mediante OCR y asociarlo con el expediente correspondiente. |
| Fuente | ERS 3.1.12; Documento de Arquitectura, pp. 10-13 y 33. |
| Actor principal | Psicólogo o personal administrativo autorizado. |
| Precondiciones | El actor inició sesión, seleccionó un expediente y dispone del documento; para escaneo, el dispositivo de captura está disponible. |
| Disparador | El actor selecciona escanear o subir un documento. |
| Flujo básico | 1. El sistema habilita captura o carga. 2. El actor obtiene o selecciona la imagen. 3. El sistema procesa el contenido mediante OCR. 4. El sistema muestra una vista previa. 5. El actor verifica el resultado. 6. El sistema asocia y guarda el documento en el expediente. |
| Flujos alternos y excepciones | Error de dispositivo: se informa la causa y no se guarda. Documento ilegible: se solicita una nueva captura. Cancelación: se descartan los cambios no guardados. |
| Postcondición | El documento y el resultado OCR quedan asociados al expediente, o la operación termina sin modificarlo. |
| Trazabilidad | RF-12; RF-16; RNF-05; RNF-08; RNF-10; RNF-18; RNF-19; CP-F12; EV-005; EV-009; EV-015; EV-016; EV-017. |

## CU-18 - Generar reportes

| Campo | Especificación |
|---|---|
| Objetivo | Obtener información consolidada de citas, expedientes, actividades, programas y otros datos autorizados. |
| Fuente | Visión 2.1, 3.4 y 5; ERS 3.9.3. |
| Actor principal | Director o personal autorizado. |
| Precondiciones | El actor inició sesión, dispone del permiso correspondiente y existen datos consultables. |
| Disparador | El actor solicita un reporte. |
| Flujo básico | 1. El sistema muestra los tipos de reporte y filtros disponibles. 2. El actor selecciona alcance y filtros. 3. El sistema valida la solicitud. 4. El sistema genera y presenta el reporte. 5. El actor puede exportarlo a un formato estándar autorizado. |
| Flujos alternos y excepciones | Sin resultados: se informa que no existen datos para los filtros. Error de exportación: se conserva la consulta y se informa el fallo. |
| Postcondición | El reporte se visualiza y, cuando se solicita, se genera el archivo de exportación. |
| Trazabilidad | RF-18; RNF-05; RNF-08; RNF-13; RNF-15; RNF-22; CP-F18; EV-006; EV-007; EV-010; EV-016; EV-020. |

## CU-19 - Gestionar cuentas y acceso por rol

| Campo | Especificación |
|---|---|
| Objetivo | Administrar cuentas autorizadas y asignar permisos conforme al perfil institucional. |
| Fuente | Visión 5; ERS 3.1.1, 3.1.2 y 3.9.1. |
| Actor principal | Director o personal administrativo autorizado. |
| Precondiciones | El actor inició sesión y dispone del permiso de administración de cuentas. |
| Disparador | El actor solicita crear, consultar o modificar una cuenta. |
| Flujo básico | 1. El actor busca o inicia el registro de la cuenta. 2. El sistema valida los datos institucionales. 3. El actor selecciona el perfil permitido. 4. El sistema valida la asignación. 5. El sistema guarda los cambios, registra la operación y confirma el resultado. |
| Flujos alternos y excepciones | Cuenta duplicada: se impide la creación. Perfil no permitido o privilegio insuficiente: se rechaza la operación. Datos incompletos: se solicita corrección. |
| Postcondición | La cuenta conserva un estado y un perfil autorizados; la operación queda registrada. |
| Trazabilidad | RF-01; RF-02; RF-17; RF-19; RNF-06; RNF-08; RNF-11; RNF-19; RNF-21; CP-F19; EV-001; EV-016; EV-017; EV-018. |
