import random
galletas=int(input("insetar el numero de galletas "))
def elegirparticipante():
    comienza = random.randint(0, 1)
    if  comienza == 0:
        print('Comienza el jugador')
    else:
        print('Comienza el PC')
jugador =elegirparticipante()
def numerojugador(galletas):
     n=int(input("insetar un valor de 1 a 3 "))
     while n>0:
        if 1<n<4:
         galletas=galletas-n
         return galletas 
        else:
          print("insertar otro valor")
          n=int(input("insetar un valor de 1 a 3 "))
def numerodemaquina(galletas):
     mq=random.randint(1, 3)
     while 0<mq<4:
         if  (galletas-1)%4==0:
             p=galletas-mq
             return p
def truno(jugador,galletas):
    while galletas>0:
            print(numerojugador(galletas))
            
            print( numerodemaquina(galletas))
truno(jugador,galletas)
print(galletas)
