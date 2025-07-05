class Animal:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def hablar(self):
        return f"{self.nombre} dice:"

    
class Gato(Animal):
    def hablar(self):
         return super().hablar() + f" Miau y tengo {self.edad} años"

class Perro(Animal):
    def hablar(self):
        return super().hablar() + f"Guau y tengo {self.edad} años"

#Herencia
gato = Gato("Bigotes",2)
perro=Perro("Firulais",5)
print(gato.hablar())
print(perro.hablar())