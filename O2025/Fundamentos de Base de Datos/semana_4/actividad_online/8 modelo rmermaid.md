erDiagram
    CARRERA {
        varchar cod_carrera PK
        varchar nombre
        int duracion
        varchar jefe_carrera
    }

    ESTUDIANTE {
        varchar rut PK
        varchar nombre
        varchar correo
    }

    ESTUDIANTE_EN_PRACTICA {
        varchar rut PK, FK
        varchar empresa_practica FK
        date fecha_inicio
        date fecha_fin
        int id_tutor FK
    }

    TUTOR {
        int id_tutor PK
        varchar nombre
        varchar correo
    }

    EMPRESA_PRACTICA {
        varchar rut_empresa PK
        varchar nombre
        varchar rubro
    }

    DOCENTE {
        varchar rut_docente PK
        varchar nombre
        varchar correo
        varchar especialidad
    }

    MODULO {
        varchar cod_modulo PK
        varchar nombre
        int horas
        varchar cod_carrera FK
        varchar rut_docente FK
    }

    SALA {
        varchar cod_sala PK
        int capacidad
        varchar edificio
    }

    EVALUACION {
        varchar rut_estudiante PK, FK
        varchar cod_modulo PK, FK
        date fecha PK
        varchar tipo PK
        float nota
    }

    ACTIVIDAD_EXTRACURRICULAR {
        int id_actividad PK
        varchar nombre
        int cupo
    }

    MATRICULA {
        varchar rut_estudiante PK, FK
        varchar cod_carrera PK, FK
        date fecha_matricula 
    }

    PARTICIPACION_ACTIVIDAD {
        varchar rut_estudiante PK, FK
        int id_actividad PK, FK
        varchar rol
    }

    ESTUDIANTE_EN_PRACTICA ||--|| ESTUDIANTE : "es subtipo de"
    ESTUDIANTE_EN_PRACTICA }o--|| TUTOR : "supervisado_por"
    ESTUDIANTE_EN_PRACTICA }o--|| EMPRESA_PRACTICA : "realiza_en"
    MODULO }o--|| CARRERA : "pertenece_a"
    MODULO }o--|| DOCENTE : "impartido_por"
    EVALUACION }o--|| ESTUDIANTE : "evaluado"
    EVALUACION }o--|| MODULO : "corresponde_a"
    MODULO }o--|| SALA : dictado_en
    MATRICULA }o--|| ESTUDIANTE : "matricula_est"
    MATRICULA }o--|| CARRERA : "matricula_carr"
    PARTICIPACION_ACTIVIDAD }o--|| ESTUDIANTE : "participa_est"
    PARTICIPACION_ACTIVIDAD }o--|| ACTIVIDAD_EXTRACURRICULAR : "participa_act"