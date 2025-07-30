# 1.4. SQLAlchemy
"""
SQLAlchemy es una biblioteca de Python que facilita el trabajo con bases de datos relacionales. 
Proporciona una API de alto nivel para trabajar con bases de datos SQL de manera más abstracta y eficiente que utilizando directamente SQL. 
SQLAlchemy es muy flexible y se puede usar con una variedad de motores de base de datos.
"""
"""
✅ Buenas prácticas demostradas:
    ORM con SQLAlchemy = modelo seguro y limpio.
    Prevención de inyección SQL automática.
    merge() permite actualizar sin duplicar.
    Separación clara entre lógica de datos y de presentación.
"""
import sys
import pandas as pd

# Intentar instalar SQLAlchemy si no está instalado
try:
    from sqlalchemy import create_engine, Column, Integer, String
    from sqlalchemy.orm import declarative_base, sessionmaker
except ImportError:
    print("❌ No se encontró SQLAlchemy. Instalando...")
    try:
        import pip
        pip.main(['install', 'sqlalchemy'])
    except Exception as install_error:
        print(f"❌ Error al instalar SQLAlchemy: {install_error}")
        sys.exit(1)
    from sqlalchemy import create_engine, Column, Integer, String
    from sqlalchemy.orm import declarative_base, sessionmaker

# Validar argumento
if len(sys.argv) < 2:
    print("Uso: python 04.py <archivo.csv>")
    sys.exit(1)

archivo_csv = sys.argv[1]

# Cargar datos
try:
    df = pd.read_csv(archivo_csv, dtype=str)
    columnas = {"id", "nombre", "email"}
    if not columnas.issubset(df.columns):
        raise ValueError("El archivo debe tener columnas: id, nombre, email")
except Exception as e:
    print(f"❌ Error al leer CSV: {e}")
    sys.exit(1)

# Configurar SQLAlchemy
Base = declarative_base()
engine = create_engine('sqlite:///usuarios_orm.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Definir tabla como clase Python
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}')>"

# Crear tabla
Base.metadata.create_all(engine)

# Insertar datos
for _, fila in df.iterrows():
    try:
        usuario = Usuario(
            id=int(fila["id"]),
            nombre=fila["nombre"].strip(),
            email=fila["email"].strip().lower()
        )
        session.merge(usuario)  # Inserta o actualiza
    except Exception as fila_error:
        print(f"⚠️ Error con fila {fila.to_dict()} → {fila_error}")

session.commit()

# Mostrar usuarios
usuarios = session.query(Usuario).all()
for u in usuarios:
    print(u)

session.close()
