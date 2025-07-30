# Caso de Estudio: Sistema de Gestión Académica – INACAP Ñuñoa

## Contexto:
La sede INACAP Ñuñoa desea implementar un sistema para gestionar las actividades académicas, administrativas y de evaluación de los estudiantes. Este sistema debe organizar la información de carreras, módulos, docentes, estudiantes, matrículas, evaluaciones y actividades extracurriculares. Se debe representar tanto a los estudiantes regulares como a estudiantes en práctica (subtipo), quienes requieren asignación de tutores.

## Requisitos del sistema:
Carrera: Cada carrera tiene un código, nombre, duración y jefe de carrera.
Estudiante: Tiene RUT, nombre, correo, y puede estar matriculado en una o más carreras.
Estudiante en práctica (subtipo de Estudiante): Se diferencia porque tiene un tutor asignado y empresa de práctica.
Docente: Cada docente imparte uno o varios módulos en diferentes carreras.
Módulo: Tiene código, nombre, y cantidad de horas. Se dicta dentro de una carrera y lo imparte un docente.
Evaluación: Un estudiante puede rendir varias evaluaciones por módulo. Cada evaluación tiene fecha, tipo (certamen, control, proyecto) y nota.
Sala: Cada módulo se imparte en una sala específica. Las salas tienen capacidad y están en un edificio determinado.
Actividad Extracurricular: Los estudiantes pueden inscribirse en talleres o actividades como deportes, emprendimiento, inglés, etc.
Tutor: Profesionales encargados de supervisar a los estudiantes en práctica. Cada tutor puede supervisar a varios estudiantes.

## Requisitos especiales:
El subtipo Estudiante en práctica debe identificarse claramente con una relación a su tutor y a la empresa.
La relación entre estudiantes y carreras es de muchos a muchos, ya que pueden cambiar de carrera o cursar más de una.
Las evaluaciones están relacionadas con un módulo y un estudiante, y deben ser identificadas de forma compuesta.
Las actividades extracurriculares pueden tener cupos limitados, y se registra la participación de los estudiantes.

## Entidades (mínimo 8 + subtipo):
Carrera
Estudiante
Estudiante en práctica (subtipo de Estudiante)
Docente
Módulo
Evaluación
Sala
Actividad Extracurricular
Tutor
Empresa de Práctica