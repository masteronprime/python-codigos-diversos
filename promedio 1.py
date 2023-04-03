n=int(input("insertar la cantidad de alumnos "))
def p(n):
    if n>0:
        prom(n)
        p(n-1)
def  prom(n):
    sumar=0
    for i in range (n):
        m=int(input("insertar la nota  "+str(i)+" :  "))
        sumar=sumar+m
        promedio=(sumar/n)
    print(promedio)
p(n)
