from dataclasses import dataclass

@dataclass
class pago:
    """Registro del pago asociado a una venta de servicio."""
    codigo: str
    monto: int
    medio_pago: str
    estado: str = "Registrado"
