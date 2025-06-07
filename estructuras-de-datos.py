"""Ejercicio Práctico: Registro de Calificaciones de Alumnos
Objetivo:
Practicar el uso de variables, operadores, estructuras de datos como listas y diccionarios, y entrada/salida básica.

Enunciado:
Desarrolla un programa en Python que permita registrar alumnos y sus calificaciones, y luego calcular el promedio de cada alumno y mostrar su estatus (Aprobado/Reprobado).

Requisitos:
Solicitar al usuario el número total de alumnos a registrar.

Para cada alumno:

Pedir su nombre.

Pedir tres calificaciones (valores entre 0 y 10).

Guardar la información en un diccionario, donde la clave sea el nombre del alumno y el valor sea una lista de sus tres calificaciones.

Al finalizar, mostrar un reporte así:

REPORTE FINAL:
Alumno: Juan Pérez
Calificaciones: [8.0, 9.0, 7.5]
Promedio: 8.2
Estatus: Aprobado

Alumno: Ana López
Calificaciones: [6.0, 5.5, 6.0]
Promedio: 5.8
Estatus: Reprobado"""

numeroTotalDeRegistro=int(input('Dame número de alumnos a registrar: '))
status=''
estudiantes={}
for registro in range(numeroTotalDeRegistro):
 nombre=input('Inserta tu nombre: ')
 calificaciones=[]
 promedio=0
 for i in range(3):
  calificacion=float(input('Inserta calificación: '))
  calificaciones.append(calificacion)
  promedio=round(sum(calificaciones)/3,1)
  if promedio>=6:
   status='Aprobado'
  else:
   status='Reprobado'
 estudiantes[nombre]={'Calificaciones':calificaciones, 'Promedio':promedio,'Estatus':status}
for clave,datos in estudiantes.items():
 print('Nombre: ' + str(clave))
 print('Calificaciones: ' + str(datos['Calificaciones']))
 print('Promedio: ' + str(datos['Promedio']))
 print('Estatus: ' + str(datos['Estatus']))
