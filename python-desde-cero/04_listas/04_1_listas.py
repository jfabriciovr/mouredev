### LISTAS ###
# son mutables

my_list = list()
my_other_list = []
print(len(my_list)) # 0
print(len(my_other_list)) # 0


my_list = [35, 24, 62, 52, 30, 30, 17]
my_list = list([35, 24, 62, 52, 30, 30, 17]) # Los corchetes son opcionales
print(my_list) # [35, 24, 62, 52, 30, 30, 17]
print(len(my_list)) # 7

my_other_list = [35, 1.77, "Brais", "Moure"]
print(my_other_list) # [35, 1.77, 'Brais', 'Moure"]
print(type(my_list)) # <class 'list'>
print(type(my_other_list)) # <class 'list'>
print(my_other_list[0]) # 35
print(my_other_list[1]) # 1.77
print(my_other_list[-1]) # "Moure" es el último elemento
print(my_other_list[-4]) # 35 es el primer elemento
#print(my_other_list[-5]) IndexError
#print(my_other_list[4]) IndexError
print(my_other_list.count("Brais")) # 1, es el número de ocurrencias de un valor
print(my_list.count(30)) # 2, porque el número 30 se repite 2 veces

# Concatenación
print(my_list + my_other_list) # [35, 24, 62, 52, 30, 30, 17, 35, 1.77, 'Brais', 'Moure']

# Funciones de listas o métdos
my_other_list.append("Mouredev")
print(my_other_list) # [35, 1.77, 'Brais', 'Moure', 'Mouredev']

my_other_list.insert(1, "Azul")
print(my_other_list) # [35, 'Azul', 1.77, 'Brais', 'Moure', 'Mouredev']

print(my_list) # [35, 24, 62, 52, 30, 30, 17]
my_list.remove(30)
print(my_list) # [35, 24, 62, 52, 30, 17] quita sólo el primer valor 30 que encontró

# pop() quita el último elemento de la lista
print(my_list.pop())  # 17 - pop devuelve el elemento que quita, por lo que se puede guardar en una variable o imprimirla
print(my_list) # [35, 24, 62, 52, 30]

my_pop_element = my_list.pop(2) # quita el elemento con el índice 2 y lo guarda en la variable
print(my_pop_element) # 62
print(my_list)  # [35, 24, 52, 30]

# del elimina un elemento en el índice indicado pero no lo devuelve
del my_list[2]
print(my_list) # [35, 24, 30]

my_list.clear() # elimina todos los elementos de la lista
print(my_list) # []

# Modificar un elemento de la lista
print(my_other_list) # [35, 'Azul', 1.77, 'Brais', 'Moure', 'Mouredev']
my_other_list[1] = "Rojo"
print(my_other_list) # [35, 'Rojo', 1.77, 'Brais', 'Moure', 'Mouredev']

my_new_list = my_other_list.copy()
my_other_list.clear()
print(my_other_list) # []
print(my_new_list) # [35, 'Rojo', 1.77, 'Brais', 'Moure', 'Mouredev']
my_new_list.reverse()
print(my_new_list) # ['Mouredev', 'Moure', 'Brais', 1.77, 'Rojo', 35]

my_new_list = [35, 24, 30]
my_new_list.sort()
print(my_new_list) # [24, 30, 35]

# sub listas
print(my_new_list[1:2]) # [30]
print(my_new_list[1:3]) # [30, 35]
