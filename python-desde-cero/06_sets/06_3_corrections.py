# 1. Crea un set con los nÃºmeros del 1 al 5 e imprÃ­melo.

my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. AÃ±ade el nÃºmero 6 al set {1, 2, 3, 4, 5} e imprÃ­melo.

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)

# 3. Intenta aÃ±adir el nÃºmero 5 al set {1, 2, 3, 4, 5} nuevamente. Â¿QuÃ© sucede?

my_set = {1, 2, 3, 4, 5}
my_set.add(5)

# Salida: {1, 2, 3, 4, 5} (no cambia porque los sets no admiten duplicados)
print(my_set)

# 4. Verifica si el nÃºmero 3 estÃ¡ en el set {1, 2, 3, 4, 5} e imprime el resultado.

print(3 in my_set)

# 5. Elimina el nÃºmero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.

my_set.remove(4)
print(my_set)

# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.

my_set.clear()
print(len(my_set))

# 7. Convierte el set {"manzana", "naranja", "plÃ¡tano"} en una lista e imprime el primer elemento de la lista.

my_set = {"manzana", "naranja", "plÃ¡tano"}
my_list = list(my_set)
print(my_list[0])

# 8. Realiza la uniÃ³n de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.

my_set1 = {1, 2, 3}
my_set2 = {4, 5, 6}
my_union_set = my_set1.union(my_set2)
print(my_union_set)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.

my_set1 = {1, 2, 3, 4}
my_set2 = {3, 4, 5, 6}
my_difference_set = my_set1.difference(my_set2)
print(my_difference_set)

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.

my_set = {1, 2, 3}
del my_set
# print(my_set)  # Esto generarÃ¡ un error: NameError