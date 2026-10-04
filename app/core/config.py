from functools import lru_cache
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR=Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    project_name: str = "ShopFlow API"
    api_prefix:   str = "/api"
    # ---- BDD ----
    # En dev : fichier SQLite dans la racine ; en prod on remplacera par Postgres via .env
    database_url: str = "postgresql://postgres:lawrynn@127.0.0.1:5432/shopflow"
    # ---- Sécurité JWT ----
    secret_key: str = "A CHANGER"                      # *à surcharger via .env*
    access_token_expire_minutes: int = 30             # durée de vie des tokens
# ---- Classe interne Pydantic ----
    class Config:
        env_file = ".env"               # s'il existe, on le charge automatiquement
        env_file_encoding = "utf-8"

# 2) Instance unique en mémoire : évite de relire le disque à chaque import
@lru_cache
def get_settings() -> Settings:
    return Settings()