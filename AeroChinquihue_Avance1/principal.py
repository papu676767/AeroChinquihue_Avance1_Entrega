from controlador.controlador_aerolinea import controlador_aerolinea
from vista.vista_consola import vista_consola

def principal():
    controlador = controlador_aerolinea()
    vista = vista_consola()

    destinos = controlador.cargar_destinos()
    aviones = controlador.cargar_aviones()
    vuelos = controlador.cargar_vuelos_demo(destinos, aviones)

    vista.mostrar_destinos(destinos)
    vista.mostrar_vuelos(vuelos)

    print("\nSistema AeroChinquihue: carga inicial completada.")

if __name__ == "__main__":
    principal()
