#main program
def main():
    print("*"*80)
    print("1 --------> si desea hallar  la media de una lista")
    print("2 --------> si desea hallar  el valor de la funcion")
    print("3 --------> si desea hallar  el valor de la serie armonica")
    print("4 --------> si desea hallar  el factorial de un numero")
    print("5 -------->si desea saber  si un numero es primo ")
    print("6 --------> si desea saber  si una palabra es palindroma")
    print("7 --------> si desea salir del menu ")
    print("*"*80)
#ejercicio1
#media de una lista
def media(n):
 l=[]
 for i in range(0,n) :
    m=int(input("insertar los elementos de la lista : "))
    l.append(m)
 media=sum(l)/n
 print(" la media es : ",media)
 #ejercicio 2
def funcion(n):
    if n==0:
        return 0
    else:
        return funcion(n-1)+n
#ejercicio 3
def serie(n):
    if n==1:
        return 1
    else:
        return (1/n)+serie(n-1)
#ejercicio 4
def factorial(n):
    while n==0:
        return 1
    else:
        return n*factorial(n-1)
#el teorema de wilson hace no indica si un numero es primo o no por medio de l factorial
#ejercicio 5
def teoremadewilson(n):
    if ((factorial(n-1)+1)%n==0):
      return "el numero "+str(n)+" si es primo"
    else:
      return "el numero "+str(n)+" no es primo"
#ejercicio 6
def palindroma(n):
    j=len(n)
    j1=-1
    while j>0 or  j1>len(n):
        j=j-1
        j1=j1+1
        if n[j]==n[j1]:
            return "es polindrona"
        else:
            return " no es  polindrona"
    
j=0
while j<7:
    main()
    j=int(input("insertar el numero que desea hallar : "))
    if j==1:
        n=int(input("insertar la cantidad de elementos de la lista : "))
        media(n)
    elif j==2:
        n=int(input("insertar el valor que desea calcular en la funcion :  "))
        print(funcion(n))
    elif j==3:
        n=int(input("insertar el valor que desea hallar en la serie armonica :  "))
        print(serie(n))
    elif j==4:
        n=int(input("insertar el factorial del numero que quieres hallar el factorial : "))
        print(factorial(n)) 
    elif j==5:
        n=int(input("insertar el numero que desea saber si es primo o no : "))
        print(teoremadewilson(n))
    elif j==6:
        n=input("insertar una palabra : ")
        print(palindroma(n))
    
        
        
        

