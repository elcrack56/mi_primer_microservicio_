from fastapi import APIRouter, HTTPException
from models.notificacion import Notificacion
from services.db import coleccion
from bson import ObjectId

router = APIRouter()

@router.post("/notificaciones")
async def crear_notificacion(notificacion: Notificacion):
    resultado = await coleccion.insert_one(notificacion.dict())
    return {
        "id": str(resultado.inserted_id),
        "mensaje": "Notificación guardada exitosamente"
    }

@router.get("/notificaciones")
async def listar_notificaciones():
    notificaciones = []
    async for documento in coleccion.find():
        documento["_id"] = str(documento["_id"])  # Convertir ObjectId a string
        notificaciones.append(documento)
    return notificaciones
