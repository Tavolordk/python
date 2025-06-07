"""def calcularNomina(diasTrabajados,sueldoPorDia):
    return diasTrabajados*sueldoPorDia

def mostrarInformacionFiscalDelEmpleado(numeroEmpleados):
    for i in range(numeroEmpleados):
     nombre=input('Nombre empleado: ')
     sueldoPorDia=float(input('Sueldo por día: '))
     diasTrabajados=int(input('Dias trabajados: '))
     print('Su nómina es: ' + str(calcularNomina(diasTrabajados,sueldoPorDia)))

numeroEmpleados=int(input('Cuantos empleados tienes: '))
mostrarInformacionFiscalDelEmpleado(numeroEmpleados)
"""
def esNegativoPositivo(numero):
   if numero>=0:
      return True
   else:
      return False

def imprimeResultado(resultado):
   if resultado==True:
      print('Es positivo')
   else:
    print('Es negativo')

resultado1=esNegativoPositivo(-5)
imprimeResultado(resultado1)
resultado2=esNegativoPositivo(10)
imprimeResultado(resultado2)
resultado3=esNegativoPositivo(0)
imprimeResultado(resultado3)

