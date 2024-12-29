# Tuples 

# crear una tupla vacía
my_tuple = tuple()
my_other_tuple = ()

# crear una tupla con elementos
my_tuple = (35, 1.77, "Brais", "Moure")
print(my_tuple) # (35, 1.77, "Brais", "Moure")
print(type(my_tuple)) # <class 'tuple'>

print(my_tuple[0]) # 35
print(my_tuple[-1]) # Moure
#print(my_tuple[4]) # IndexError
#print(my_tuple[-6]) # IndexError
print(my_tuple.count("Brais")) # 1 - Encontró "Brais" una vez 
print(my_tuple.index("Moure")) # 3

# Modificar valores de la tupla no es posible
# my_tuple[1] = 1.80 # 'tuple' object does not support item assignment
my_other_tuple = (40, 1.70, "Fabricio", "Villalobos") # (35, 1.77, 'Brais', 'Moure', 40, 1.7, 'Fabricio', 'Villalobos')

# concatenación de tuplas pero el resultado se debe guardar en una nueva variable
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) # ('Moure', 40, 1.7)


#Modificar una tupla convirtiendo a lista
my_tuple = list(my_tuple)
print(my_tuple) # [35, 1.77, 'Brais', 'Moure']
print(type(my_tuple)) # <class 'list'>
my_tuple[3] = "dev"
my_tuple.insert(1, "azul") 
print(my_tuple) # [35, 'azul', 1.77, 'Brais', 'dev']
my_tuple = tuple(my_tuple)
print(my_tuple) # (35, 'azul', 1.77, 'Brais', 'dev')
print(type(my_tuple)) # <class 'typle'>

del my_tuple
# print(my_tuple) # NameError: name 'my_tuple' is not defined


