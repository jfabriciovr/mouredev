### Functions ###

# DefiniciÃ³n

def my_function():
    print("Esto es una funciÃ³n")


my_function()
my_function()
my_function()

# FunciÃ³n con parÃ¡metros de entrada/argumentos


def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2) # 6.6

# FunciÃ³n con parÃ¡metros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2) # 6.6
print(my_result) # None - porque la función no retorna nada

my_result = sum_two_values_with_return(10, 5)
print(my_result) # 15


# FunciÃ³n con parÃ¡metros de entrada/argumentos por clave
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure", name="Brais") # Brais Moure

# FunciÃ³n con parÃ¡metros de entrada/argumentos por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure") # Brais Moure Sin alias
print_name_with_default("Brais", "Moure", "MoureDev") # Brais Moure MoureDev

# FunciÃ³n con parÃ¡metros de entrada/argumentos arbitrarios
def print_texts(*text): # *text quiere decir argumentos infinitos
    print(type (text))
    print(text)

print_texts("estos", "textos", "se imprimen como tuplas") 
# <class 'tuple'>
# ('estos', 'textos', 'se imprimen como tuplas')


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts: # recorre la tupla de elementos y va imprimiendo cada uno en una línea independiente
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
# <class 'tuple'>
# HOLA
# PYTHON
# MOUREDEV

print_upper_texts("Hola")
# <class 'tuple'
# HOLA


