"""una forma más limpia, más compacta de hacer funciones, es conocido como programación funcional, patrón de diseño llamado pipeline
https://ellibrodepython.com/programacion-funcional-python
lambda argumentos:expresion
"""
from functools import reduce
sumar=lambda x,y:x+y
print(sumar(8,2))

numeros=[1,2,3,4]
cuadrados=list(map(lambda numero:numero**2,numeros))
print(cuadrados)
edades=[18,23,6,9,12,11,50]
filtradoDeNumerosPares=list(filter(lambda numero:numero%2==0,numeros))
filtradoDeNumerosImpares=list(filter(lambda numero:numero%2!=0,numeros))
filtradoMayoresDeEdad=list(filter(lambda edad:edad>=18,edades))
print(filtradoDeNumerosPares)
print(filtradoDeNumerosImpares)
print(filtradoMayoresDeEdad)

sumaMaximaDeNumeros=reduce(lambda numOrigen,numDestino:numOrigen+numDestino,numeros)
print(sumaMaximaDeNumeros)

personas=[("Yolanda",48),("Ana",25),("Luis",19),("Pedro",30)]
personasOrdenadasPorLaEdad=sorted(personas,key=lambda persona:persona[1])
personasOrdenadasPorElNombre=sorted(personas,key=lambda persona:persona[0])
print(personasOrdenadasPorLaEdad)
print(personasOrdenadasPorElNombre)

def potencia(numeroParaElevarPotencia):
    return lambda numero:numero**numeroParaElevarPotencia

elevar_al_cubo=potencia(3)
print(elevar_al_cubo(2))

es_par=lambda numero:"Par" if numero%2==0 else "Impar"
print(es_par(2))
print(es_par(3))
operaciones = {
    'suma':lambda num1,num2:num1+num2,
    'resta':lambda num1,num2:num1-num2,
    'multiplicacion':lambda num1,num2:num1*num2,
    'division':lambda num1,num2:num1/num2
}

print(operaciones["multiplicacion"](2,5))

class Calculadora:
    suma=lambda self,x,y:x+y
    resta=lambda self,x,y:x-y

calculadora=Calculadora()
print(calculadora.suma(5,3))