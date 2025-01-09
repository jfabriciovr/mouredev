#### CLASSES ###

'''
En Python, una clase es una plantilla que define cómo crear objetos, y es un concepto fundamental de la programación orientada a objetos (POO): 

Definición
Una clase es una estructura de programación que define los atributos y métodos que tendrá un objeto. 

Creación de objetos
Las clases actúan como plantillas para crear objetos concretos, llamados instancias de la clase. 

Atributos y métodos
Cada instancia de una clase puede tener sus propios valores para los atributos, pero comparte los métodos y la estructura básica de comportamiento con otras instancias de la misma clase. 

Modelo de entidades
Las clases se utilizan para modelar entidades del mundo real o abstracto en un programa de computadora. 
Las clases son una de las características más poderosas de Python y permiten organizar y estructurar el código de manera eficiente
'''

class MyEmptyClass: # las clases se escriben con CamelCase
   pass

class Person:
   def __init__(self, name, surname, alias="Sin alias"):
      #self.name = name
      #self.surname = surname
      self.full_name = f"{name} {surname} {alias}"
    
   def walk(self):
      print(f"{self.full_name} está caminando")

my_person = Person("Brais", "Moure")
#print(f"{my_person.name} {my_person.surname}") # Brais Moure 
print(my_person.full_name) # Brais Moure Sin alias
my_person.walk()
# Brais Moure Sin alias está caminando

my_other_person = Person("Brais", "Moure", "MoureDev") # name, surname, alias
print(my_other_person.full_name) # Brais Moure MoureDev
my_other_person.walk() # Brais Moure MoureDev está caminando
my_other_person.full_name = "Hétor de León"
print(my_other_person.full_name) # Héctor de León







