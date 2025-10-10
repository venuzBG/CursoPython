# Crear un program para generar un email.

Nombre = "Sebastian Oña"
Empresa = "Global Mentoring"
Dominio = "COM.EC"

# Parte del nombre
nombre = Nombre.lower().replace(" ", ".")

# Parte de la empresa
empresa = Empresa.lower().replace(" ", "")

# Parte de la dominio
dominio = Dominio.lower()


# Parte final

print("*** Generador de Email ***")
print("Nombre: ", Nombre)
print("Nombre normalizado: ", nombre)
print("\nEmpresa: ", Empresa)
print("Empresa normalizada: ", empresa)
print("Dominio: ", Dominio)
print(f"Dominio normalizado: {empresa}.{dominio}")

print(f"\nEmail final generado: {nombre}@{empresa}.{dominio}")