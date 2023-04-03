n=input("insertar la secuencia a ser identificada : ")
m=int(input("insertar la cantidad de secuencias candidatas"))
def hamming(n,*n1):
    suma=0
    i=-1
    while i<=len(n) :
        i+=1
        if n[i]!=n1[i]:
            suma=suma+1
            print(n[i])
            print(suma)
    if i>len(n):
        print("insertar otro valor") 
def lista(m):
    for x in range(m):
        n=input("valores")
n1=lista(m)
hamming(n,n1) 
