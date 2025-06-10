from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from routes import notificaciones
from services.db import coleccion
from models.notificacion import Notificacion

app = FastAPI(title='Microservicio de Notificación de Incidentes')

templates = Jinja2Templates(directory="templates")

app.include_router(notificaciones.router)

@app.get("/", response_class=HTMLResponse)
async def mostrar_formulario(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

@app.post("/notificaciones", response_class=HTMLResponse)
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

