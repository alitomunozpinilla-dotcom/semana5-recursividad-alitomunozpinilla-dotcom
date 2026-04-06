"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    Resultado = 1
    for i in range(exponente):
        Resultado *= base
    return Resultado
print(potencia_ciclo(2, 5))

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia_recursiva(base, exponente - 1)
print(potencia_recursiva(2, 5))
