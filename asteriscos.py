x=int(input("insertar un valor "))
def a(x):
    if x>0:
        print("*"*x)
        a(x-1)
def m(x):
    if x>0:
        print(" "*20+ x*"*")
        m(x-1)
        print(" "*20+"*"*x)
m(x)
