# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Importamos los módulos necesarios
import math
import numpy as np
from matplotlib import pyplot as plt

# Generamos los datos para el gráfico
n=int(input("insertar el costo inferior de un articulo  "))
n1=int(input("insertar el costo superior de un articulo  "))
n2=int(input("insertar el costo que sea mas posible que se de "))
p=1/(n2-n)
b=-(p*n)
x3=str(1)+"/"+str(n2-n)+"*"+"x"+str(b)
p1=(1/(n1-n2))
b1=(p1*n1)
y3="-"+str(1)+"/"+str(n1-n2)+"*"+"x"+"+"+str(b1)
x1=lambda x:(y-b)*p
x2=lambda x:-1*((y-b1)*p1)
y=np.linspace(-30,40)
print("===============================================")
print("de 0 a "+str(n)+"="+"0")
print("===============================================")
print(x3)
print("===============================================")
print(y3)
print("===============================================")
print("de"+  str(n1)+ "a "+"mas"+"="+"0")
aa=x1(y)
bb=x2(y)
# Creamos el gráfico
plt.ion()
plt.plot(aa,y,color="red")
plt.plot(bb,y,color="green")
plt.title("funcion pertenencia ")
plt.grid()
plt.xlabel("eje x ")
plt.ylabel("eje y ")

