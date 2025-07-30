erDiagram
    CARRERA {
        string cod_carrera
        string nombre
        int duración
        string jefe_carrera
    }

    ESTUDIANTE {
        string rut
        string nombre
        string correo
    }

    ESTUDIANTE_EN_PRACTICA {
        string empresa_práctica
        date fecha_inicio
        date fecha_fin
    }

    TUTOR {
        int id_tutor
        string nombre
        string correo
    }

    DOCENTE {
        string rut_docente
        string nombre
        string correo
        string especialidad
    }

    MODULO {
        string cod_modulo
        string nombre
        int horas
    }

    SALA {
        string cod_sala
        int capacidad
        string edificio
    }

    EVALUACION {
        string tipo
        date fecha
        float nota
    }

    ACTIVIDAD_EXTRACURRICULAR {
        int id_actividad
        string nombre
        int cupo
    }

    EMPRESA_PRACTICA {
        string rut_empresa
        string nombre
        string rubro
    }

    ESTUDIANTE ||--|| ESTUDIANTE_EN_PRACTICA : es_subtipo
    ESTUDIANTE }|..|{ CARRERA : Matricula
    DOCENTE ||--|{ MODULO : Imparte
    MODULO ||--|{ SALA : "Se dicta en"
    EVALUACION }|--|{ MODULO : "Evaluado en"
    EVALUACION }|--|{ ESTUDIANTE : "Evaluado en"
    ESTUDIANTE }|..|{ ACTIVIDAD_EXTRACURRICULAR : "Participa en"
    TUTOR ||--|{ ESTUDIANTE_EN_PRACTICA : Supervisa
    ESTUDIANTE_EN_PRACTICA ||--|| EMPRESA_PRACTICA : "Realiza práctica en"