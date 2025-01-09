# 1. Crea una lista con los nÃºmeros del 1 al 5 e imprÃ­mela.
lista_numeros = [1, 2, 3, 4, 5]
print(lista_numeros)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
lista_numeros_decenas = [10, 20, 30, 40, 50]
print(lista_numeros_decenas[2]) # 30

# 3. Agrega el nÃºmero 6 al final de la lista [1, 2, 3, 4, 5] e imprÃ­mela.
lista_numeros.append(6)
print(lista_numeros) # [1, 2, 3, 4, 5, 6]

# 4. Inserta el nÃºmero 15 en la posiciÃ³n 2 de la lista [10, 20, 30, 40, 50].
lista_numeros_decenas.insert(2, 15)
print(lista_numeros_decenas) # [10, 20, 15, 30, 40, 50]

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
my_new_list = [10, 20, 30, 30, 40, 50]
my_new_list.remove(30)
print(my_new_list) # [10, 20, 30, 40, 50]

# 6. Usa la funciÃ³n pop() para eliminar el Ãºltimo elemento de la lista [1, 2, 3, 4, 5] y almacÃ©nalo en una variable. Imprime la variable y la lista.
lista_numeros = [1, 2, 3, 4, 5]
numero_eliminado = lista_numeros.pop()
print(numero_eliminado) # 5
print(lista_numeros) # [1, 2, 3, 4]

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprÃ­mela.
lista_numeros = [100, 200, 300, 400, 500]
lista_numeros.reverse()
print(lista_numeros) # [500, 400, 300, 200, 100]

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprÃ­mela.
lista_numeros = [3, 1, 4, 2, 5]
lista_numeros.sort()
print(lista_numeros) # [1, 2, 3, 4, 5]

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
lista_1 = [1, 2, 3]
lista_2 = list([4, 5, 6])
lista_concatenada = lista_1 + lista_2
print(lista_concatenada) # [1, 2, 3, 4, 5, 6]


# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posiciÃ³n 1 hasta la 3 (sin incluir la posiciÃ³n 3).
mi_lista = [10, 20, 30, 40, 50]
sub_lista = mi_lista[1:3]
print(sub_lista) # [20, 30]
