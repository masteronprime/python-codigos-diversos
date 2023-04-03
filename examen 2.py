n=int(input("insertar un numero en base 10"))
def conversion(n):
    if n>0:
      if n%2==1 :
         return str(conversion(n//2))+str(1)
      else:
         return str(conversion(n//2))+str(0)
    else:
        return 
print(conversion(n))
def conversion2(n):
    binario = bin(n)
    return binario

    
