def suma(n):
    if n==1:
        return 1
    else:
        return suma(n-1)+n
def multiplicacion(a,b):
    if b==0:
        return 0
    else:
        return multiplicacion(a,b-1)+a
def cifras(n):
    if n<10:
        return 1
    else:
        return cifras(n//10)+1
def potencia(a,b):
    if b==0:
        return 1
    else:
        return potencia(a,b-1)*a

a=int(input("insertar el valor del numero que quiere que se sume "))
b=int(input("insertar el valor del numero que quiere que se sume "))
n=int(input("insertar el valor del numero que quiere que se sume "))
print(multiplicacion(a,b))
print(cifras(n))
print(potencia(a,b))
print(suma(n))
