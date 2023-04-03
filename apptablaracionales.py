# Programa para ilustrar operaciones de números racionales 

from libreria1 import *

# ************************  MÓDULOS  **************************

# ============== Módulo de Números Racionales  ====================

# Módulo Leer número racional
def LeerNroRacional(Texto):
    N = int(input('Ingrese numerador del '+Texto+' número racional: '))
    D = int(input('Ingrese denominador del '+Texto+' número racional: '))
    while (D == 0):
        print('ERROR. El denominador no puede ser CERO')
        D = int(input('Ingrese denominador del '+Texto+' número recional'))
    N, D = Simplificar(N, D)
    return N, D

# Módulo Simplificar
def Simplificar(A, B):        
    mcd = MCD(A, B)
    return A / mcd, B / mcd
    
# Módulo MCD
def MCD(A, B):        
    Resto = A % B
    while Resto != 0:
        A = B
        B = Resto
        Resto = A % B
    return B        
    
# Módulo de Menú de números racionales
def Menu():
    print()
    print(' ***** OPERACIONES DE NÚMEROS RACIONALES *****')
    print('1 Sumar')
    print('2 Restar')
    print('3 Multiplicar')
    print('4 Dividir')
    print('5 FIN')    
    
# Módulo  Sumar Nros Racionales
def Sumar(N1,D1,N2,D2):
    NS = N1 * D2 + N2 * D1
    DS= D1 * D2
    NS, DS = Simplificar(NS, DS)
    return NS,DS
def Restar(N1,D1,N2,D2):
    NS = N1 * D2 - N2 * D1
    DS= D1 * D2
    NS, DS = Simplificar(NS, DS)
    return NS,DS
def Multiplicar(N1,D1,N2,D2):
    NS = N1 * N2
    DS= D1 * D2
    NS,DS=Simplificar(NS, DS)
    return NS,DS
def  Dividir(N1,D1,N2,D2):
    NS = N1*D2
    DS= N2*D1
    NS,DS=Simplificar(NS, DS)
    return NS,DS
# Módulo procesar nro racionales
def Procesar(ModuloProcesar):
    # -- Leer dos números racionales
    N1, D1 = LeerNroRacional('Primer')
    N2, D2 = LeerNroRacional('Segundo')

    # -- Procesar los dos números racionales    
    NR, DR = ModuloProcesar(N1, D1, N2, D2)

    # --  Mostrar el resultado
    print(NR, '/', DR)

# Programa Principal del módulo de números racionales
Opcion = 0
while Opcion != 5:
    # Mostrar Menu
    Menu()
    # Leer Opción
    Opcion = int(input('    Ingrese opción -->'))
    if Opcion == 1:
        Procesar(Sumar)
    elif Opcion == 2:
        Procesar(Restar)
    elif Opcion == 3:
        Procesar(Multiplicar)
    elif Opcion == 4:
        Procesar(Dividir)
