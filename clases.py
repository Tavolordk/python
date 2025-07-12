class Perro:
    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
    def ladrar(self):
     print(f"{self.nombre} dice: ¡Guau!")
perro1=Perro('Firulais','Boxer',2)
perro2=Perro('Zuky','Chihuahua',4)
perro1.ladrar()#abstraccion
perro2.ladrar()#abstraccion
