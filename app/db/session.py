import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Por ejemplo, usando el driver pymysql para MySQL:
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:sightofthesunshine@localhost/chacharitas")

# Crea el engine, puedes agregar opciones como pool_pre_ping para detectar conexiones inactivas.
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Crea una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función de dependencia para inyectar la sesión en tus endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
