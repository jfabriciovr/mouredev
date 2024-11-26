# 1. Imprime "Â¡Hola Mundo!" por consola.

print("Â¡Hola Mundo!")

# 2. Escribe un comentario de una sola lÃ­nea explicando quÃ© hace el cÃ³digo del Ejercicio 1.

# Este cÃ³digo imprime "Â¡Hola Mundo!" por consola.

# 3. Imprime tu nombre y edad en la misma lÃ­nea utilizando la funciÃ³n print.

print("Mi nombre es Brais y tengo", 37, "aÃ±os.")

# 4. Usa la funciÃ³n type() para imprimir el tipo de dato de una cadena de texto, un nÃºmero entero y un nÃºmero decimal.

print(type("Brais"))  # str
print(type(37))       # int
print(type(3.14))     # float

# 5. Escribe un comentario en varias lÃ­neas explicando quÃ© son los tipos de datos en Python.

"""
En Python, los tipos de datos mÃ¡s comunes son:
- str: para cadenas de texto
- int: para nÃºmeros enteros
- float: para nÃºmeros con decimales
- bool: para valores booleanos (True/False)
"""

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".

print("Hola" + " " + "Mundo")

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma lÃ­nea.

my_name = "Brais"
my_age = 37
print("Mi nombre es", my_name, "y tengo", my_age, "aÃ±os.")

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.

user_name = input("Â¿CuÃ¡l es tu nombre? ")
print("Â¡Hola", user_name + "!")

# 9. Usa print() para mostrar el resultado de la suma de dos nÃºmeros enteros y el tipo de dato resultante.

result = 5 + 10
print("El resultado es:", result)
print("El tipo de dato del resultado es:", type(result))

# 10. Comenta el cÃ³digo del Ejercicio 9, y explica quÃ© hace cada lÃ­nea usando comentarios de una sola lÃ­nea.

# Suma dos nÃºmeros enteros.
result = 5 + 10

# Imprime el resultado de la suma.
print("El resultado es:", result)

# Imprime el tipo de dato del resultado, que es 'int'.
print("El tipo de dato del resultado es:", type(result))