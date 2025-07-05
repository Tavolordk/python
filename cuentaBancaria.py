class CuentaBancaria:
  def __init__(self,titular,saldo):
    self.__titular=titular
    self.__saldo=saldo
  def ver_saldo(self):
    print(f"Hola {self.__titular} su saldo actual es: ${self.__saldo}")
  def depositar(self,cantidad):
    if cantidad >0:
      self.__saldo+=cantidad
  def modificarNombre(self,nombre):
    self.__titular=nombre
#Encapsulamiento tipos de acceso
cuenta=CuentaBancaria("Ana",1000)
cuenta.modificarNombre('Octavio')
cuenta.depositar(500)
cuenta.ver_saldo()
