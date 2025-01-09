### Strings ###

my_string = "Mi String"
my_other_string = "Mi otro String"

# len() cuenta los caracteres incluyendo espacios
print(len(my_string)) # 9
print(len(my_other_string)) # 14

print(my_string + " " + my_other_string) # Mi String Mi otro String

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string) 
# Este es un string 
# con salto de línea

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)
#       Este es un string con tabulación

my_scape_string = "\\t Este es un string \\n escapado" # \t Este es un string \n escapado
print(my_scape_string)

name, surname, age = "Fabricio", "Villalobos", 42
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # inferencia de datos
# Mi nombre es Fabricio Villalobos y tengo 42 años
# Mi nombre es Fabricio Villalobos y tengo 42 años
# Mi nombre es Fabricio Villalobos y tengo 42 años
# Mi nombre es Fabricio Villalobos y tengo 42 años

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a, b, c, d, e, f) # P y t h o n
print(language[0]) # P

# División
print(language[1:3]) # yt
print(language[1:]) # ython
print(language[1:2:4]) # y
print(language[-1]) # n
print(language[-2]) # o

# Reverse
print(language[::-1]) # nohtyP

# Funciones

print("python".capitalize()) # Python
print(language.upper()) # PYTHON
print(language.upper().isupper()) # True
print(language.lower()) # python
print(language.count("t")) # 1
print(language.isnumeric()) # False
print(language.startswith("Py")) # True