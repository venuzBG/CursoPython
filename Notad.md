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

