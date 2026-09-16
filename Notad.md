# Variables en python

Cuando nosotros creamos una varibale y le asignamos un valor. estamos reservando un espacio de memoria en la ram, entonces la direccion de memoria estara en Hexadecimal y empezara 0x333, "0x" nos dice q esta en hexadecima. Cuando cambiamos el valor de la variable no cambia la direccion d ememoria solo se sobreescribe del valor anterior y sigue teniendo la misma
direccion de memoria.

## Seccion 3

### Variables

1. Al crear una variable esta en memoria y el valor es un objeto, entonces cuando sobreescribre no es que borra el nuevo valor sino que se crea un nuevo
objeto y ahora apunta a ese nuevo valor.

2. si quieres que un valor en python sea un numero que no lo vas a usar para sumar,etc. Sino que funcione com string lo pones entre comillas.

### Convecciones y buenas practicas para las variables

1. Snake case: Que significa que los nombres esten en minuscula y que esten separados por un guion bajo y evitar empezar con digitos.

2. Los nombres deben ser descriptivos no usar solo una letra sino un nombre

### Tipos de datos

Python es dinamico por lo que no necesitamos indicar que tipo de variables son.

1. Numero int: Numeros enteros.
2. Numero con punto flotante(float): Numeros con coma.
3. Cadena de texto: Cadena de letras o caracteres.
4. Booleanos: Almacenan un valor logico, verdadero o falso, y lo usaremos para
controlar el flujo del programa
5. none: este es un tipo especial de python que representa ausencia de valor.

### Constantes

Python es diferentes que otros lengajes de programacion debido a que no tiene una especificacion para definir una contante, por lo que para una buena practica de programacion vamos a usar una convencion que es poner la variable en cuestion en mayusculas y con esto entender que esa variable no debe ser modificada.

## Seccion 4

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

``` Python
    " ".join(["cadena1","cadena2","cadena3"]) #"" o " " el espacio entre cadenas.
```

### Formateo de Cadenas

Python ofrece varias formas de formatear cadenas, que incluyen la capacidad de concatenar texto, variables e incluso dar otro tipo de formate, como por ejemplo indicar el numero de decimales a utilizar en el formato.

- f-string(python3.6+): esta es la opcion mas recomendada, por ser la mas sencilla, rapida y legible.

```  Python
    resultado = f' Hola {variable}.'
```

- Metodo format: Es muy versatil y podertoso. Permite construir cadenas muy complejas.

``` Python
    resultado = 'Hola {}'.format(variable)
```

### Metodos de Cadenas

Las cadenas en python vienen con una serie de metodos utiles que facilitan su manipulacion.

- upper(): Cambia las letras a mayusculas.
- lower(): Cambia las letras a minusculas.
- strip(): Elimina los espacios, al inicio y al final de una cadena.

### Obtener el largo de una cadena

Es una funcion que contiene python, llamada len(). La funcion len funciona para varios tipos de datos.Cuando se calcula el largo de una cadena se incluye o se toma en cuenta todos los caracteres de una cadena hasta los espacion en blanco, caracteres esceciales, etc.

``` Python
    cadena1 = 'Hola, mundo!'
    longitud = len(cadena1) #Devuelve largo de 12
```

### Subcadenas en python

La subcadena es una parte de una cadena principal, y hay varias maneras de extraer subcadenas en python. Podemos extraer, reemplazar, entre otras operaciones.

- Extraccion de cadenas:(Slicing): El slicing o segmentacion permite indicar el indice del inicio y el inidce final(sin incluir este ultimo caracter)

``` Python
    subcadena = cadena [inicio:fin]
```

- Buscar subcadenas (find): El metodo devuelve el indice de la primera aparicion de la subcadena, pero si no encuentra la subcadena, devuelve -1.

``` Python
    cadenas = 'Hola Mundo"
    posicion = cadena.find("Mundo")
    print(posicion) #imprime 5
```

