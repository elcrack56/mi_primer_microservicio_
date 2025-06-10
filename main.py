from fastapi import FastAPI
from routes import notificaciones

app = FastAPI(title='Microservicio de Notificación de Incidentes')

app.include_router(notificaciones.router)

@app.get('/')
def root():
    return {"message": "Microservicio de Notificaciones activo"}