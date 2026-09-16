# Listas - Diccionarios

lista = [
        {
            "nombre":"Regina", 
            "apellido":"Flores", 
            "edad":21
        },
        
        {"nombre":"Alejandro", 
         "apellido":"Reyes", 
         "edad": 21
        }
]

print(lista)

# Como acceder a un diccionario desde una lista

print(f'''Detalle del primer elemnto de la lista: 
      Nombre : {lista[0].get('nombre')} 
      Apellido : {lista[0].get("apellido")}
      Edad : {lista[0].get('edad')}
      ''')

# Recorrer los elementos de la lista
print()

for contador, persona in enumerate(lista):
    print(f"{contador} - Persona : {persona}")
    print(f"Detalle: Nombre : {persona.get("nombre")}, Apellido : {persona.get("apellido")}, Edad : {persona.get("edad")}")

