def LeerNroRacional(Texto):
    N = int(input('Ingrese numerador del '+Texto+' número racional: '))
    D = int(input('Ingrese denominador del '+Texto+' número racional: '))
    while (D == 0):
        print('ERROR. El denominador no puede ser CERO')
        D = int(input('Ingrese denominador del '+Texto+' número recional'))
    N, D = Simplificar(N, D)
    return N, D
# Módulo de Menú de números racionales
def Menu():
    print()
    print(' ***** OPERACIONES DE NÚMEROS RACIONALES *****')
    print('1 Sumar')
    print('2 Restar')
    print('3 Multiplicar')
    print('4 Dividir')
    print('5 FIN')    

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
        Procesar(lambda N1, D1, N2, D2:Simplificar(N1 * D2 + N2 *D1 ,D1*D2))
    elif Opcion == 2:
        Procesar(lambda N1, D1, N2, D2:Simplificar(N1 * D2 - N2 *D1 ,D1*D2))
    elif Opcion == 3:
        Procesar(lambda N1, D1, N2, D2:Simplificar(N1 * N2,D1*D2))
    elif Opcion == 4:
        Procesar(lambda N1, D1, N2, D2:Simplificar(N1*D2,N2*D1))
