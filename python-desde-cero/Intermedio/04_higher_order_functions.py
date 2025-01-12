## Funciones de orden superior ##

# funciones que hacen uso de otras funciones
# first class citizens

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_and_add(first_value, second_value, f_sum): # f_sum recibe otra función que es la que ejecuta en return
    return f_sum(first_value + second_value) # dependiendo la función se recibe, es lo que se calcula

print(sum_two_and_add(5, 6, sum_one)) # 12 # se envía la función sum_one como argumento para que después de sumar 5 + 6, se le sume 1
print(sum_two_and_add(8, 4, sum_five)) # 17 # 8 + 4 + 1

# @@@@@@@@@@@@@@@@@@@@@@@@
# CLOSURES
# @@@@@@@@@@@@@@@@@@@@@@@

# a lo que entendí, un closure, es una función definida dentro de otra función


def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten() # add_closure almacena la función add que retorna la función sum_ten
print(add_closure(5)) # 15, porque ahora si, a través de la variable add_closure que almacena la función add(value) es como podemos ejecutarla 
# Basicamente la forma de acceder a una función definida dentro de otra función es guardándola en una variable y después ejecutarla con los argumentos de la función interna

print(sum_ten()(5)) # de esta manera también podemos pasarle a través de sum_ten, un argumento a la función add y retornar su resultado


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### Built-in Higher Order Functions ####
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# todas las funciones de orden superior integradas en python requieren 
# de una función y un elemento iterable(lista, tupla, dict, etc)

# utilizamos como base una lista de números
my_list = [2, 5, 10, 21]

# @@@@@@@@@@@@@@@@@@@@@@@@
# MAP 
# @@@@@@@@@@@@@@@@@@@@@@@
# map(funcion, iterable)

# ejecuta una función sobre cada elemento de un iterable, en este caso de la lista de números
# primero necesitamos una función que realize alguna operación. en este caso, una función que 
# multiplica un número por 2
def mult_by_two(number):
    return number * 2

# la función de orden superior MAP, recibe dos parámetros:
# primero la función que queremos que corra en cada elemento de la lista 
# y el segundo parámetro es la lista de elementos
# y el resultado se puede guardar en una variable
result = map(mult_by_two, my_list)
print(result) # <map object at 0x1012321> el resultado es un objeto
# por lo que para poder manipular el resultado de map, es necesario guardarlo como una lista
result = list(result)
print(result) # [4, 10, 20, 42]

# todo lo anterior se puede hacer en una sola línea
result = list(map(mult_by_two, my_list))
print(result) # [4, 10, 20, 42]

# si no queremos guardar el resultado y sólo lo queremos imprimir:
print(list(map(mult_by_two, my_list))) # [4, 10, 20, 42]

# usando una funcióno lambda para no tener que definir la función y luego llamarla:
# la función lambda se define y llama en el mismo lugar
print(list(map(lambda number: number * 2, my_list))) # [4, 10, 20, 42]


# @@@@@@@@@@@@@@@@@@@@@@@@
# FILTER
# @@@@@@@@@@@@@@@@@@@@@@@

# conserva los elementos de la lista que regresan True después de ejecutar una función en cada elemento

# definimos primero una función
# en este ejemplo, una que determine si un número es mayor a 10
# y retorna True si es mayor a diez o False si no.
def mayor_a_diez(number):
    return number > 10

# utilizamos como base una lista de números
my_list = [2, 5, 10, 21, 30, 3]

print(list(filter(mayor_a_diez, my_list))) # [21, 30]
# como filter regresa un objeto, es necesario al final convertirlo a una lista para poderlo manipular

# aplicando una función lambda:
print(list(filter(lambda number: number > 10, my_list))) # [21, 30]



# @@@@@@@@@@@@@@@@@@@@@@@@
# REDUCE
# @@@@@@@@@@@@@@@@@@@@@@@
from functools import reduce
# aplica una función de DOS ARGUMENTOS acumulativos a los elementos de una lista de izquierda a derecha
# para que al final que de "reducido" a un solo valor.
# ejemplo: 
print(reduce(lambda a,b: a+b, [1, 2, 3, 4, 5])) # 15, ya que 1+2+3+4+5 = 15, es decir, ((((1+2)+3)+4)+5)

my_list = [1, 2, 3, 4, 5]

def suma(a, b):
    return a + b

print(reduce(suma, my_list)) # 15

######
# módulo operator
######

# ya python implementa funciones que suman o multiplican por ejemplo una lista de números
# para simplificar este proceso
# como las funciones add y mul
# que requieren que se importen de la siguiente manera:

from operator import add, mul

# las funciones add y mul sólo reciben dos argumentos por lo que son apropiadas para usarlas
# junto con la función reduce que requiere funciones que reciban sólamnete dos argumentos
print(add(1,2)) # 3 
print(mul(1,2)) # 2


my_list = [1, 2, 3, 4, 5]

print(reduce(add, my_list)) # 15 = 1 + 2 + 3 + 4 + 5
print(reduce(mul, my_list)) # 120 = 1 * 2 * 3 * 4 * 5






