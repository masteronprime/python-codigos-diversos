m=int(input("Ingrese el número de filas: "))
n=int(input("Ingrese el número de columnas: "))


A=[]
for j in range(m):
  A.append([0]*n)
  
print( "Lectura de la matriz A")
for j in range(m):
  for k in range(n):
    A[j][k] = float(input("Dame el componente (%d,%d): " %(j+1,k+1)))
    
for i in A:
  print (i)

C=[]      

      

orden = min(m, n)
for i in range(orden):
    for j in range(orden):
        if i + j == n  + 1:
            C.append(A[i][j])
print (C)
