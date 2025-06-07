from tkinter import *

def menu(opcion):
 num1=float(input('Inserta primer numero: '))
 num2=float(input('Inserta segundo numero: '))
 match opcion:    
    case 1:
     print(str(suma(num1,num2)))
    case 2:
     print(str(resta(num1,num2)))
    case 3:
     print(str(division(num1,num2)))
    case 4:
     print(str(multiplicacion(num1,num2)))

def suma(num1,num2):
 return num1+num2

def resta(num1,num2):
 return num1-num2

def multiplicacion(num1,num2):
 return num1*num2

def division(num1,num2):
 if num2==0:
  print('La division entre 0 no es posible regresando al menu principal: ')
  bienvenida()
 return num1/num2

def bienvenida():
 print('BIENVENIDO A MI CALCULADORA...')
 print('1)SUMA')
 print('2)RESTA')
 print('3)DIVISION')
 print('4)MULTIPLICACION')
 opcion=int(input('ELIGE UNA OPCIÓN:'))
 menu(opcion)

bienvenida()