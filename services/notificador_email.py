from core.interfaces.notificador_interface import NotificadorInterface

class NotificadorEmail(NotificadorInterface):
    def enviar(self, titulo: str, mensaje: str, destinatario: str):
        print(f"Enviando Email a {destinatario}: {titulo} - {mensaje}")