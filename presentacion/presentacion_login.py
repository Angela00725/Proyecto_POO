from maskpass import askpass

from auxiliares.validaciones import validar_correo
from negocio.negocio_autenticacion import login_usuario


def iniciar_sesion():
    while True:
        correo = input("Correo: ").strip()
        correo_valido, resultado = validar_correo(correo)
        if not correo_valido:
            print(f"\n>> {resultado}")
            continue

        contrasena = askpass(prompt="Contraseña: ", mask="*")
        usuario, mensaje = login_usuario(resultado, contrasena)
        if usuario:
            print(f"\n>> {mensaje}")
            return usuario

        print(f"\n>> {mensaje}")