- Reemplazar subcadenas(replace): El metodo reemplaza una subcadena por otra dentro de una cadena principal

``` Python
    cadenas = 'Hola Mundo"
    nueva_cadena = cadena.replace('Mundo','a todos')
    print(nueva_cadena) # 'Hola a todos'
```

- Extraer subcadenas por separadores(split): L afuncion split permite dividir una cadena en una lista de subcadenas basadas en un caracter separador.

``` Python
    datos = 'Juan, 30, Mexico"
    lista = datos.split(',')
    print(lista) # ['Juan','30','Mexico']
```

## Seccion 5

### Conversion de tipo de datos

Otra forma de llamarlo es casting, es una tecnica para manipular datos que no estan en el tipo requerido. Podemos hacer conversiones desde y hacia tipos de datos.

- Convertir a entero: funcion int()
- Convertir a flotante: funcion float()
- Convertir a cadena: funcion str()
- Convertir a booleano: funcion bool()

### Entrada de datos por consola

Entrada de datos se realiza usando la funcion imput. Esta funcion pausa el programa y espera a que el usuario ponga algun texto. Una vez que el usuario ponga enter, el texto introducido se vuelve como una cadena (str).

#### Caracteristicas de la funcion imput

- Interactividad: Permite a los usuarios de nuestro programa proporcionar valores dinamicos, en lugar de usar valores estaticos.
- sencillez: Es sencilla de usar y solo necesita indicar la cadena o mensaje a mostrar al usuario, para que entienda lo que se esta solicitando.
- Tipo de dato: Siempre devuelve una cadena, si requiere otro tipo de dato hay q convertirlo.

### Generar valores aleatorios

La funcion randint(), que es parte del modulo random, nos permite generar numeros aleatorios. randiant(a,b), devuelve los valores entre a y b, incluyendo los valores a y b. Es importante importarr el modulo random antes de usar la funcion. Para importar el modulo usamos:

``` Python
    import random
```

## Seccion 6

### Operadores en python

Son simbolos especiales que estan diseñados para hacer una operacion en especifico. Tenemos varios tipos:

- Operadores aritmeticos: Permiten realizar calculos matematicos basicos.
- Operadores de asignacion: Se utilizan para asignar valores a variables.
- Operadores de comparacion: Se utilizan para comparar un valor con otro.
- Operadores Logicos: Se utiliza para expresiones condicionales o logicos.
- Operadores con identidad: Se utilizan para comparar si dos variables son el mismo objeto.
- Operadores de membresia: Se presenta para probar si una secuencia(ej:subcadena) se presenta en un objeto.

#### Operadores aritmeticos

Para realizar calculos matematicos:

