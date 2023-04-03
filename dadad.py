a=int(input("insertar un valor"))
impar=2*a-1
def  copa(impar):
    if  impar>0:
        return " "
    else:
         copa(impar)
         print("*"*impar)
print(copa(impar))


