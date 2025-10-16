# reto de sistema de verificacion

Usuario = 'Sebas'
Contrasena = '1234'

ingresar_usurio = input('Ingrese su usuario: ')
ingresar_contrasena = input('Ingrese su contrasena: ')

# Una forma de verificar si el usuario y contrasena son correctos es con el operador logico and
# verificacion_usuario = ingresar_usurio.strip() == Usuario
# verificacion_contrasena = ingresar_contrasena.strip() == Contrasena 

# confirmacion = verificacion_usuario and verificacion_contrasena

son_datos_correctos = ((ingresar_usurio.strip() == Usuario) 
                      and (ingresar_contrasena.strip() == Contrasena))

print(f'El usuario es correcto: {son_datos_correctos}')

