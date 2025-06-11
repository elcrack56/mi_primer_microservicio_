from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from models.notificacion import Notificacion
from services import db
from core.dependencies import get_notificador
from core.interfaces.notificador_interface import NotificadorInterface

router = APIRouter(prefix="/notificaciones")

@router.post("/")
async def crear_notificacion(
    data: Notificacion,
    notificador: NotificadorInterface = Depends(get_notificador)
):
    await db.coleccion.insert_one(data.dict())
    notificador.enviar(data.titulo, data.mensaje, data.destinatario)
    return {"detalle": "Notificación enviada y registrada"}

@router.get("/", response_class=JSONResponse)
async def listar_notificaciones():
    items = await db.coleccion.find().to_list(100)
    return items