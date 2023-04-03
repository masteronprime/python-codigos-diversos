from libreria1 import *

# *******  Módulos   *********
# --  Leer lista de notas
def LeerNotas(N):
    # -- Inicializar una lista vacía de notas
    Lista = []
    # -- Leer cada nota
    for K in range(0, N):
        # -- Leer la K-ésima nota
        Rotulo = 'Ingresar la nota '+str(K+1)+':'
        Nota = leernroentero(Rotulo, 0, 20)
        Lista.append(Nota)
    # -- Retornar la lista
    return Lista

# *******  Programa principal   *****

# -- Poner titulo
print()
print('PROCESAR NOTAS')
# -- Leer el número de alumnos
N = leernroentero('Número de Alumnos: ', 1, 100)
# -- Leer las notas
Notas = LeerNotas(N)
# -- Contar número de alumnos aprobados
print('Aprobados:', len([x for x in Notas if x >=13.5 ]))
# -- Contar número de alumnos desaprobados
print('Desaprobados:', len([x for x in Notas if 10< x < 13.5 ]))
# -- Contar número de alumnos reprobados
print('reprobados:', len([x for x in Notas if x < 10]))
