# Importar libreria
import calendar
# Leer año y mes
anio = int(input('Ingrese el año: '))
mes = int(input('Ingrese el mes: '))
# -- Recuperar el calendario
calendario = calendar.month(anio, mes)
# -- Mostrar el caelndario
print(calendario)
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
    return ' '

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
  return nomMes, diaSemana, nroDia
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
  # -- Recuperar datos
  nomMes, diaSemana, nroDias = recuperarDatos(anio, mes)    
  # -- Generar el encabezado del calendario
  calendario = encabezadoCalendario(nomMes, anio)
  # -- Generar el cuerpo del calendario
  calendario += cuerpoCalendario(diaSemana, nroDias)
  # -- Generar el pie o parte final del calendario
  calendario += pieCalendario()  
  # -- Retornar resultado
  return calendario
