erDiagram
    CARRERA {
        string cod_carrera PK
        string nombre
        int duracion
        string jefe_carrera
    }

    ESTUDIANTE {
        string rut PK
        string nombre
        string correo
    }

    ESTUDIANTE_EN_PRACTICA {
        string rut PK, FK
        string empresa_practica
        date fecha_inicio
        date fecha_fin
        int rut_tutor FK
    }

    TUTOR {
        int id_tutor PK
        string nombre
        string correo
    }

    EMPRESA_PRACTICA {
        string rut_empresa PK
        string nombre
        string rubro
    }

    DOCENTE {
        string rut_docente PK
        string nombre
        string correo
        string especialidad
    }

    MODULO {
        string cod_modulo PK
        string nombre
        int horas
        string cod_carrera FK
        string rut_docente FK
    }

    SALA {
        string cod_sala PK
        int capacidad
        string edificio
    }

    EVALUACION {
        string rut_estudiante PK, FK
        string cod_modulo PK, FK
        date fecha PK
        string tipo PK
        float nota
    }

    ACTIVIDAD_EXTRACURRICULAR {
        int id_actividad PK
        string nombre
        int cupo
    }

    MATRICULA {
        string rut_estudiante PK, FK
        string cod_carrera PK, FK
        date fecha_matricula
    }

    PARTICIPACION_ACTIVIDAD {
        string rut_estudiante PK, FK
        int id_actividad PK, FK
        string rol
    }

    ESTUDIANTE_EN_PRACTICA ||--|| ESTUDIANTE : es
    ESTUDIANTE_EN_PRACTICA }o--|| TUTOR : supervisado_por
    ESTUDIANTE_EN_PRACTICA }o--|| EMPRESA_PRACTICA : realiza_en
    MODULO }o--|| CARRERA : pertenece_a
    MODULO }o--|| DOCENTE : impartido_por
    EVALUACION }o--|| ESTUDIANTE : evaluado
    EVALUACION }o--|| MODULO : sobre
    MODULO }o--|| SALA : dictado_en
    MATRICULA }o--|| ESTUDIANTE : matricula_est
    MATRICULA }o--|| CARRERA : matricula_carr
    PARTICIPACION_ACTIVIDAD }o--|| ESTUDIANTE : participa_est
    PARTICIPACION_ACTIVIDAD }o--|| ACTIVIDAD_EXTRACURRICULAR : participa_act