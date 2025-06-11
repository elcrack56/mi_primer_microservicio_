from fastapi import FastAPI
from routes import notificaciones, formulario
from core.dependencies import configurar_dependencias

def create_app() -> FastAPI:
    app = FastAPI(title='Microservicio de Notificación de Incidentes')
    app.include_router(notificaciones.router)
    app.include_router(formulario.router)
    configurar_dependencias(app)
    return app

app = create_app()
