import os

class Settings:
    def __init__(self):
        self.db_url = os.getenv("DATABASE_URL")
        self.secret_key = os.getenv("SECRET_KEY")

        if not self.db_url or not self.secret_key:
            raise Exception("Faltan variables de entorno necesarias: DATABASE_URL y/o SECRET_KEY")

settings = Settings()