- suma(+)
- resta(-)
- multiplicacion(*)
- division(/)
- division entera(//): Divide el primer operando con el segundo. El resultado te dara solo la parte entera.
- modulo(%): Residuo d ela division
- esponente(**): eleva el primer operador a la segund potencia.

#### Operadores de asignacion

El operador de asignación se usa para asignar un valor a una variable, y se usa el caracter (=) para ello.

Ejemplo:

``` Python
    variable = valor
    numero = 10
```

Python tambien tiene lo que es la asignacion multiple lo que permite asignar valores a varias variables en una misma linea de codigo.

Ejemplo:

``` Python
    # Sintaxis de asigancion multiple
    variable 1, variable 2 = valor 1, valor 2
    a,b,c = 1,"carro", 5
```

Tambien hay asignacion en cadenado en python. Esto permite asgnar el mismo valor a diferentes variables en una
linea de codigo.

Ejemplo:

``` Python
    # Sintaxis de asigancion encadenada
    variable1 + variable 2 + .... =valor
    # Ejemplo de inicializar contadores
    contador1 + contador2 = 0
```

Otra caracteristica es que podemos pedirle al usuario multiples valores de entrada, usamos la funcion
split(), para que el programa entienda que un espacio es el separdar de una a otra variable.

Ejemplo:

``` Python
    # Sintaxis de pedir multiples valores de entrada, si dejmaos el split entiende que es un espacio
    nombre, apellido = input('Ingrese su nombre y apellido: ').split()
    # Tambien podemos poner dentro de la funcion split cual queremos q sea nuestro separdaor
    nombre, apellido = input('Ingrese su nombre y apellido: ').split(",")
```

### Operadores de asignacion compuesto

Los operadores de asignacion compuesto combian una operacion aritmetica con una asiganacion, haciendo las
operaciones mas conscisas.
Los operadores pueden ser +=, -=, *=, /=, etc.

Ejemplo:

``` Python
    # Sintaxis operador asignacion compuesto
    variable Operador= Valor
    # Ejemplo 
    contador = 0
    contador += 1 # contador = contador + 1
```

### Operador de Comparacion

Los operadores de comparacion se utiliza para comparar dos valores. El valor siempre es un valor booleano
'true' o 'false', dependiendo si la condicion se cumple o no.

- Operador de igualdad

``` Python
    # Sintaxis operador de igualdad ==
    a == b
    # Ejemplo 
    print(5 == 5) #Imprime true
    print(5 == 3) #Imprime false
```

- Operador de desigualdad

``` Python
    # Sintaxis operador de igualdad !=
    a != b
    # Ejemplo 
    print(5 != 6) #Imprime true
    print(5 != 5) #Imprime false
```

- Operador menor que(<)

``` Python
    print(5 < 6) #Imprime true
    print(5 < 5) #Imprime false
```

- Operador menor o igual que(<=)

``` Python
    print(5 <= 6) #Imprime true
    print(5 <= 4) #Imprime false
```

- Operador mayor que(>)

``` Python
    print(5 > 3) #Imprime true
    print(5 > 7) #Imprime false
```

- Operador mayor o igual que(>=)

``` Python
    print(5 >= 3) #Imprime true
    print(5 >= 7) #Imprime false
```

### Operadores logicos

Se utilizan para realizar operaciones logicos

- Operador Logico and (y): Devuelve True si ambos operadores son verdaderos, caso contrario siempre sera falso.

``` Python
    exp1 = False 
    exp2 = True
    print(exp1 and exp2) #False
```

- Operador logico or (o): Devuelve True si cualquiera de los operandos son verdaderos, sino tiene niguna variable verdadero siempre sera falso.

``` Python
    exp1 = False 
    exp2 = True
    print(exp1 or exp2) #True
```

- Operador logico not (no): Inverte el valor del operado. Es un operador unario.

``` Python
    exp1 = False 
    print(not exp1) #True
```

### Precedencia de Operadores

Determina el orden en que se evaluan las operaciones.

Python aplica las siguiente tabla para asegurar que algunos operadores tengan prioridad sobre otros

1. Operador de parentesis ()
2. Exponente **
3. Unarios +x(positivo), -x(negativo)
4. Multiplicacion, division, modulo *, /, //, %
5. Suma y Resta +. -
6. Comparacion ==, !=, <, <=, >, >=
7. Operadores logicos not, and y or
8. Operadores de asignacion =, +=, -=, /=, %=, //=, **=

``` Python
    resultado = 5 + 3 * 2 ** 2 # 17
    resultado = (5 + 3) * 2 ** 2 # 32
```

## Seccion 7

### Sentencias de decisión

Nos permite controlar el flujo de ejecucion del programa

Las estructuras pueden ser: if, else y elif

- La sentecia if permite ejecutar un bloque de codigo si la condicion a evaluar es verdadera.

Ejemplo:

``` Python
    # Sintaxis sentencia if
    if condition:
        #Bloque de codigo que se
        #ejecuta si la condicion es TRUE
        #son importantes la tabulacion

    # Ejemplo
    edad = 30
    if edad > = 30
        print("Eres mayor de edad")
```

### Diagrama de Flujo

Un diagram de flujo es una representación gráfica de los pasos a ejecutar para lograr un resultado especifico.

Se utilizan simbolos estandarizados para representar distintos tipos de acciones.

1. Circulo o Ovalo: Representa el inicio o fin de un proceso
2. Rectangulo: Muestra instrucciones o acciones a ejecutar
3. Rombo o diamante: Indica decisciones, con multiples flujos dependiendo si la respuesta es verdadera o falsa
4. Flechas: Dirigen el flujo del proceso, mostrando la direccion en que se mueven la secuencia de acciones

Ejercicio:

Dado el siguiente código, vamos a creae su diagrama de flujo equivalente:

- Código

``` Python
    edad = 30
    if edad > = 30
        print("Eres mayor de edad")
```

- Diarama

![alt text](image.png)

### Sentencia else

La sentencia else se usa para ejecutar un bloque de codigo cuando la sentencia if es falsa

``` Python
    # Sintaxis sentencia else-if
    if condition:
        #Bloque de codigo
        #si la condicion es verdadera
    else:
        #Bloque de codigo
        #si la condicion es falsa
    #Ejemplo
    edad = 30
    if edad > = 30
        print("Eres mayor de edad")
    else:
        print("Eres menos de edad")
```

- Diagrama
![alt text](image-1.png)

### Sentecia if elif else

La sentencia elif es una abreviatura de else-if, y se utiliza cuando necesitemos verificar multiples condiciones, una tras otra. Se pude crear cuantas elif necesitemos.

``` Python
    # Sintaxis sentencia else-if
    if condition1:
        #Bloque de codigo
    elif condition2:
        #Bloque de codigo
    else:
        #Bloque de codigo
    #Ejemplo
    edad = 30
    if edad > = 18
        print("Eres mayor de edad")
    elif 13 <= edad < 18
        print('Eres un adolescente')
    else:
        print("Eres un niñ@")
```

### Operador ternario

Es una funcion compacta de agregar una condicion y el objetivo es asignar un valor a una variable dependiendo
del valor de la condicion.

``` Python
    # Sintaxis operador ternario
    resultado = valor_si_verdadero if condition else valor_si_falso
    # Ejemplo
    edad = 18
    es_adulto = 'Si' if edad >= 18 else 'No'
    print(es_adulto)
    
```

## Seccion 8

### Ciclos

Son estructuras de control que va a repetir una serie de instrucciones hasta que se cumpla una condicion
especifica. Solo hay dos estrcuturas de ciclos For y While.

#### Ciclo While

Repite una serie de intrucciones mientras la condicion sea verdadera.

``` Python
    # Sintaxis de bucle while
    while condicion:
        # Bloque de codigo a ejecutar

    # Ejemplo de imprimir del 1 al 3
    contador = 1
    while contador <= 3:
        print(contador)
        contador +=1
```

### Ciclo For

En el ciclo for itera o recorre una secuencia de valores, por ejemplo los caracteres de una cadena, una lista, etc.
Y ejecuta un bloque de codigo por cada elemento de la secuencia.

``` Python
    # Sintaxis de bucle while
    for variable in secuencia:
        # Bloque de codigo a ejecutar

    # Ejemplo de imprimir del 1 al 3
    secuencia = "Hola Mundo"
    for letra, in cadena:
        print(letra, end = " ")
```

### Funcion de range en python

Es una funcion incorporada que genera una funcion de números. Es utilizada muy comunmente para iterar numeros
con el ciclo for. Es importante aclarar que si no se pone un valor inicial empezara desde 0 por defecto. El incremento
en cambio tiene por defecto 1.

``` Python
    # Sintaxis de funcion range
    # Inicio - valor inicial (opcional)
    # Fin - valoe final, sin uncluirlo (eso significa que si dices que el fin es 5 va del 0 al 4, osea menor al fin)
    # Incremento - diferencia entre cada numero(opcional)
    range(inicio, fin, incremento)
```

``` Python
    # Imprimir los numeros del 0 al 4
    for i in range(5):
        print(i)
    
    # usar range para imprimir del 0 al 9
    # que vaya incrementando en 2
    for i in range(0, 10, 2):
        print(i)
```

### Palabra break y continue

Break sirve para salir de bucle inmediatamente, Continue en cambio sirve para que pase a la siguiente iteracion desde ese punto.

Ejemplo:

``` Python
    # Ejemplo break
    print("Palabra break: ")

    for numero in range(1,10):
        if numero % 2 == 0:
            print(numero)
            break  # Salimos del ciclo inmediatamente

    # Ejemplo de continue

    print("\n\nPalabra continue: ")
    for numero in range(1,10):
        if numero % 2 == 1:
            continue # si llega a esta linea va a la siguiente iteracion desde ese punto
        print(numero)
```

## Seccion 9

### Coleccion en python

Una coleccion es un conjunto de datos. En python tenemos varios tiposque podemos utilizar con el objetivo de
almacenar, organizar y manipular multiples conjunto de datos.
Los tipos de datos que vamos a estudiar son:
    - listas
    - tuplas
    - set(Conjunto)
    - Diccionarios
Estos son los mas comunes y mas usados.

#### Listas en python

Las listas son colecciones ordenadas y mutables(se puede modificar) de elementos que pueden ser diferentes tipos.
Las listas son dinamicas, lo que significa que pueden cambiar de tamaño, podemos añadir, modificar o elminar elementos.
La lista va a tener un indice que empieza desde el 0.

``` Python
    # Sintaxis de una lista
    lista = [elemento1, elemto2, etc]

    # Ejemplos de listas
    numeros = [1,2,3,5]
    frutas = ["Manzana", "Peras"]
    mixta = ["Dado", 12, 13, [2,4]] #una lista puede contener a otra lista

```

### Formas de modificar elementos de una lista

#### 1. Modificar un elemento por su indice

Se asigna un nuevo valor al indice que se desea cambiar. El indice debe existir; de lo contrario, Python genera un error `IndexError`.

```python
frutas[1] = "naranja"
print(frutas)  # ["manzana", "naranja", "uva"]
```

Tambien se puede usar un indice negativo:

```python
    frutas[-1] = "mango"
```

#### 2. Agregar un elemento al final con `append()`

`append()` agrega un solo elemento al final de la lista y modifica la lista original.

```python
    frutas.append("melon")
    print(frutas)
```

#### 3. Insertar un elemento en una posicion con `insert()`

`insert(indice, elemento)` agrega un elemento en la posicion indicada. Los elementos que estaban desde esa posicion se desplazan a la derecha.

```python
frutas.insert(1, "kiwi")
print(frutas)
```

#### 4. Reemplazar varios elementos con cortes

La asignacion mediante un corte permite sustituir un grupo de elementos. El indice final no se incluye.

```python
numeros = [1, 2, 3, 4, 5]
numeros[1:3] = [20, 30]
print(numeros)  # [1, 20, 30, 4, 5]
```

El reemplazo puede tener una cantidad diferente de elementos, por lo que tambien permite eliminar o insertar varios valores:

```python
    numeros = [1, 2, 3, 4, 5]
    numeros[1:3] = [200]
    print(numeros)  # [1, 200, 4, 5]
```

#### 5. Eliminar por valor con `remove()`

`remove(valor)` elimina la primera coincidencia del valor indicado. Si el valor no existe, Python genera un error `ValueError`.

```python
frutas.remove("kiwi")
```

#### 6. Eliminar por indice con `pop()`

`pop(indice)` hace dos cosas: elimina el elemento de la posicion indicada y devuelve ese elemento como resultado. "Devolver" significa que podemos guardar el elemento eliminado en una variable y utilizarlo despues. Si no se proporciona un indice, elimina y devuelve el ultimo elemento.

```python
frutas = ["manzana", "pera", "uva"]
fruta_eliminada = frutas.pop(1)

print(fruta_eliminada)  # pera
print(frutas)           # ["manzana", "uva"]
```

Tambien podemos usar `pop()` sin indice para quitar el ultimo elemento:

```python
ultima_fruta = frutas.pop()
print(ultima_fruta)  # uva
```

#### 7. Eliminar con `del`

`del` elimina un elemento por indice o un grupo de elementos mediante un corte, pero no devuelve el valor eliminado. Por eso se usa cuando solo necesitamos quitar el elemento y no necesitamos guardarlo.

```python
frutas = ["manzana", "pera", "uva"]
del frutas[0]     # elimina el primer elemento
print(frutas)     # ["pera", "uva"]
```

La diferencia principal se puede resumir asi:

```python
frutas = ["manzana", "pera", "uva"]

fruta = frutas.pop(1)  # elimina "pera" y permite guardarla en una variable
del frutas[0]          # elimina "manzana", pero no podemos recuperar su valor
```

`pop()` es util cuando necesitamos trabajar con el elemento eliminado. `del` es util cuando solo queremos eliminarlo. `del` tambien permite eliminar varios elementos usando un corte:

```python
del frutas[0:2]  # elimina los indices 0 y 1
```

#### 8. Vaciar toda la lista con `clear()`

`clear()` elimina todos los elementos, pero conserva la lista para poder usarla nuevamente.

```python
frutas.clear()
print(frutas)  # []
```

### Resumen rapido

| Operacion | Uso | Resultado |
| ----------- | ----- | ----------- |
| Cambiar un valor | `lista[indice] = valor` | Reemplaza un elemento |
| Agregar al final | `lista.append(valor)` | Anade un elemento |
| Insertar | `lista.insert(indice, valor)` | Agrega y desplaza elementos |
| Reemplazar varios | `lista[inicio:fin] = valores` | Sustituye un grupo |
| Eliminar por valor | `lista.remove(valor)` | Elimina la primera coincidencia |
| Eliminar por indice | `lista.pop(indice)` | Elimina y devuelve un elemento |
| Eliminar con indice o corte | `del lista[indice]` | Elimina sin devolverlo |
| Vaciar | `lista.clear()` | Deja la lista vacia |

1. Evitar nombres de un solo caracter.

### Tuplas

Las tuplas son similares a las listas, con la diferencia que los elementos que contendra no se podran modificar, eliminar
ni aumentar despues de haberla creada. Por esta razon solo se las crea para colecciones de datos que no pueden cambiar con
el tiempo.

```python
    # Sintaxis
    mytupla = (elemento1, elemento2, elemento3)
    mytupla2 = elemento1, elemento2, elemento3

    # Ejemplos
    tupla_numeros = (1, 2, 3, 4)
    tupla_mixta = ("manzana", 10, 3.14, [1,3,4])
    tupla_sin_parentesis = "Juan", "Carla"
    tupla_un_elemento = 10, # Es necesario la coma si es un solo elemento sino se interpretara como un numero 
```

### Desempaquetado de tuplas

El desempaquetado permite asignar cada elemento de una tupla a una variable diferente en una sola linea.

```python
datos = ("Ana", 25)
nombre, edad = datos

print(nombre)  # Ana
print(edad)    # 25
```

### Sets en Python

Un set es una coleccion de datos que no permite elementos repetidos y no esta ordenada. Esto significa que sus elementos no tienen una posicion fija y Python no garantiza el orden en que se mostraran.

```python
    #Sintaxis
    mi_set = {elemento 1, elemento 2, elemento 4}
```

```python
    set_a = {1,2,3,4}
    set_b = {3, "Juan", True, 6.5}
    frutas = {"manzana", "pera", "manzana"}
    print(frutas)  # {'manzana', 'pera'}
```

Para comprobar si un elemento pertenece a un set usamos `in`:

```python
mi_set = {2, 4, 6, 8}
print(6 in mi_set)  # True
```

### Operaciones con sets

- **Union (`|`)**: combina los elementos de dos sets sin repetirlos.
- **Interseccion (`&`)**: obtiene los elementos que existen en ambos sets.
- **Diferencia (`-`)**: obtiene los elementos del primer set que no estan en el segundo.

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)  # {1, 2, 3, 4, 5}
print(set_a & set_b)  # {3}
print(set_a - set_b)  # {1, 2}
```

### Diccionarios en Python

Un diccionario es una coleccion de datos que guarda informacion en pares de **clave y valor**. La clave identifica el dato y debe ser unica. Desde la version 3.7 de python ya son ordenadas los diccionarios antes de esa version no lo era.

#### Sintaxis

```python
diccionario = {clave: valor, clave2: valor2}
```

#### Ejemplo

```python
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])  # Ana
```

#### Acceder a los elementos de un diccionario

Para obtener un valor de un diccionario se usa la clave entre corchetes.

```python
persona = {"nombre": "Ana", "edad": 25}

