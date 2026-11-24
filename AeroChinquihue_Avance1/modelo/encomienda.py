from dataclasses import dataclass
from modelo.destino import destino

@dataclass
class encomienda:
    """Paquete entregado en La Paloma para envío a un destino."""
    codigo: str
    remitente: str
    destinatario: str
    destino: destino
    peso_kg: float
    precio: int
    fecha_entrega: str = "Por confirmar"
