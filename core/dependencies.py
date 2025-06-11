from fastapi import FastAPI
from core.interfaces.notificador_interface import NotificadorInterface
from services.notificador_email import NotificadorEmail

notificador: NotificadorInterface = NotificadorEmail()

def get_notificador() -> NotificadorInterface:
    return notificador

def configurar_dependencias(app: FastAPI):
    @app.get("/health")
    async def health_check():
        return {"status": "ok"}
