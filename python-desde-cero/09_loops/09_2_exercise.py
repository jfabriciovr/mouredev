# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.
print("ejercicio 1. imprime los números del 1 al 10")
num = 1
while num <= 10:
    print(num)
    num+=1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.
print("ejercicio 2. imprime los elementos de una lista")
my_list = [10, 20, 30, 40, 50]
for element in my_list:
    print(element)

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.
print("ejercicio 3.")
num = 1
resultado = 0
while num <= 100:
    resultado = resultado + num # resultado += num
    num+=1
else: 
    print(f'la suma de los números del 1 al 100 es: {resultado}')

# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".
print("ejercicio 4.")
cadena = "Python"
for element in cadena:
    print(element)

# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.
print("ejercicio 5.")
num = 1
while num <= 50:
    if num % 7 == 0:
        print(f'el primer número divisible entre 7 es {num}')
        break
    else:
        num+=1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
print("ejercicio 6.")
my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
for element in my_dict:
    print(element)

# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.
print("ejercicio 7. números pares entre 1 y 20.")
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.
print("ejercicio 8. imprime los números del 10 al 1")
for num in range(10):
    print(10-num)

''' otra forma es:

for num in range(10, 0, -1):
    print(num)

'''

# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la 
# lista[30, 10, 30, 20, 30, 40].
print("ejercicio 9. ¿cuántas veces aparece el número 30 en la lista: [30, 10, 30, 20, 30, 40]?")
my_list = [30, 10, 30, 20, 30, 40]
contador = 0
for element in my_list:
    if element == 30:
        contador+=1

print(f'el número 30, aparece {contador} veces.')

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
print("ejercicio 10.")
my_list_of_names = ["Fabricio", "José", "Brais", "Alfredo"]
for name in my_list_of_names:
    print(name)
    if name == "Brais":
        break
