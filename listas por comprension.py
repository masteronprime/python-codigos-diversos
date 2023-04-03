'''
LISTAS POR COMPRENSIÓN

[ Elemento_devuelto for E in L if Condición]

'''

def ExisteDigito(d, N):
    if N == 0:
        return False
    else:
        if N % 10 == d:
            return True
        else:
            return ExisteDigito(d, N//10)
            
def SumaDigitos(N):
    return N if N < 10 else SumaDigitos(N // 10) + (N % 10 )

# --- Programa principal -----------

L = [11,32,47,64,15,16,24,8,19,80,22]
# -- Mostrar lista original
print('Lista original: ',L)

# -- Recuperar los cuadrados de los elementos de la lista
L1 = [E**2 for E in L]
print('Cuadrados: ',L1)

# -- Recuperar los elementos impares de la lista
L2 = [E for E in L if E % 2 ==1]
print('Impares: ',L2)

# -- Recuperar los elementos que tenga algun digito 2
L3 = [E for E in L if ExisteDigito(2, E)]
print('Números que tenga el dígito 2: ',L3)

# -- Recuperar la suma de los dígitos de cada elemento
L4 = [SumaDigitos(E) for E in L]
print('Suma dígitos: ',L4)
