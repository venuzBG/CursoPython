print("Agenda de contactos")

agenda = {
    "Carlos" : {
        "telefono":"55667711",
        "email":"carlos@gmail.com",
        "direccion" : "Calle principal 123"
    },
    
    "Maria" : {
            "telefono":"99887733",
            "email":"maria@gmail.com",
            "direccion" : "Avenida Central 456"
    },

    "Pedro" : {
            "telefono":"55139078",
            "email":"pedro@gmail.com",
            "direccion" : "Plaza Mayor 789"
    }
}

print(agenda)

# Acceder a un contacto en especifico
print()
print(f'''Informacion del contacto de Maria:
      
      Telefono: {agenda["Maria"]["telefono"]}
      Email : {agenda.get("Maria").get("email")}
      Direccion : {agenda.get("Maria").get("direccion")}
      
      ''')

# Agregar un contacto

agenda["Ana"] = {
    "telefono" : "55678392",
    "email" : "ana@gmail.com",
    "direccion" : "AV. mariscal sucre"
}

print(agenda)

# Eliminar un contacto

agenda.pop("Pedro")

# del agenda(Pedro)
print(agenda)

# MMostrar los contactos de la agenda

print("\nContactos Agenda:")

for nombre, detalles in agenda.items():
    print(f'''Nombre : {nombre}
    Telefono : {detalles.get("telefono")}
    Email : {detalles.get("email")}
    ''')

