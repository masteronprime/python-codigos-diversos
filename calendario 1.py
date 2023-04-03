import datetime
def main():
    año = int(input('Ingrese el año: '))
    mes = NroMes()
    dt = datetime.datetime(año, mes, 1)
    mostrar(espacio(dt.strftime('%A')), meses(mes), año, dias(mes, año))

def NroMes():
    mes = int(input('Ingrese el mes: '))
    if 1>mes>12:
        return NroMes()
    else:
        return mes

def meses(m):
    if m==1: return "Enero".center(9)
    elif m==2: return "Febrero".center(9)
    elif m==3: return "Marzo".center(9)
    elif m==4: return "Abril".center(9)
    elif m==5: return "Mayo".center(9)
    elif m==6: return "Junio".center(9)
    elif m==7: return "Julio".center(9)
    elif m==8: return "Agosto".center(9)
    elif m==9: return "Septiembre".center(0)
    elif m==10: return "Octubre".center(9)
    elif m==11: return "Noviembre".center(9)
    elif m==12: return "Diciembre".center(9)
def espacio(Dia):
    if Dia == "Monday": return 0
    elif Dia == "Tuesday": return 1
    elif Dia == "Wednesday": return 2
    elif Dia == "Thursday": return 3
    elif Dia == "Friday": return 4
    elif Dia == "Saturday": return 5
    elif Dia == "Sunday": return 6

def dias(m, a):
    if m in [1, 3, 5, 7, 8, 10, 12]: return 31
    elif m == 2:
        if bisiesto(a) == True: return 29
        else: return 28
    else: return 30

def bisiesto(año):
    return True if año%4 == 0 and año%100 != 0 or año%400==0 else False

def mostrar(e, m, a, d):
    print("┌──────────────────────────────────┐")
    print(f"│         {m} - {a}         │")
    print("├────┬────┬────┬────┬────┬────┬────┤")
    print("│ Lu │ Ma │ Mi │ Ju │ Vi │ Sa │ Do │")
    print("├────┼────┼────┼────┼────┼────┼────┤")
    for i in range(1,d+1+e):
        if i <=e: 
            print("│   " ,end=" ")
        else:
            print("│ "+str(i-e) if i<10 +e else "│"+str(i-e),end="  ")
            if i%7 == 0: print("│")

    print(("│    "*(7-(i%7))+"│"))
    print("└────┴────┴────┴────┴────┴────┴────┘")

main()
