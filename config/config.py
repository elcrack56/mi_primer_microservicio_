import json

class Settings:
    def __init__(self, path='config/appsettings.json'):
        with open(path) as f:
            config = json.load(f)
        self.db_url = config['DATABASE_URL']
        self.secret = config['SECRET_KEY']

settings = Settings()