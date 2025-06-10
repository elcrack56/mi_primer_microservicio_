from motor.motor_asyncio import AsyncIOMotorClient
from config.config import settings

client = AsyncIOMotorClient(settings.db_url)
db = client.get_default_database()
coleccion = db['notificaciones']