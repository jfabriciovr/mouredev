# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text)) # 18

# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.
print("Hola" + "Python") # HolaPython

# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
print("Hola\nPython")
# Hola
# Python

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre, apellido, edad = "Fabricio", "Villalobos", 42
print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")
# Mi nombre es Fabricio Villalobos y mi edad es 42

# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.
lenguaje = "python"
letra0, letra1, letra2, letra3, letra4, letra5 = lenguaje
print(letra0, letra1, letra2, letra3, letra4, letra5)
# p y t h o n

# 6. Extrae un slicede la palabra Programaciónpara obtener los caracteres desde la posición 3 hasta la 7.
mi_palabra = "Programación"
print(mi_palabra[3:8])
# gramaci

# 7. Invierte la cadena Python usando slicing y muestra el resultado.
mi_cadena = "Python"
print(mi_cadena[::-1])
# nohtyP

# 8. Convierte la cadena "aprendiendo python"en mayúsculas usando el método adecuado e imprÃ­mela.
mi_cadena = "aprendiendo python" 
print(mi_cadena.upper())
# APRENDIENDO PYTHON

# 9. Cuenta cuántas veces aparece la letra "n"en la cadena "Programación en Python".
mi_cadena = "Programación en Python"
print(mi_cadena.count("n"))
# 2

# 10. Verifica si la cadena "12345"es numérica usando el método adecuado e imprime el resultado.
mi_cadena = "12345" 
print(mi_cadena.isnumeric())
# True