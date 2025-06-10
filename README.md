## Microservicio de Notificación de Incidentes en una Universidad

Este microservicio gestiona el envío y almacenamiento de notificaciones relacionadas con incidentes de una universidad.

## Tecnologías utilizadas

- Python 3.10+

- FastAPI (API web asíncrona)

- Motor (cliente asíncrono para MongoDB)

- MongoDB Atlas (base de datos NoSQL)

- Docker & Docker Compose (contenedorización)

- python-multipart (para manejo de formularios multipart)

- Jinja2 (plantillas HTML)


## Características

- Recepción y almacenamiento de notificaciones de incidentes en MongoDB.

- Manejo asíncrono para mayor rendimiento y escalabilidad.

- Formulario HTML para enviar notificaciones.

- Contenedorización con Docker para fácil despliegue.

- Endpoint /health para verificar el estado del servicio.

## Requisitos previos

- Tener instalado Docker y Docker Compose.

- Cuenta y cluster de MongoDB Atlas (u otra instancia de MongoDB accesible).

- Conexión a Internet para descargar imágenes Docker y paquetes.

## comando para levantar servidor

docker-compose up --build

## URL funcional

http://localhost:8000

## URL para ver el estado de la app

http://localhost:8000/health

## Las notificaciones Mongo DB

Las notificaciones enviadas se almacenan en la colección notificaciones en MongoDB.

## Mejoras futuras

- Añadir autenticación y autorización para enviar notificaciones.

- Implementar sistema de notificaciones vía correo o mensajería externa.

- Agregar métricas y trazabilidad (observabilidad).

- Despliegue en la nube (Azure).