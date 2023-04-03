from libreria1 import *
from functools import *

# *******   Módulos   *****

# -- Módulo para leer las notas
def LeerNotas(N):
    Notas = []
    # -- Poner título
    print()
    print('Ingresar las notas')
    for K in range(0, N):
        Nota = leernroreal('Ingresar la nota '+str(K+1)+': ', 0, 20)
        Notas.append(Nota)
    return Notas

# -- Módulo para procesar aprobados
def ProcesarNotas(Notas):
    print()
    print('PROCESO DE NOTAS ')
    NotasP = [Nota for Nota in Notas]
    print('Las notas son: ', NotasP)
    print('El número de notas es: ', len(NotasP))
    print('mayor nota ', reduce(lambda x, y : x<y,)
def ProcesarAprobados(Notas):
    print()
    print('PROCESO DE NOTAS APROBADAS')
    NotasA = [Nota for Nota in Notas if Nota >= 13.5]
    print('Las notas son: ', NotasA)
    print('El número de notas es: ', len(NotasA))
    if (len(NotasA) > 0):
        Suma = reduce(lambda x, y : x + y, NotasA)
        print('Promedio: ', Suma/len(NotasA))
def ProcesarDesaprobados(Notas):
    print()
    print('PROCESO DE NOTAS DESAPROBADAS')
    NotasA = [Nota for Nota in Notas if 9<=Nota <= 13.5]
    print('Las notas son: ', NotasA)
    print('El número de notas es: ', len(NotasA))
    if (len(NotasA) > 0):
        Suma = reduce(lambda x, y : x + y, NotasA)
        print('Promedio: ', Suma/len(NotasA))
def ProcesarReprobados(Notas):
    print()
    print('PROCESO DE NOTAS REPROBADAS')
    NotasA = [Nota for Nota in Notas if Nota <9]
    print('Las notas son: ', NotasA)
    print('El número de notas es: ', len(NotasA))
    if (len(NotasA) > 0):
        Suma = reduce(lambda x, y : x + y, NotasA)
        print('Promedio: ', Suma/len(NotasA))

# *******  Programa principal   *****

# -- Poner titulo
print()
print('PROCESAR NOTAS')
# -- Leer el número de alumnos
N = leernroentero('Número de Alumnos: ', 1, 100)
# -- Leer las notas
Notas = LeerNotas(N)
# -- Procesar aprobados
ProcesarAprobados(Notas)
ProcesarDesaprobados(Notas)
ProcesarReprobados(Notas)
