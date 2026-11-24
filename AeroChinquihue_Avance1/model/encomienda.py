from dataclasses import dataclass
from model.destino import Destino

@dataclass
class Encomienda:
    """Paquete entregado en La Paloma para envío a un destino."""
    codigo: str
    remitente: str
    destinatario: str
    destino: Destino
    peso_kg: float
    precio: int
    fecha_entrega: str = "Por confirmar"
