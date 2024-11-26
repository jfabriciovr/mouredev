# 1. Imprime "Â¡Hola Mundo!" por consola.

# 2. Escribe un comentario de una sola lÃ­nea explicando quÃ© hace el cÃ³digo del Ejercicio 1.

# 3. Imprime tu nombre y edad en la misma lÃ­nea utilizando la funciÃ³n print.

# 4. Usa la funciÃ³n type() para imprimir el tipo de dato de una cadena de texto, un nÃºmero entero y un nÃºmero decimal.

# 5. Escribe un comentario en varias lÃ­neas explicando quÃ© son los tipos de datos en Python.

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma lÃ­nea.

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.

# 9. Usa print() para mostrar el resultado de la suma de dos nÃºmeros enteros y el tipo de dato resultante.

# 10. Comenta el cÃ³digo del Ejercicio 9, y explica quÃ© hace cada lÃ­nea usando comentarios de una sola lÃ­nea.

# ---------------- SOLUCION ------------

# 1
print("!Hola Mundo¡")

# 2
# Este código imprime Hola Mundo en la consola

# 3
print("Mi nombre es Fabricio y tengo 41 años")

# 4
print(type("cadena de texto"))
print(type(123))
print(type(1.5))

# 5
"""
Los tipos de datos en python son la manera de clasificar los la información que se recibe, almacen, procesa y se muestra como reaultado en la pantalla
Estos tipos de datos pueden ser:
- Int: Entero
- Float: Número decimal
- String: Cadena de texto
- Boolean: Verdadero o Falso
- List: Colección de elementos
- Tuple: Colección de elementos inmutables
- Dictionary: Colección de elementos con clave y valor
- Set: Colección de elementos sin orden

Saber los tipos de datos nos ayuda a saber cómo pueden interactuar entre ellos para llegar a un resultado deseado

"""
# 6
print("Hola" + "Mundo")

# 7
nombre = "Fabricio"
edad = 41
print(f"Mi nombre es {nombre} y tengo {edad} años")

# 8
nombre_usuario = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre_usuario}")

# 9
num1 = 10
num2 = 20
print(num1 + num2)
print(type(num1 + num2))

# 10
# print(num1 + num2) # Imprime la suma de dos números enteros
# print(type(num1 + num2)) # Imprime el tipo de dato resultante de la
# suma de dos números enteros

