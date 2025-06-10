from fastapi import APIRouter, Depends
from models.notificacion import Notificacion
from services.notificador_email import NotificadorEmail
from services import db

router = APIRouter(prefix="/notificaciones")

@router.post('/')
async def crear_notificacion(data: Notificacion, servicio=Depends(NotificadorEmail)):
    await db.coleccion.insert_one(data.dict())
    servicio.enviar(data.titulo, data.mensaje, data.destinatario)
    return {"detalle": "Notificación enviada y registrada"}