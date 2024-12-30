# Dictionaries

# Definición
my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}
my_dict = {
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.77
}

print(my_other_dict) # {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}
print(len(my_other_dict)) # 4
print(my_dict) # {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Swift', 'Kotlin', 'Python'}, 1: 1.77}
print(len(my_dict)) # 5

# imprimir el valor en base a una clave
print(my_dict["Nombre"]) # "Brais"

# cambiar el valor de una clave
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"]) # Pedro

# imprimir el valor buscando la clave con el número 1 (no estamos hablando de un índice)
print(my_dict[1]) # 1.77

# Agregar un nuevo campo al diccionario
my_dict["Calle"] = "Calle MoureDev"
print(my_dict) 
'''
{
    'Nombre': 'Pedro', 
    'Apellido': 'Moure', 
    'Edad': 35, 
    'Lenguajes': {'Kotlin', 'Python', 'Swift'}, 
    1: 1.77, 
    'Calle': 'Calle MoureDev'
}
'''
# Eliminar un elemento (clave y valor)
del my_dict["Calle"]
print(my_dict) # {'Nombre': 'Pedro', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Swift', 'Kotlin', 'Python'}, 1: 1.77}
'''
{
    'Nombre': 'Pedro', 
    'Apellido': 'Moure', 
    'Edad': 35, 
    'Lenguajes': {'Kotlin', 'Python', 'Swift'}, 
    1: 1.77
}
'''

# Búsqueda por Clve (key)
print("Moure" in my_dict) # False
print("Apellido" in my_dict) # True

# extraer la lista de parea de claves y nombres
print(my_dict.items()) # dict_items([('Nombre', 'Pedro'), ('Apellido', 'Moure'), ('Edad', 35), ('Lenguajes', {'Python', 'Kotlin', 'Swift'}), (1, 1.77)])

# extraer una lista de sólo las claves
print(my_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1])

# extraer una lista de sólo los valores
print(my_dict.values()) # dict_values(['Pedro', 'Moure', 35, {'Python', 'Kotlin', 'Swift'}, 1.77])

# crear un diccionario y pasarle una lista de claves sin valores
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
'''
{
    'Nombre': None, 
           1: None, 
      'Piso': None
}
'''


# Crear las claves de un diccionario copiándolas de una lista de elementos. todavía sin valores
my_list_of_keys = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list_of_keys)
print(my_new_dict)
'''
{
    'Nombre': None, 
           1: None, 
      'Piso': None
}
'''
# crear un diccionario nuevo a partir de otro diccionario ya existente (sólo se copian las claves)
my_new_dict = dict.fromkeys(my_dict) 
print(my_new_dict)
'''
{
    'Nombre': None, 
    'Apellido': None, 
    'Edad': None, 
    'Lenguajes': None, 
    1: None
}
'''

# si convertimos un diccionario a lista, tupla o set, sólo se van a copiar las claves (keys)
print(list(my_new_dict)) # ['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1]
print(tuple(my_new_dict)) # ('Nombre', 'Apellido', 'Edad', 'Lenguajes', 1)
print(set(my_new_dict)) # {1, 'Apellido', 'Edad', 'Nombre', 'Lenguajes'}



