from controller.aerolinea_controller import AerolineaController
from view.consola_view import ConsolaView

def main():
    controlador = AerolineaController()
    vista = ConsolaView()

    destinos = controlador.cargar_destinos()
    aviones = controlador.cargar_aviones()
    vuelos = controlador.cargar_vuelos_demo(destinos, aviones)

    vista.mostrar_destinos(destinos)
    vista.mostrar_vuelos(vuelos)

    print("\nSistema AeroChinquihue: carga inicial completada.")

if __name__ == "__main__":
    main()
