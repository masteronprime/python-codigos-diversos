a=[]
def matriz(a):
    filas=int(input("insertar el numero de filas"))
    columnas=int(input("insertar el numero de filas"))
    ceros=0
    sumar=0
    n=0
    for i in range (filas):
        a.append([])
        for j in range(columnas):
            n=int(input(" insertar valores de la componente (%d,%d) "%(i+1,j+1)))
            a[i].append(n)
    for k in range(filas):
        print(a[k])
        while n>=0 and n<columnas:
            n=n+1
            if a[k][0]*a[k][0]==1 or a[k][1]*a[k][1]==1:
               print( "gano el jugador  1")
            if  a[k][0]*a[k][0]==-1 or a[k][1]*a[k][1]==-1:
                print("gano el jugador  2")
            if k==n:
                sumar=sumar+a[k][n]
            print(sumar)
    
print(matriz(a))
