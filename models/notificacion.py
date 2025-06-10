from pydantic import BaseModel
from typing import Optional

class Notificacion(BaseModel):
    titulo: str
    mensaje: str
    destinatario: str
    prioridad: Optional[str] = 'media'