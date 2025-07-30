# 1. Modelo Conceptual – Notación de Chen
✔️ Entidades con atributos:
Carrera (cod_carrera, nombre, duración, jefe_carrera)
Estudiante (rut, nombre, correo)
Estudiante en práctica (subtipo de Estudiante) → empresa_práctica, fecha_inicio, fecha_fin
Tutor (id_tutor, nombre, correo)
Docente (rut_docente, nombre, correo, especialidad)
Módulo (cod_modulo, nombre, horas)
Sala (cod_sala, capacidad, edificio)
Evaluación (tipo, fecha, nota)
Actividad Extracurricular (id_actividad, nombre, cupo)
Empresa de Práctica (rut_empresa, nombre, rubro)

✔️ Relaciones:
Matricula entre Estudiante y Carrera (N:M)
Imparte entre Docente y Módulo (1:N)
Se dicta en entre Módulo y Sala (1:N)
Evaluado en entre Evaluación, Módulo y Estudiante (relación ternaria)
Participa en entre Estudiante y Actividad Extracurricular (N:M)
Supervisa entre Tutor y Estudiante en Práctica (1:N)
Realiza práctica en entre Estudiante en Práctica y Empresa (1:1)

✔️ Subtipo:
Estudiante en práctica ⊂ Estudiante