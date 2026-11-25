from dataclasses import dataclass

@dataclass
class destino:
    """Destino al que vuela AeroChinquihue, con sus tarifas."""
    nombre: str
    precio_pasaje: int
    precio_encomienda_kg: int

    def calcular_precio_encomienda(self, peso_kg: float) -> int:
        if peso_kg <= 0:
            raise ValueError("El peso debe ser mayor que cero.")
        return round(self.precio_encomienda_kg * peso_kg)
