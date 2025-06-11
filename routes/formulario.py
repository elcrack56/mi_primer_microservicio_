from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models.notificacion import Notificacion
from services.db import coleccion

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def mostrar_formulario(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

@router.post("/notificaciones", response_class=HTMLResponse)
async def enviar_formulario(
    request: Request,
    titulo: str = Form(...),
    mensaje: str = Form(...),
    destinatario: str = Form(...),
    prioridad: str = Form("media")
):
    notificacion = Notificacion(
        titulo=titulo,
        mensaje=mensaje,
        destinatario=destinatario,
        prioridad=prioridad
    )
    await coleccion.insert_one(notificacion.dict())
    return RedirectResponse(url="/", status_code=303)