print(persona["nombre"])  # Ana
print(persona["edad"])    # 25
```

En este ejemplo, `"nombre"` y `"edad"` son las claves. Cuando escribimos `persona["nombre"]`, Python busca esa clave dentro del diccionario y devuelve su valor asociado. Si la clave no existe, Python lanza un error `KeyError`.

Otra forma de acceder a un valor es con `get()`, que es más seguro porque si la clave no existe, devuelve `None` en lugar de dar un error.

```python
persona = {"nombre": "Ana", "edad": 25}

print(persona.get("nombre"))  # Ana
print(persona.get("pais"))    # None
```

Esto es útil cuando no sabemos si una clave existe antes de usarla.

#### Modificar valores dentro de un diccionario

Los diccionarios son mutables, es decir, podemos cambiar sus valores después de crearlos.

```python
persona = {"nombre": "Ana", "edad": 25}

persona["edad"] = 30
print(persona)  # {'nombre': 'Ana', 'edad': 30}
```

Aquí estamos accediendo a la clave `"edad"` y le asignamos un nuevo valor. Esto cambia el contenido del diccionario sin necesidad de crear uno nuevo.

#### Agregar nuevos elementos

También podemos agregar pares clave-valor nuevos al diccionario.

```python
persona = {"nombre": "Ana", "edad": 25}

