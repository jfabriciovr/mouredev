# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
my_dict = {"name": "Juan", "age": 34, "country": "EEUU"}
print(my_dict)

# 2. Accede al valor de la clave name en el diccionario.
print(my_dict["name"]) # Juan

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
my_dict["job"] = "Programador"
print(my_dict) # {'name': 'Juan', 'age': 34, 'country': 'EEUU', 'job': 'Programador'}


# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
my_dict["age"] = 38
print(my_dict) # {'name': 'Juan', 'age': 38, 'country': 'EEUU', 'job': 'Programador'}


# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del my_dict["country"]
print(my_dict) # {'name': 'Juan', 'age': 38, 'job': 'Programador'}

# 6. Crea un diccionario donde las claves sean nÃºmeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
squares = {x: x**2 for x in range(1, 6)}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 7. Verifica si la clave age estÃ¡ presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
my_dict = {"name":"Brais", "age":37, "country":"Galicia"}
print("age" in my_dict) # True

# 8. Imprime solo las claves del diccionario.
print(my_dict.keys()) # dict_keys(['name', 'age', 'country'])

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
print(list(my_dict.keys())) # ['name', 'age', 'country']

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
my_keys = ["name", "age", "job"]
my_new_dict = dict.fromkeys(my_keys, "Desconocido")
print(my_new_dict) # {'name': 'Desconocido', 'age': 'Desconocido', 'job': 'Desconocido'}

