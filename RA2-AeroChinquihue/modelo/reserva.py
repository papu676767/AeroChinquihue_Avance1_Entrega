from dataclasses import dataclass
from modelo.pasajero import pasajero
from modelo.vuelo import vuelo

@dataclass
class reserva:
    """reserva de un asiento para un pasajero en un vuelo"""
    codigo: str
    pasajero: pasajero
    vuelo: vuelo
    asiento: str
    precio_final: int
    estado: str = "Pendiente"
