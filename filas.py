'''
Se tiene la relación de los integrantes del equipo de Fútbol de IIS,
También se tiene la relación de integrantes del equipo de Basketball.
Escribir una aplicación que determine que estudiantes participan en
ambos equipos.
'''
# **********************   MÓDULOS   ***************************
# -----------  Leer Deportistas  -------------
def LeerDeportistas(Rotulo):
    # -- Ingresar el número de deportistas a leer
    N = int(input('Número de deportistas '+Rotulo+': '))
    # -- Inicializar lista
    LD = []
    # -- Leer los deportistas
    for K in range(0, N):
        # -- Leer el K-ésimo deportista
        D = input('Ingresar el deportista ' + str(K+1) + ': ')
        LD += [D]

    # -- Retornar lista de deportistas
    return LD

# -----------  Escribir Lista de deportistas -------------
def EscribirDeportistas(Rotulo, LD):
    # -- Escribir los elementos de la lista
    print()
    print('Relación de deportistas: ' + Rotulo)
    for D in LD:
        print(D)

# -----------  Intersección  -------------
def Interseccion(LF, LB):
    # -- Inicializar la lista resultado    
    LR = []
    # -- Ubicar los deportistas de fútbol en la lista de los deportistas de basket
    for DF in LF:
        if DF in LB:
            LR += [DF]
    # -- Devolver resultado
    return LR

# -----------  Unión  -------------
def Union(LF, LB):
    # -- Inicializar la lista resultado    
    LR = []
    # -- Copiar los deportistas de fútbol a la lista de resultados
    for DF in LF:
        LR += [DF]
    # -- Copiar los deportistas de basket en la lista de resultados
    for DB in LB:
        if DB not in LR:
            LR += [DB]
    # -- Devolver resultado
    return LR

# -----------  Diferencia  -------------


# -----------  Diferencia  simétrica -------------

    
# *****************   PROGRAMA PRINCIPAL   *******************
# -- Leer la Lista de los integrantes del equipo de Fútbol
print('Ingresar los integrantes del equipo de Fútbol')
LFutbol = LeerDeportistas('Fútbol')
print('Ingresar los integrantes del equipo de Basketball')
LBasket = LeerDeportistas('Basket')
# -- Determinar el total de deportistas
LResultado = Union(LFutbol, LBasket)
# -- Mostrar el total de deportistas
EscribirDeportistas('Total', LResultado)
# -- Determinar los deportistas que juegan en ambos equipos
LResultado = Interseccion(LFutbol, LBasket)
# -- Mostrar el total de deportistas
EscribirDeportistas('ambos equipos', LResultado)
