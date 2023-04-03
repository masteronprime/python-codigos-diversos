# -- Módulo para recuperar el nombre del mes
def nombreMes(mes):
  if mes == 1:
    return 'Enero'
  elif mes == 2:
    return 'Febrero'
  elif mes == 3:
    return 'Marzo'
  elif mes == 4:
    return 'Abril'
  elif mes == 5:
    return 'Mayo'
  elif mes == 6:
    return 'Junio'
  elif mes == 7:
    return 'Julio'
  elif mes == 8:
    return 'Agosto'
  elif mes == 9:
    return 'Setiembre'
  elif mes == 10:
    return 'Octubre'
  elif mes == 11:
    return 'Noviembre'
  elif mes == 12:
    return 'Diciembre'
  else:
    return ''

# -- Módulo para determinar el número de días de un mes
def nroDiasMes(anio, mes):
  if mes in (1, 3, 5, 7, 8, 10, 12):
    return 31
  elif mes in (4, 6, 9, 11):
    return 30
  else:
    return 29 if anio % 4 == 0 else 28

# -- Módulo para determinar datos básicos necesarios para generar calendario
import datetime
def recuperarDatos(anio, mes):
  # -- Recuperar fecha del primer día del mes
  fechaIni = datetime.date(anio, mes, 1)
  # -- Determinar día de la semana al que corresponde el primer día del mes
  diaSemana = fechaIni.isoweekday()
  # -- Recuperar nombre del mes
  nomMes = nombreMes(mes)
  # -- Recuperar número de días del mes
  nroDias = nroDiasMes(anio, mes)
  # -- Retornar datos
  return nomMes, diaSemana, nroDias

# -- Módulo para dibujar línea de símbolos especiales
def linea(ini, med, sep, fin):
  return ini + (med*4 + sep)*6 + med*4 + fin + '\n'

# -- Módulo para mostrar el encabezado del calendario
def encabezadoCalendario(nomMes, anio):
  texto = linea('┌','─','─','┐')
  titulo = nomMes + ' - ' + str(anio)
  texto += '│'+titulo.center(34)+'│\n'
  texto += linea('├','─','┬','┤')
  texto += '│ Lu │ Ma │ Mi │ Ju │ Vi │ Sa │ Do │\n'
  texto += linea('├','─','┼','┤')
  return texto

# -- Módulo para mostrar el cuerpo del calendario
def cuerpoCalendario(diaSemana, nroDias):
  # -- Mostrar los días del calendario
  texto = '│    '*(diaSemana-1)+'│'
  for dia in range(1, nroDias+1):
    # -- Mostrar día del mes
    texto += ('  ' if dia < 10 else ' ') + str(dia) + ' │'  
    # -- incrementar día semana
    diaSemana += 1
    # -- verificar si se llegó a fin de semana
    if diaSemana > 7:
      # -- Cambio de línea
      texto += '\n│'
      # -- Incializar día semana
      diaSemana = 1
  # -- Completar espacios si hiciese falta
  texto += '    │'*(8-diaSemana)+'\n'
  return texto

# -- Módulo para generar la última línea del calendario
def pieCalendario():
  return linea('└','─', '┴','┘')


# -- Módulo par crear un calendario
def generarCalendario(anio, mes):
    CalendarLIST = []
    # -- Recuperar datos
    nomMes, diaSemana, nroDias = recuperarDatos(anio, mes)
    # -- Generar el encabezado del calendario
    encabezado = encabezadoCalendario(nomMes, anio)
    CalendarLIST.append(encabezado)
    # -- Generar el cuerpo del calendario
    cuerpo = cuerpoCalendario(diaSemana, nroDias)
    CalendarLIST.append(cuerpo)
    # -- Generar el pie o parte final del calendario
    pie = pieCalendario()
    CalendarLIST.append(pie) 
  # -- Retornar resultado
    return CalendarLIST

# *******  CALENDARIO  ******

# -- Leer año y mes
calendario = []
anio = int(input('Ingrese el año: '))
for IndMes in range(1, 13):
    mes = IndMes
    # -- Recuperar el calendario
    calendario.append(generarCalendario(anio, mes))
# -- Mostrar el calendario
for i in calendario:
    for j in range(0, 3):
        print(i[j])
