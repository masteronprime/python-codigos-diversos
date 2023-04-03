a=[]
def numeros():
 for i in range(1,n+1):
    for j in range(1,i+1):
        print(j)
def lista():
 a=[]
 n=int(input("insertar cuantos valores tendra la lista  "))
 for i in range(0,n):
    m=int(input("insertar un valor "))
    a.append(m)
 return a 
def repetidos(b):
 m=[]
 for j in b:
     if not j in m:
         m.append(j)
 return m
def divisores(n):
    i=0
    suma=0
    while i<n-1:
        i=i+1
        if n%i==0:
            suma=suma+i
    return suma 
def amigos(a1,b1):
    if divisores(a1)==b1 and divisores(b1)==a1:
        print("True")
    else:
        print("False")
def valores(k):
    k=int(k)
    if k>0 and k<9999:
        k=k
def pitagoras(valores):
    c=int(input("escribir un valor"))
    if valores(k)**2+valores(k)**2==c:
        print( valores(k)**2+valores(k)**2)
        print("True")
    else:
        print("False")
        print( valores(k)**2+valores(k)**2)
def cuadrado(a):
    columnas=3
    filas=3
    for i in range(filas):
       a.append([])
       for j in range(columnas):
           n=int(input("insertar valores"))
           a[i].append(n)
           print(a)
        
    


##b=lista()
##pitagoras(valores)
#amigos(a,b)
#print(repetidos(b))
#print(divisores())
print(cuadrado(a))
