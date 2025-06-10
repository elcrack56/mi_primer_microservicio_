from abc import ABC, abstractmethod

class NotificadorInterface(ABC):
    @abstractmethod
    def enviar(self, titulo: str, mensaje: str, destinatario: str):
        pass