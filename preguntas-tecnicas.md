1.¿Cuál es la diferencia entre == e is ?
== compara valores e is compara ubicación de memoria
2.¿Qué tipos de datos básicos tiene Python?
int, float, str, bool, list, tuple, set, dict, Nonetype
3.¿Qué significa que un objeto sea mutable o inmutable?
mutable quiere decir que si se puede modificar e inmutable que no se puede modificar.
4.¿Que es un f-string?
para combinar texto con variables más fácilmente
nombre="Octavio"
saludo=f"Hola,{nombre}"
5.¿Cuándo usarías una lista o una tupla?
lista cuando quiero que los valores cambien osea que sea mutable y una tupla cuando no osea inmutable
¿Qué es un set y para que sirve?
un set es para elementos únicos
Cómo obtener los elementos únicos de una lista
mi_lista=list(1,2,3,4,5,6,6,8,8,9)
set(mi_lista)
¿Qué es un función lambda?
es una función anónima osea más simplificada de una sola línea la cual podemos meter condicionales
cuadrado = lambda x: x*2
¿Qué es una clase?
Una clase es un tipo de dato abstracto que es una instancia de un objeto
class Persona:
  def __init__(self,nombre):
   self.nombre=nombre
p=Persona("Octavio")
p2=Persona("Adrian")
print(p.nombre)
¿Qué es self?
Referencia a la instancia actual dentro de los métodos.
Diferencias entre atributos de clase y de instancia:
atributos: Estos los comparte todas las instancias
instancia: Es propia del objeto
¿Qué es herencia?
Es la reutilización de atributos y métodos de una clase padre o superclase a una clase hija o subclase
¿Qué es una excepcion?
Es la captura de un error 
¿Qué es el bloque finally?
Es algo que se va a ejecutar si o si ocurra el error
¿Cómo lees y escribes un archivo de forma segura?
with open("nombre_archivo.txt","r") as f:
  contenido=f.read()
