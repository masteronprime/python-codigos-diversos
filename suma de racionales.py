'''
##############################################################
      Programa que permita procesarf números racionales
##############################################################
'''  
 
# Módulo MCD
def MCD(A, B):
    R = A % B
    while (R != 0):
        A = B
        B = R
        R = A % B
    return B

# Módulo simplificar
def Simplificar(A, B):
    M = MCD(A, B)
    A = A // M
    B = B // M
    return A, B


# Módulo Leer número racional
def LeerNroRacional(Texto):
    N = int(input('Ingrese numerador del '+Texto+' número racional: '))
    D = int(input('Ingrese denominador del '+Texto+' número racional: '))
    while (D == 0):
        print('ERROR. El denominador no puede ser CERO')
        D = int(input('Ingrese denominador del '+Texto+' número recional'))
    N, D = Simplificar(N, D)
    return N, D

# Módulo Sumar nro racionales
def Sumar(N1, D1, N2, D2):
    NS = N1 * D2 + N2 *D1
    DS = D1 * D2
    N, D = Simplificar(N, D)
    return N, D

# Módulo Restar nro racionales
def Restar(N1, D1, N2, D2):
    NS = N1 * D2 - N2 *D1
    DS = D1 * D2
    N, D = Simplificar(N, D)
    return N, D


# Módulo para procesar Sumar nro racionales
def SumarNrosRacionales():
    # -- Leer dos números racionales
    N1, D1 = LeerNroRacional('Primer')
    N2, D2 = LeerNroRacional('Segundo')

    # -- Sumar los dos números racionales    
    NR, DR = Sumar(N1, D1, N2, D2)

    # --  Mostrar el resultado
    print(NR, '/', DR)

# Módulo para procesar Restar nro racionales
def RestarNrosRacionales():
    # -- Leer dos números racionales
    N1, D1 = LeerNroRacional('Primer')
    N2, D2 = LeerNroRacional('Segundo')

    # -- Restar los dos números racionales    
    NR, DR = Restar(N1, D1, N2, D2)

    # --  Mostrar el resultado
    print(NR, '/', DR)

# Módulo para mostrar menú
def Menu():
    print('')
    print('**********************************')
    print('OPERACIONES CON NÚMEROS RACIONALES')
    print('**********************************')
    print('1-> Sumar')
    print('2-> Restar')
    print('3-> Multiplicar')
    print('4-> Dividir')
    print('5-> FIN')
    print('')    

# Módulo para procesar nro racionales
def ProcesarNrosRacionales():
    # -- Declarar opción
    Opcion = 0

    # -- Procesar opciones
    while Opcion < 5:
        # -- Mostrar menú
        Menu()
        # -- Leer opción
        Opcion = int(input('Ingrese opción: '))      
        # -- Procesar opcion
        if Opcion == 1:
            SumarNrosRacionales()
        elif Opcion == 2:
            RestarNrosRacionales()
        elif Opcion == 3:
            MultiplicarNrosRacionales()
        elif Opcion == 4:
            DividirNrosRacionales()
                
# #######################################################
#                   Programa principal
# #######################################################

ProcesarNrosRacionales()