persona["pais"] = "Mexico"
print(persona)  # {'nombre': 'Ana', 'edad': 25, 'pais': 'Mexico'}
```

Cuando se usa una clave que todavía no existe, Python la crea automáticamente y le asigna el valor que se indica.

#### Eliminar elementos

Podemos eliminar elementos con `del` o con `pop()`.

```python
persona = {"nombre": "Ana", "edad": 25, "pais": "Mexico"}

del persona["pais"]
print(persona)  # {'nombre': 'Ana', 'edad': 25}

persona.pop("edad")
print(persona)  # {'nombre': 'Ana'}
```

- `del` elimina directamente la clave indicada.
- `pop()` elimina la clave y además devuelve el valor eliminado, por si queremos guardarlo en otra variable.

#### Recorrer un diccionario

Para leer todos los datos del diccionario, podemos iterar sobre sus claves, valores o ambos.

```python
persona = {"nombre": "Ana", "edad": 25, "pais": "Mexico"}

for clave, valor in persona.items():
    print(clave, valor)
```

La función `items()` devuelve cada par clave-valor, por lo que podemos acceder a ambos en cada iteración.

```python
for valor in persona.values():
    print(valor)
```

Con `values()` solo obtenemos los valores.

```python
for clave in persona.keys():
    print(clave)
```

Con `keys()` solo obtenemos las claves.

En resumen, acceder y modificar diccionarios consiste en usar las claves para leer o actualizar información, y cuando queremos agregar nuevos datos solo necesitamos asignar una nueva clave con su valor. Esto hace que los diccionarios sean muy útiles para manejar datos estructurados como información de personas, productos, usuarios o configuraciones.
