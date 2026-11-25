from dataclasses import dataclass, field

@dataclass
class avion:
    """Representa un avion disponible."""
    modelo: str
    capacidad_pasajeros: int
    capacidad_carga_kg: float
    asientos: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.asientos:
            self.asientos = [f"{fila}{letra}" for fila in range(1, self.capacidad_pasajeros + 1)
                             for letra in ("a",)]
        if self.capacidad_pasajeros <= 0 or self.capacidad_carga_kg <= 0:
            raise ValueError("las capacidades del avion deben ser mayores que cero.")

    def cantidad_asientos(self):
        return len(self.asientos)
