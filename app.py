from auxiliares.menu import menu_superior
from presentacion.cliente_presentacion import menu_clientes
from presentacion.mesa_presentacion import menu_mesas
from presentacion.reserva_presentacion import menu_reservas
from presentacion.restaurante_presentacion import menu_restaurantes


def main():
    while True:
        print("\n==========================================")
        print(" SISTEMA DE RESERVAS RESTAURANTE POO ")
        print("==========================================")
        for clave, texto in menu_superior.items():
            print(f"[{clave}] {texto}")

        opcion = input("\nIngrese una opción: ").strip()

        match opcion:
            case "1":
                menu_restaurantes()
            case "2":
                menu_reservas()
            case "3":
                menu_mesas()
            case "4":
                menu_clientes()
            case "0":
                print("\n¡Gracias por utilizar el sistema!")
                break
            case _:
                print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()