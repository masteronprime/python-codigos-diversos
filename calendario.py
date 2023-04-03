mes=int(input('ingrese mes [1-12]:'))
anio=int(input('ingrese año:[<?1900]'))
mes_valido=False
while not mes_valido :
    try:
        mes=int(input('ingrese mes [1-12]:'))
        if mes>= 1 and mes <=12:
            mes_valido=True
        else:
            print('error el mes ingresado debe estar en el rango espesificado')
    except ValueError:
        print('error el mes ingresado debe estar en el rango espesificado')
anio_valido=False
while not anio_valido:
    try:
        anio=int(input('ingrese año:[<?1900]'))
        if anio>=1900:
            anio_valido=True
        else:
            print('error el año ingresado debe estar en el rango espesificado')
    except ValueError:
        print('error el año ingresado debe estar en el rango espesificado')
def dia_mes(dia,mes,anio):
    #usanddo la  Convergencia de Zeller.
    #https://es.wikipedia.org/wiki/Congruencia_de_Zeller
    if mes in [1,2]:
        mes+=1
        anio-=1
    q,m,y=dia,mes,anio
    h=q+((13*(m+1))//5)+y+(y//4)-(y//100)+(y//100)%7
    return (h-1)%7
    #retorna la fecha
        
if mes_valido and anio_valido:
    calendario=['']*42
    idx=dia_mes(1,mes,anio)
    n_dias=num_dia_mes(mes,anio)
    calendario[idx:idx+n_dias]=range(1,n_dias+1)
    #[1,2,3,.....n-dias,,,](42 elementos )
    #['','',1,2,..n-dias,,,] (42 elementos)
    print_calendario(mes,calendario)
def num_dias(mes,anio):
    #regresar el numero de dias e una fecha
    if mes==2:
        #si corresponde a año bisiesto
        if anio %4==0 and (anio%100!=0 or anio %400==0):
            return 29
        else:
            return 28
    elif mes in [4,6,8,10]:
        return 30
    else:
        return 31
        
def print_calendario(mes,calendario):
    #imprime una lista de dias 842)
    nombre_mes={1:'ENERO', 2:'FEBREARO',3:'MARZO',4:'ABRIL',
                5:'MAYO',6:'JUNIO',7:'JULIO',8:'AGOSTO',9:'SEPTIEMBRE',
                10:'OCTUBRE',11:'NOVIEMBRE',12:'DICIEMBRE'}
    print(nombre_mes[mes])
    print(' D  L  M  M  J  V  S')
    for idx,dia in enumerate (calendario, start=1):
        print(f' {dia:2} ',end=' ')
        if idx % 7==0:
            print ()
