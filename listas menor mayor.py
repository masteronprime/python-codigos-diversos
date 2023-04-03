'''
Se tiene el importe de las ventas totales diarias de una empresa,
correspondientes a los N primeros días del año. Escribir un programa 
que calcule: El promedio de ventas diarias, el monto máximo de venta ,
el monto mínimo de venta.
'''
# **********************   MÓDULOS   ***************************
# -----------  Leer Lista  -------------
def LeerLista():
    # -- Leer el número de elementos de la Lista
    N = int(input("Número de Dias de la Lista: "))
    # -- Inicializar un Lista vacío
    LV = []
    # -- Leer los elementos de la Lista
    for K in range(0, N):
        # -- Leer el K-ésimo elemento de la Lista
        # -- print("Ingresar el elemento ",K+1,":",end="")
        Elemento = float(input("Ingresar el Monto de Venta "+str(K+1)+": "))
        LV += [Elemento]

    # -- Retornar la  Lista
    return LV

# -----------  Calcular Promedio  -------------
def CalcularPromedio(LV):
    # -- Sumar los elementos de la Lista
    Suma = 0
    for E in LV:
        Suma += E
    # -- Calcular el promedio
    return Suma / len(LV)

# -----------  Determinar el mayor  -------------
def DeterminarMayor(LV):
    # -- Suponer el mayor igual a cero
    Mayor = 0
    for E in LV:
        if Mayor < E:
            Mayor = E        
    # -- Retornar el mayor
    return Mayor
def DeterminarMenor(LV):
    # -- Suponer el mayor igual a cero
    Menor = 999999
    for E in LV:
        if Menor > E:
            Menor = E        
    # -- Retornar el mayor
    return Menor

def DeterminarMenor(LV):

    
# *****************   PROGRAMA PRINCIPAL   *******************
# -- Leer la Lista con los importes de ventas totales por día
print('Ingresar el importe de las ventas totales por día')
LVentas = LeerLista()
# -- Calcular y mostrar el promedio de ventas diarias
Promedio = CalcularPromedio(LVentas)
print('Promedio =', Promedio)
# -- Determinar el importe máximo de venta diaria 
Mayor = DeterminarMayor(LVentas)
print('Mayor =', Mayor)
Menor = DeterminarMenor(LVentas)
print('Mayor =', Menor)
