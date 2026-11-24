from dataclasses import dataclass
from model.pasajero import Pasajero
from model.vuelo import Vuelo

@dataclass
class Reserva:
    """Reserva de un asiento para un pasajero en un vuelo."""
    codigo: str
    pasajero: Pasajero
    vuelo: Vuelo
    asiento: str
    precio_final: int
    estado: str = "Pendiente"
