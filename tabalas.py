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
# Módulo que muestra una línea de asteriscos
def Asteriscos(N):
    print('*'*N)

# Módulo que muestra un texto dentro de un recuadro de asteriscos
def TextoAsteriscos(Texto):
    Asteriscos(len(Texto)+4)
    print('* '+Texto+' *')
    Asteriscos(len(Texto)+4)
    print()
def Menu():
    TextoAsteriscos('TABLAS ARITMÉTICAS')
    print('1 Sumar')
    print('2 Restar')
    print('3 Multiplicar')
    print('4 Dividir')
    print('5 FIN')
    
# Tabla Aritmetica de Sumar
def Sumar(K,N):
    return(str(K)+'+'+str(N)+'='+str(K+N))


# -- Modulo Procesar
def Procesar(Titulo,Operacion):
    TextoAsteriscos('TABLA ARITMETICA DE '+Titulo)
    # --- Ingresa Nro
    N = LeerNroEntero('Ingresa un Nro. entre 1 y 12: ',1,12)
    # -- Procesar Tabla
    for K in range(1,13):
        print(Operacion(K,N))
    
# Programa principal de Tablas Aritméticas
Opcion = 0;
while Opcion != 5:
    # Mostrar Menu
    Menu()
    # Leer Opción
    Opcion = int(input('    Ingrese opción -->'))
    if Opcion == 1:
        Procesar('SUMAR',Sumar)
    
