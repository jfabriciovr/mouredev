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