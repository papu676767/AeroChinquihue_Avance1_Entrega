from dataclasses import dataclass

@dataclass
class pasajero:
    """cliente que solicita un pasaje"""
    rut: str
    nombre: str
    telefono: str
    vuelos_realizados: int = 0

    def tiene_descuento_frecuente(self):
        return self.vuelos_realizados > 10
