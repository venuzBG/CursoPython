# Ejercicio 1: Sumar la serie finita Σx_i en orden inverso

def suma_inversa(x):
    """
    Suma los elementos del vector x en orden inverso.
    """
    S = 0
    for i in range(len(x) - 1, -1, -1):
        S += x[i]
    return S

# Ejemplo
x = [1, 2, 3, 4, 5]
print("Suma inversa =", suma_inversa(x))