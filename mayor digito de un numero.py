n=int(input("insertar el numero"))
def d2(a,b):
    if a>=b:
        return a
    else:
        return b
def dm(n):
    #caso baase
    if n<10:
        return n%10
    #caso recurrente 
    if n>=10:
        return d2(dm(n//10),n%10)
print(dm(n))
