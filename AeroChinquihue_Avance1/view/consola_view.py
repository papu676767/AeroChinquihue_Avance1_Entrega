class ConsolaView:
    """Vista sencilla para mostrar los datos en consola."""

    def mostrar_destinos(self, destinos):
        print("\nDESTINOS Y TARIFAS")
        print("-" * 66)
        print(f"{'Destino':<20}{'Pasaje':>16}{'Encomienda/kg':>22}")
        for destino in destinos.values():
            print(f"{destino.nombre:<20}${destino.precio_pasaje:>14,}"
                  f"${destino.precio_encomienda_kg:>20,}")

    def mostrar_vuelos(self, vuelos):
        print("\nVUELOS DE DEMOSTRACIÓN")
        print("-" * 78)
        for vuelo in vuelos:
            print(f"{vuelo.codigo} | {vuelo.destino.nombre:<16} | "
                  f"{vuelo.fecha} {vuelo.horario} | {vuelo.avion.modelo} | "
                  f"Asientos libres: {len(vuelo.asientos_disponibles())}")
