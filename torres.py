n=int(input("cantidad de discos"))
inicio=1
final=4
def hanoi(n,inicio,final):
    if n==1 :
    #caso auxliar base 
     print("mover de ",str(inicio),"a",str(final))
    else:
    #caso recurrente
     auxiliar=8-inicio-final
     hanoi(n-1,inicio,auxiliar)
     hanoi(1,inicio,final)
     hanoi(n-1,auxiliar,final)
print(hanoi(n,inicio,final))
