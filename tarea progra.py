n=input("insertar la secuencia a ser identificada : ")
m=int(input("insertar la cantidad de secuencias candidatas"))
l=[]
l1=[]
#ACtg
def hamming(n,l1,m):
    for i in range (0,m):
        x=input("insertar el  fragmento de la especie candidata numero " + str(  i+1  ) + " : " )
        for t in x:
          l1.append(t )
    return l1
def ident(n,m,l):
 for d in range(m):
    for t1 in n:
        l.append(t1)
 return l
n1=hamming(n,l1,m)
n2=ident(n,m,l)
def comparar(n1,n2):
    for i in range(min(len(n1), len(n2))):
        if n1[i] != n2[i]:
            return n1[i]
    return len(n1) == len(n2)
print(comparar(n1,n2))

