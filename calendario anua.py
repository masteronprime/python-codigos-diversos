# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 17:31:20 2022

@author: marce
"""

# -- Módulo para recuperar el nombre del mes
def nombreMes(mes):
  T = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Setiembre','Octubre','Noviembre','Diciembre']
  return T[mes-1]
           # -- Módulo para determinar el número de días de un mes
def nroDiasMes(anio, mes):
  T = (31,28,31,30,31,30,31,31,30,31,30,31)
  return 29 if mes == 2 and anio % 4 == 0 else T[mes-1]
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
def linea(ini, med, sep, fin):
  return ini + (med*2 + sep)*6 + med*2 + fin
# -- Módulo para mostrar el encabezado del calendario
def encabezadoCalendario(nomMes, anio):
  L = [linea('┌','─','─','┐')]
  titulo = nomMes + ' - ' + str(anio)
  L += ['│'+titulo.center(20)+'│']
  L += [linea('├','─','┬','┤')]
  L += ['│Lu│Ma│Mi│Ju│Vi│Sa│Do│']
  L += [linea('├','─','┼','┤')]
  return L
# -- Módulo para mostrar el cuerpo del calendario
def cuerpoCalendario(diaSemana, nroDias):
  # -- Inicializar una lista
  LCuerpo = []
  # -- Generar cada linea de los días del calendario como un texto
  linea = '│  '*(diaSemana-1)+'│'
  for dia in range(1, nroDias+1):
    # -- Mostrar día del mes
    linea += (' ' if dia < 10 else '') + str(dia) + '│'  
    # -- incrementar día semana
    diaSemana += 1
    # -- verificar si se llegó a fin de semana
    if diaSemana > 7:
      # -- Cambio de línea, almacenando previamente la línea generarada en la lista
      LCuerpo += [linea]
      # -- Inicializar nueva linea
      linea = '│'
      # -- Incializar día semana
      diaSemana = 1  
  # -- Generar la última línea completando con espacios si hiciese falta
  linea += '  │'*(8-diaSemana)
  # -- Agregar la última línea a la lista de líneas del cuerpo
  LCuerpo += [linea]
  return LCuerpo
# -- Módulo para generar la última línea del calendario
def pieCalendario():  
  return linea('└','─', '┴','┘')
# -- Módulo para crear un calendario
def generarCalendario(anio, mes):
  # -- Recuperar datos
  nomMes, diaSemana, nroDias = recuperarDatos(anio, mes)    
  # -- Generar el encabezado del calendario
  calendario = encabezadoCalendario(nomMes, anio)  
  # -- Generar el cuerpo del calendario
  calendario += cuerpoCalendario(diaSemana, nroDias)  
  # -- Generar el pie o parte final del calendario
  if len(calendario) == 10:
    calendario += [linea('│',' ', '│','│')]
  calendario += [pieCalendario()]
  # -- Retornar resultado
  return calendario
# -- Módulo par mostrar el calendario mensual
def mostrarCalendarioMensual(calendario):
 for linea in calendario:
      print(linea)
      
      

# *******************  CALENDARIO  ******************

# -- Leer año y mes1
anio = int(input('Ingrese el año: '))
for mes in range(1,3):
    calendario=generarCalendario(anio, mes)
    for  i in calendario:
        print(f"{i:30}",end=" ")
        print(f"{i:30}",end=" ")
        print(f"{i:30}",end=" ")