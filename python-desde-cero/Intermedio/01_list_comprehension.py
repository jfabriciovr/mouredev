## LIST COMPREHENSION ##
# se utiliza para crear listas donde se pueden implementar
# operaciones a cada elemento antes de incorporarlo a la lista


## distintas formas de crear una lista

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list) # [0, 1, 2, 3, 4, 5, 6, 7]

my_list = [i for i in my_original_list]
print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7]

my_list = [i for i in range(8)]
print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7]

my_range = range(8)
print(list(my_range)) # [0, 1, 2, 3, 4, 5, 6, 7]




## Realizar operaciones con cada elemento antes de
## meter el dato a la lista

# agrega 1 antes de meter el dato a la lista
my_list = [i + 1 for i in range(8)] 
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

my_list = [i * 2 for i in range(8)]
print(my_list) # [0, 2, 4, 6, 8, 10, 12, 14]

# multiplicar cada número por sí mismo
my_list = [i * i for i in range(8)]
print(my_list) # [0, 1, 4, 9, 16, 25, 36, 49]





## usando una función
def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list) # [5, 6, 7, 8, 9, 10, 11, 12]















