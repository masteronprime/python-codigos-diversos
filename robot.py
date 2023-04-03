n=int(input("insertar la cantidad de metros : "))
def robot(n):
    if n<=2: return n
    else: return robot(n-2)+robot(n-1)
print(robot(n))
