def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def leernatural(n):
    while n<0:
        print("error , numero fuera de rango....")
        n=int(input("escribir el numero del factorial que desea"))
    return n
n=int(input("escribir el numero del factorial que desea"))
print(factorial(n))
