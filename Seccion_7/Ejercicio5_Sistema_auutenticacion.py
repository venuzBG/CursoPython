# Sistema de autenticacion 

# Constantes de usuarios y contraseñas

USUARIO = "admin"
PASSWORD = "1234"

# Datos a ingresar

usuario_ingresado = input("Ingrese su usuario: ")
password_ingresado = input("Ingrese su contraseña: ")

# Función para autenticar al usuario

if usuario_ingresado == USUARIO and password_ingresado == PASSWORD:
    print("Autenticación exitosa. ¡Bienvenido!")
    
elif usuario_ingresado != USUARIO :
    print("Usuario incorrecto. Intente nuevamente.")
    
elif password_ingresado != PASSWORD:
    print("Contraseña incorrecta. Intente nuevamente.")
    
else:
    print("Usuario y contraseña incorrectos. Intente nuevamente.")
    
