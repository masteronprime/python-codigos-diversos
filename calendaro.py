from math import* #importamos math para poder utlizar floor 

# Funcion que te devuelve el numero de mes, ingreso un  string y me devuelve el mes en numero
def dameMes(m):
    if m in meses:
        if m =='enero': 
            return 1
        elif m =='febrero':
            return 2
        if m =='marzo': 
            return 3
        elif m =='abril':
            return 4
        if m =='mayo': 
            return 5
        elif m =='junio':
            return 6
        if m =='julio': 
            return 7
        elif m =='agosto':
            return 8
        if m =='setiembre': 
            return 9
        elif m =='octubre':
            return 10
        if m =='noviembre': 
            return 11
        elif m =='diciembre':
            return 12
    else:
        print("mes ingresado incorrecto") 
        return -1
    
    
    
    
    

#funcion que te dice si un año es bisiesto o no lo es devuelve un dato booleano
def anio_bisiesto(anio):
    if (anio%4==0 and anio%100!=0) or (anio%400==0):
        return True
    else:
        return False
    
      
        
    
#funcion que te devuelve el numero de dias por cada mes    
def calDias(m,a):
  try:    
      if m==2:  
        if  anio_bisiesto(a):
            return 29
        else :
            return 28
      if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
          return 31
      elif m==4 or m==6 or m==9 or m==11:    
          return 30
  except:
    print("error 4")        #generamos try except pra validar que cada funcion nos retorne datos correctos

   
      
    
       
#funcion que te devuelve el dia entre domingo y sabado que corresponde para un dia , mes y año especifico  
def diaSemana(m,a,d):
  try: 
    digito_siglo=anio//100
    digito_anio=anio%100
    
    valor=digito_anio+floor(digito_anio/4)


    if digito_siglo==18:
        valor=valor+2
    
    elif digito_siglo==20:
        valor=valor+6
    
    if mes==1 and anio  is not anio_bisiesto(a):
        valor=valor+1
    elif mes==2 and anio is anio_bisiesto(a):
        valor=valor+3
    elif mes==2 and anio  is not anio_bisiesto(a) :
        valor=valor+4
    elif mes==3 or mes==11:
        valor=valor+4
    elif mes==4 or mes==7:
        valor=valor+0
    elif mes==5:
        valor=valor+2
    elif mes==6:
        valor=valor+5
    elif mes==8:
        valor=valor+3
    elif mes==10:
        valor=valor+1
    elif mes==9 or mes==12:
        valor=valor+6

    valor=(valor+d)%7
    #print(valor)      

    if valor==1:
        dia_semana="Domingo"
    elif valor==2:
        dia_semana="Lunes"
    elif valor==3:
        dia_semana="Martes"
    elif valor==4:
        dia_semana="Miercoles"
    elif valor==5:
        dia_semana="Jueves"        
    elif valor==6:
        dia_semana="Viernes"
    elif valor==0:#corregir
        dia_semana="Sabado"
    return dia_semana
  except:
      print ("error desconocido 3")
    
    
 
 #funcion que te devuelve el numero de dias que tiene que imprimir espacios en blanco antes del primer dia   
def calculaEspacio(d):
    if d=='Domingo':
        return 0
    elif d=='Lunes':
        return 1
    elif d=='Martes':
        return 2
    elif d=='Miercoles':
        return 3
    elif d=='Jueves':
        return 4
    elif d=='Viernes':
        return 5
    elif d=='Sabado':
        return 6
   

 #funcion que te imprime el calendario   
def imprimeCalendario(ms,mn,a,d):
  try:  
    dias=['Dom','Lun','Mar','Mier','Jue','Vie','Sab']  #se genera una lista de los dias 
    mesanio = '{0}  {1}'.format(ms.upper(),a) #utilizamos un metodo de formato 
                                              #para que convierta el año ingresado como string ya sea , 
                                              #si se ingreso en minusculas o mayusculas o mixto  todo el 
                                              #texto se convertira en mayuscula
        
    numE=calculaEspacio(d)  #llamamos a la funcion que nos calculara el n° de espacios 
                            #que esta antes de el dia situado 
                            #desde el primer dia que cae en cada mes 
               
    print(mesanio)          #imprimimos el año para validar
    
    for i in dias:            #este lazo recorrera los dias e imprimira un concatenador
                              #para que una los dias sin un salto de linea
        print(i,end=' ')
    linea = ''
    linea=linea + numE*'    '   #en esta parte se probo y calculo los espacios para una impresion con formato
    linea=linea+'1   '
    print('\n',linea,end='')
    if d=='Sabado':
        print('\n',end=' ')
       
    
    
    
    for i in range(2,calDias(mn,a)+1):
        nu=diaSemana(mn,a,i)
        if nu=='Sabado':
            print(i,'\n',end=' ')            
        else:  
            if i<10:
                print(i,end='   ')
            else:
                print(i,end='  ')
  except:
    print("error desconocido2")       
    
    
## aqui inicia toda la logica    
mes_31=(1,3,5,7,8,10,12)
anio_a=range(1800,2099)
meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","setiembre","octubre","noviembre","diciembre"]


mesSTR=input("Ingrese el mes  : ").lower() #convertimos el mes en string y en minusculas
mes=dameMes(mesSTR) #mes en numero

#validamos el ingreso de los datos

try:
   anio=int(input("Ingrese el año [1800:2099]:"))
   if anio  not in anio_a:
     print("el año debe de estar en el rango [1800-2099]")
   else:     
       print(' ')
       imprimeCalendario(mesSTR,mes,anio,diaSemana(mes,anio,1))       
       
except:
    print("Ingrese un año valido")
