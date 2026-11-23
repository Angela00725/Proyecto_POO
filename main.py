from presentacion.presentacion_login import iniciar_sesion
from presentacion.menu import menu_principal


def main():
    while True:
        usuario = iniciar_sesion()
        if usuario is not None:
            menu_principal(usuario)
            break


if __name__ == "__main__":
    main()
