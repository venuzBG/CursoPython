# Variables en python

Cuando nosotros creamos una varibale y le asignamos un valor. estamos reservando un espacio de memoria en la ram, entonces la direccion de memoria estara en Hexadecimal y empezara 0x333, "0x" nos dice q esta en hexadecima. Cuando cambiamos el valor de la variable no cambia la direccion d ememoria solo se sobreescribe del valor anterior y sigue teniendo la misma
direccion de memoria.

## Unidad 1

### Variables

1. Al crear una variable esta en memoria y le valor es un objeto, entonces cuando sobreescribre no es que borra el nuevo valor sino que se crea un nuevo
objeto y ahora apunta a ese nuevo valor.

2. si quieres que un valor en python sea un numero que no lo vas a usar para sumar,etc. Sino que funcione com string lo pones entre comillas.

### Convecciones y buenas practicas para las variables

1. Snake case: Que significa que los nombres esten en minuscula y que esten separados por un guion bajo y evitar empezar con digitos.

2. Los nombres deben ser descriptivos no usar solo una letra sino un nombre

3. Evitar nombres de un solo caracter.

### Tipos de datos

Python es dinamico por lo que no necesitamos indoicar que tipo de variables son.

1. Numero int: Numeros enteros.
2. Numero con punto flñotante(float): Numeros con coma.
3. Cadena de texto: Cadena de letras o caracteres.
4. Booleanos: Almacenan un valor logico, verdadero o falso, y lo usaremos para
controlar el flujo del programa
5. none: este es un tipo especial de python que representa ausencia de valor.

### Constantes

Python es diferentes que otros lengajes de programacion debido a que no tiene una especificacion para definir una contante, por lo que para una buena practica de programacion vamos a usar un convencion que es poner la variable en cuestion en mayusculas y con esto entender que esa variable no debe ser modificada.

## Unidad 2

### Cadenas

La cadena o string es el tipo de dato que se usa para almacenar una secuencia de caracteres, se cierran en comillas dobles o simples. Los caracteres en cuestion puden ser tambien numeros o espacios.

Ejemplo:

``` Python
    #Numero de cadenas 
    cadena1 = "Hola mundo"

    #Cadena con numeros 
    cadena 2 = "123 456"
```

### Detalle de una cadena

Los caracteres de una cadena estan indexados de manera secuencial. Por lo tanto, podemos acceder cada caracter indicando el indice del caracter que queremos recuperar.

Ejemplo:

|   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|  "h"  |  "o"  |  "l"  |  "a"  |  ""   |  "m"  |  "u"  |  "n"  |  "d"  |  "o"  |

Para calcular el inidce es el numero de caracteres y espacio(n) menos 1: n-1

### Imnutabilidad de una cadena

Al crear una nueva cadena los caracteres dentro de ella no puden ser modificados. Si queremos modificar una cadena, entonces tendremos que crear una nueva cadena.

### Caracteres Especiales

Se pueden incluir caracteres especiales, como una diagonal invertida "\".

- Nueva linea: "\n" Insterta un salto de linea.
- Tabulacion: "\t" Inserta un tabulador horizontal, para alinear texto.
- Comilla simple: "\`" Permite incluir comillas simples en una cadena delimitada por comillas simples.
- comilla doble: "\``" Permite incluir comillas dobles en una cadena delimitada por comillas dobles.
- Barra invertidad: "\\" Permite incluir una barra invertida en la cadena.

Existen mas pero estos son los escenciales.

### Concatenacion de cadenas

Es una operacion que permite combinar dos o mas cadenas para formar una cadena nueva, en python hay varias formas.

- Uso de operador "+": Es el mas directo para concatenar cadenas.
- Uso de la funcion join: Nos permite unir cuantas cadenas nosotros necesitemos.
ej:
'''Python
    " ".join(["cadena1","cadena2","cadena3"]) #"" o " " el espacio entre cadenas.
'''

### Formateo de Cadenas

Python ofrece varias formas de formatear cadenas, que incluyen la capacidad de concatenar texto, variables e incluso dar otro tipo de formate, como por ejemplo indicar el numero de decimales a utilizar en el formato.

- f-string(python3.6+): esta es la opcion mas recomendada, por ser la mas sencilla, rapida y legible.

'''Python
    resultado = f' Hola {variable}.'
'''

- Metodo format: Es muy versatil y podertoso. Permite construir cadenas muy complejas.

'''Python
    resultado = 'Hola {}'.format(variable)
'''

### Metodos de Cadenas

Las cadenas en python vienen con una serie de metodos utiles que facilitan su manipulacion.

- upper(): Cambia las letras a mayusculas.
- lower(): Cambia las letras a minusculas.
- strpi(): Elimina los espacios, al inicio y al final de una cadena.

### Obtener el largo de una cadena

Es una funcion que contiene python, llamada len(). La funcion len funciona para varios tipos de datos.Cuando se calcula el largo de una cadena se incluye o se toma en cuenta todos los caracteres de una cadena hasta los espacion en blanco, caracteres esceciales, etc.

'''Python
    cadena1 = 'Hola, mundo!'
    longitud = len(cadena1) #Devuelve largo de 12
'''

### Subcadenas en python

La subcadena es una parte de una cadena principal, y hay varias maneras de extraer subcadenas en python. Podemos extraer, reemplazar, entre otras operaciones.

- Extraccion de cadenas:(Slicing): El slicing o segmentacion permite indicar el indice del inicio y el inidce final(sin incluir este ultimo caracter)

'''Python
    subcadena = cadena [inicio:fin]
'''

- Buscar subcadenas (find): El metodo devuelve el indice de la primera aparicion de la subcadena, pero si no encuentra la subcadena, devuelve -1.

'''Python
    cadenas = 'Hola Mundo"
    posicion = cadena.find("Mundo)
    print(posicion) #imprime 5
'''

- Reemplazar subcadenas(replace): El metodo reemplaza una subcadena por otra dentro de una cadena principal

'''Python
    cadenas = 'Hola Mundo"
    nueva_cadena = cadena.replace('Mundo','a todos')
    print(nueva_cadena) # 'Hola a todos'
'''

- Extraer subcadenas por separadores(split): L afuncion split permite dividir una cadena en una lista de subcadenas basadas en un caracter separador.

'''Python
    datos = 'Juan, 30, Mexico"
    lista = datos.split(',')
    print(lista) # ['Juan','30','Mexico']
'''
