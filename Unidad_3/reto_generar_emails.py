# Reto generar emails

nombre = input("Ingrese sus nombres: \n")
apellido = input("Ingrese sus apellidos: \n")
empresa = input("Ingrese el nombre de la empresa: \n")
dominio = "com.ec"

nombre_email = nombre.lower().strip().replace(" ", ".")
apellido_email = apellido.lower().strip().replace(" ", ".")
empresa_email = empresa.lower().strip().replace(" ", "")
email = f"{nombre_email}.{apellido_email}@{empresa_email}.{dominio}"

print(f"Su email generado es: \n {email}")