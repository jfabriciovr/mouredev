### Regular Expressions ###

# liga útil para crear patrones de expresiones regulares
# https://regex101.com


import re # módulo para expresiones regulares

### Match ###
# busca en el inicio de un string
my_string = "Esta es la Lección número 7: lección para usar Expresiones Regulares"
### para cuando si hay un match
match = re.match("Esta es la lección", my_string, re.I) # "texto a buscar", en cual string
if match is not None: # cuando hay un error con el match, regresa 'None', entonce esta if es que entre al bloque CUANDO NO HAY ERROR
    print(match) # <re.Match object; span=(0, 18), match='Esta es la lección'>
    print(match.span()) # (0, 18)
    inicio, fin = match.span() # como regresa una tupla, se puede guardar en dos variables
    print(my_string[inicio:fin]) # Esta es la lección


### Serch ####
# busca en cualquier parte de un string
search = re.search("lección", my_string, re.I) # el flag re.I es para que no importe si hay mayúsculas o minúsculas
print(search) # <re.Match object; span=(11, 18), match='lección'>
inicio, fin = search.span() 
print(my_string[inicio:fin]) # lección

### Findall ###
# guarda en una lista todas las veces que encuentra el string
findall = re.findall("lección", my_string, re.I)
print(findall)  # ['lección', 'lección']

### Split ###
# separa en elementos de una lista a partir de un texto o símbolo
print(re.split(":", my_string)) # ['Esta es la lección número 7', ' lección para usar Expresiones Regulares']


### Sub ###
# sustituye un texto con otro
print(re.sub("Expresiones Regulares", "RegEx", my_string)) # Esta es la lección número 7: lección para usar RegEx

print(re.sub("lección|Lección", "LECCIÓN", my_string)) # Esta es la LECCIÓN número 7: LECCIÓN para usar Expresiones Regulares
print(re.sub("[l|L]ección", "LECCIÓN", my_string)) # esta es otroa manera de escribir la instrucción anterior

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### Usando patrones personalizados para Expresiones Regulares
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

my_string = "Esta es la Lección número 7: lección para usar Expresiones Regulares"

print(re.findall("[lL]ección", my_string))
patron = r"[lL]ección"
print(re.findall(patron, my_string)) # ['Lección', 'lección']

patron = r"[lL]ección|Expresiones"
print(re.findall(patron, my_string)) # ['Lección', 'lección', 'Expresiones']
print(re.match(patron, my_string)) # None

patron = r"[0-9]"
print(re.findall(patron, my_string)) # ['7']
print(re.search(patron, my_string)) # <re.Match object; span=(26, 27), match='7'>

# email validation 
my_string = "regex@example.net.edu"
patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.findall(patron, my_string)) # ['regex@example.net.edu']
print(re.match(patron, my_string)) # <re.Match object; span=(0, 21), match='regex@example.net.edu'>
print(re.search(patron, my_string)) # <re.Match object; span=(0, 21), match='regex@example.net.edu'>









