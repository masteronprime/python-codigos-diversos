
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

# -- Módulo para procesar notas
def ProcesarNotas(Titulo, Notas, MCondicion):
    print()
    print('PROCESO DE NOTAS '+Titulo.upper())
    NotasP = [Nota for Nota in Notas if MCondicion(Nota)]
    print('Las notas son: ', NotasP)
    print('El número de notas es: ', len(NotasP))
    print('Promedio: ', reduce(lambda x, y : x + y, NotasP)/len(NotasP))
        

# *******  Programa principal   *****

# -- Poner titulo
print()
print('PROCESAR NOTAS')
# -- Leer el número de alumnos
N = leernroentero('Número de Alumnos: ', 1, 100)
# -- Leer las notas
Notas = LeerNotas(N)
# -- Procesar aprobados
ProcesarNotas('APROBADAS', Notas, lambda N : N >= 13.5)
ProcesarNotas("DESAPROBADAS",Notas,lambda N : 9<=N<13.5)
ProcesarNotas("REPROBADAS",Notas,lambda N : N<9)
