#Implementar una función recursiva llamada “ordenadoCrecientemente”, que tenga
 #como parámetro de entrada un número entero positivo y verifique si los dígitos de dicho
#número están ordenados crecientemente. Puede implementar funciones auxiliares que
#permitan implementar dicha función. Implementar una función principal que permita
#ingresar un número y muestre un mensaje indicando si los dígitos están o no ordenados
#de forma creciente.
n=int(input("insertar un numero"))
    
def mayor(a,b):
    if int(a)>int(b):
        return a
    else:
        return b
def ordenadoCrecientemente(n):
    l=[]
    if n == 0:
     cotador = 1
    else:
     cotador = 1
     while (n >= 10):
      cotador += 1
      n = n//10
      l.append(n)
     return l
	        #imprime(n)
c=ordenadoCrecientemente(n) 
print(c)
