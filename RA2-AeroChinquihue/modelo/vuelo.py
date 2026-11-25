from dataclasses import dataclass
from modelo.avion import avion
from modelo.destino import destino

@dataclass
class vuelo:
    """vuelo programado desde el aerodromo La Paloma hacia un destino"""
    codigo: str
    destino: destino
    fecha: str
    horario: str
    avion: avion
    asientos_reservados: list[str]

    def asientos_disponibles(self):
        return [asiento for asiento in self.avion.asientos
                if asiento not in self.asientos_reservados]

    def tiene_disponibilidad(self):
        return len(self.asientos_disponibles()) > 0

    def reservar_asiento(self, asiento: str):
        if asiento not in self.avion.asientos:
            raise ValueError(f"El asiento {asiento} no existe en este avión.")
        if asiento in self.asientos_reservados:
            raise ValueError(f"el asiento {asiento} ya está reservado.")
        self.asientos_reservados.append(asiento)
