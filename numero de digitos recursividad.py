# **********************   MODULO   ***************************
# Módulo número de dígitos
def NroDigitos(N):
    if (N < 10):
        return 1
    else:
        return 1 + NroDigitos(N // 10)
    
# *****************   PROGRAMA PRINCIPAL   *******************
# -- Leer Numero
N = int(input('Ingresa un número: '))
# -- determinar el número de dígitos
ND = NroDigitos(N)
# -- Mostrar resultado
print('Número de dígitos = ',ND)
