### Files Handling ###
import os

txt_file = open("python-desde-cero/Intermedio/my_file.txt", "w+") # w+ es para escribir, si el archivo no existe, lo crea
txt_file.write("Mi nombre es Brais\nMi apellido es Moure\n35 años\nMi lenguaje favorito es python")

# Lee todo el archivo
# print(txt_file.read(10))

# Leer una candidad de caracteres solamente:
# print(txt_file.read())

# Leer lina a línea
#print(txt_file.readlines()) # guarda cada linea en un elemento de una lista: ['Mi nombre es Brais\n', 'Mi apellido es Moure\n', '35 años\n', 'Y mi lenguaje preferido es Python\n', '\n']

# como readLines() guarda una lista, se puede iterar a través de ella
for line in txt_file.readlines():
    print(line)

"""
Mi nombre es Brais

Mi apellido es Moure

35 años

Y mi lenguaje preferido es Python
"""
txt_file.write("\nAunque también me gusta kotlin")

txt_file.close()

with open("python-desde-cero/Intermedio/my_file.txt", "a") as my_other_file: # se crea un alias para el nombre del archivo
    my_other_file.write("\nY swift")

my_other_file.close()

txt_file = open("python-desde-cero/Intermedio/my_file.txt", "r+") # w+ es para escribir, si el archivo no existe, lo crea
print(txt_file.read())
txt_file.close()

#os.remove("python-desde-cero/Intermedio/my_file.txt")

# @@@@@@@@@@@@@@@@@@@@@@@@@@
## .jason file
# @@@@@@@@@@@@@@@@@@@@@@@@@

import json

json_file = open("python-desde-cero/Intermedio/my_file.json", "w+")

json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "language": "Python",
    "website": "https://moure.dev"
}

json.dump(json_test, json_file, indent=2)

json_file = open("python-desde-cero/Intermedio/my_file.json", "r+")

#print(json_file.readlines())
"""
['{\n', '  "name": "Brais",\n', '  "surname": "Moure",\n', '  "age": 35,\n', '  "language": "Python",\n', '  "website": "https://moure.dev"\n', '}']

"""

for line in json_file.readlines():
    print(line)
"""
{

  "name": "Brais",

  "surname": "Moure",

  "age": 35,

  "language": "Python",

  "website": "https://moure.dev"

"""

json_file.close()

print("se vuelve a imprimir el json con un alias:")
with open("python-desde-cero/Intermedio/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

print(type(my_other_file)) # <class '_io.TextIOWrapper'>

print("convertir el json a dict para poderlo manipular")
json_dict = json.load(open("python-desde-cero/Intermedio/my_file.json"))
print(type(json_dict)) #  <class 'dict'>
print(json_dict) # {'name': 'Brais', 'surname': 'Moure', 'age': 35, 'language': 'Python', 'website': 'https://moure.dev'}

print("ahora ya como diccionario, podemos acceder un valor:")
print(json_dict["name"]) # Brais
json_file.close()


# @@@@@@@@@@@@@@@@@@@@@@@@@@
## .csv file
# @@@@@@@@@@@@@@@@@@@@@@@@@

import csv

data = [
    ["Name", "Age", "Email"], 
    ["Alice", 30, "alice@gmail.com"]
]
file_name = "python-desde-cero/Intermedio/my_file.csv"

with open(file_name, "w") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Leer el archivo 
# 3 maneras de hacerlo
with open(file_name) as file:
    print(file.read())

with open(file_name) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open(file_name) as file:
    for line in file.readlines():
        print(line)

# @@@@@@@@@@@@@@@@@@@@@@@@@@
## .xml file
# @@@@@@@@@@@@@@@@@@@@@@@@@
import xml
