# app/core/database.py
from contextlib import asynccontextmanager
from typing import Generator
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import get_settings
settings = get_settings()

# 1. Création de l'engine  -----------------------------
# echo=True ouvre le log SQL ; pratique en dev. Passe à False en prod.
engine = create_engine(settings.database_url, echo=True)

# 2. Dépendance FastAPI pour obtenir une session --------
def get_session() -> Generator[Session, None, None]:
    """
    Dépendance FastAPI (yield) :
    - ouvre une session au début de la requête
    - la ferme automatiquement à la fin
    """
    with Session(engine) as session:
        yield session #ouvre une session, met a disposition la session, et ferme la session apres utilisation
# 3. Initialisation de la base (dev) --------------------
def init_db() -> None:
    """
    Crée toutes les tables définies dans SQLModel.metadata.
    À appeler une seule fois (startup) quand on travaille en SQLite
    ou lors des tout premiers tests.
    En production, on préférera Alembic pour gérer les migrations.
    """
    SQLModel.metadata.create_all(engine)