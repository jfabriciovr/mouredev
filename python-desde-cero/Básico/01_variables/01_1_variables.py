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

# Variables en una sola lí­nea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(f"Hola {name}, tienes {age} años")

# Cambiamos su tipo
name = 35
age = "Brais"
print("Ahora hemos intercambiado las variables, 'name' = ", name)
print("Y 'age' es = ", age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))