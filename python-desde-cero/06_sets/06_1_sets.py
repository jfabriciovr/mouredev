## SETS, son mutables, pero no se almacenan en orden, cada que se corre el programa, puede cambiar el orden de los elementos

# Definición
my_set = set()
my_other_set = {} # esto no es correcto para un set, tiene que crearse con elementos desde un inicio
my_other_set = {"Brais", "Moure", 35}
print(my_other_set) # {'Moure', 35, 'Brais'}
print(type(my_other_set)) # <class 'set'>
print(len(my_other_set)) # 3

# Inserción - Un set no es una estructura ordenada
my_other_set.add("Mouredev")
print(my_other_set) #  {'Moure', 35, 'Mouredev', 'Brais'}

my_other_set.add("Mouredev") # un set no admite repetidos, sin embargo, no genera error
print(my_other_set) #  {'Moure', 35, 'Mouredev', 'Brais'}

# Búsqueda
print("Moure" in my_other_set) # True
print("Mouri" in my_other_set) # False

# Eliminación - son mutables, por lo tanto si se pueden borrar elementos
my_other_set.remove("Moure")
print(my_other_set) # {'Brais', 35, 'Mouredev'}

my_other_set.clear() # elimina todo el contenido del set
print(len(my_other_set)) # 0

del my_other_set
#print(my_other_set) # NameError: name 'my_other_set' is not defined

# Transformación
my_set = {"Brais", "Moure", 35} # creación de un set
my_list = list(my_set) # convierte el set en una lista
print(my_list) # ['Brais', 35, 'Moure']
print(my_list[0]) # Brais

# Otras operaciones
my_other_set = {"Kotlin", "Swift", "Python"}
print(f"my_set: {my_set}") # my_set: {"Brais", "Moure", 35}
print(f"my_other_set: {my_other_set}") # my_other_set: {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(f"union of my_set con my_other_set: {my_new_set}") # {"Brais", "Moure", 35, "Kotlin", "Swift", "Python"}

print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) # {'Kotlin', 35, 'C#', 'Python', 'JavaScript', 'Swift', 'Moure', 'Brais'}
print(my_new_set.difference(my_set)) # {'Kotlin', 'Swift', 'Python'}

