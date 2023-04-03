def leernroentero(texto,minimo,maximo):
    nro=int(input(texto))
    while (nro<minimo) or (nro>maximo):
        print("error , numero fuera de rango....")
        nro=int(input(texto))
    return nro
def leernroreal(texto,minimo,maximo):
    nro=float(input(texto))
    while (nro<minimo) or (nro>maximo):
        print("error , numero fuera de rango....")
        nro=float(input(texto))
    return nro
def mayordos(a,b):
    return a if a>b else b
def menor(a,b):
    return a if a<b else b
def intercambiar(a,b):
    temp=a
    a=b
    b=temp
    return(a,b)
def ordenardos(a,b):
    if a >b:
        a,b=intercambiar(a,b)
        return(a,b)
def distancia(x1,x2,y1,y2):
    r=((x2-x1)**2+(y2-y1)**2)**0.5
    return r
def perimetro (lado1,lado2,lado3):
    p=(lado1+lado2+lado3)
    return p
def estriangulo(lado1,lado2,lado3):
    if((lado1+lado2>lado3) and (lado1+lado3>lado2) and (lado2+lado3>lado1)):
       h=print("si es un triangulo")
    else:
       h=print("no es un triangulo")
    return h
def area(lado1,lado2,lado3):
    s=(lado1+lado2+lado3)/2
    b=((s*(s-lado1)*s(s-lado2)*s(s-lado3))**0.5)
    return b
    

