from modelo.avion import avion
from modelo.destino import destino
from modelo.vuelo import vuelo

class controlador_aerolinea:
    """Coordina los datos iniciales y operaciones básicas del sistema."""

    def cargar_destinos(self):
        tarifas = [
            ("Cochamó", 20000, 5000),
            ("Puelo Bajo", 20000, 5000),
            ("Contao", 20000, 5000),
            ("Río Negro", 25000, 6000),
            ("Pupelde", 25000, 6000),
            ("Chepu", 30000, 8000),
            ("Ayacara", 30000, 8000),
            ("Pillán", 40000, 12000),
            ("Reñihue", 40000, 12000),
            ("Isla Quenac", 40000, 12000),
            ("Palqui", 40000, 12000),
            ("Chaitén", 50000, 15000),
            ("Santa Bárbara", 50000, 15000),
        ]
        return {nombre: destino(nombre, pasaje, encomienda)
                for nombre, pasaje, encomienda in tarifas}

    def cargar_aviones(self):
        # Capacidades transcritas del enunciado del proyecto.
        return [
            avion("CESSNA 310", 5, 910),
            avion("CESSNA 208 CARAVAN", 9, 1315),
            avion("LET 410 UVP-E20", 19, 1800),
        ]

    def cargar_vuelos_demo(self, destinos, aviones):
        """Datos de demostración para poblar la aplicación; no son horarios reales."""
        destinos_demo = ["Cochamó", "Puelo Bajo", "Contao", "Río Negro",
                         "Pupelde", "Chepu", "Ayacara", "Pillán",
                         "Reñihue", "Isla Quenac", "Palqui", "Chaitén",
                         "Santa Bárbara"]
        vuelos = []
        for i, nombre in enumerate(destinos_demo, start=1):
            avion = aviones[(i - 1) % len(aviones)]
            vuelos.append(vuelo(
                codigo=f"ac-{i:03d}",
                destino=destinos[nombre],
                fecha="2026-11-25",
                horario=f"{8 + ((i - 1) % 8):02d}:00",
                avion=avion,
                asientos_reservados=[]
            ))
        return vuelos
