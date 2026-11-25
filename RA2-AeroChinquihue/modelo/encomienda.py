from dataclasses import dataclass
from modelo.destino import destino

@dataclass
class encomienda:
    """paquete entregado en La Paloma para envio a un destino."""
    codigo: str
    remitente: str
    destinatario: str
    destino: destino
    peso_kg: float
    precio: int
    fecha_entrega: str = "Por confirmar..."
