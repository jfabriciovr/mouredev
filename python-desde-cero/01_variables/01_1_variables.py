my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable) # 5
print(type(my_int_variable)) # <class 'int'>

my_int_to_str_variable = str(my_int_variable) # la función str convierte el argumenta a una cadena de texto
print(my_int_to_str_variable) # 5
print(type(my_int_to_str_variable)) # <class 'str'> 

my_bool_variable = False
print(my_bool_variable) # False
print(type(my_bool_variable)) # <class 'bool'>

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable) # My String variable 5 False
print("Este es el valor de:", my_bool_variable) # Este es el valor de: False

# Algunas funciones del sistema
print(len(my_string_variable)) # 18

# Variables en una sola lÃ­nea. Â¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('Â¿CuÃ¡l es tu nombre? ')
age = input('Â¿CuÃ¡ntos aÃ±os tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# Â¿Forzamos el tipo?
address: str = "Mi direcciÃ³n"
address = True
address = 5
address = 1.2
print(type(address))