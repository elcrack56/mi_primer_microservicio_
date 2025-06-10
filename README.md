# Microservicio de Notificación de Incidentes en una Universidad

Este microservicio gestiona el envío de notificaciones relacionadas con incidentes de seguridad informática en una universidad.

## Tecnologías utilizadas
- Python 3.10+
- FastAPI
- Motor (MongoDB async)
- Docker
- Azure

## Configuración
1. Renombra `config/appsettings.example.json` a `appsettings.json` y coloca tu cadena de conexión de MongoDB Atlas.
2. Usa `docker-compose up --build` para ejecutar el servicio localmente.
3. Configura tus variables en Azure App Service para el despliegue.