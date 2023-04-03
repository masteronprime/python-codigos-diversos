n=int(input("insertar el numero"))
def dimpa(n):
   #caso base
    if n==0:
        return 0
    #caso recurrente 
    if n>=0:
        return dimpa(n//10)+(n%2)
print(dimpa(n))
