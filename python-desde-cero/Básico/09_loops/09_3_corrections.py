# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.

i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.

numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".

word = "Python"
for letter in word:
    print(letter)

# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.

i = 1
while i <= 50:
    if i % 7 == 0:
        print(i)
        break
    i += 1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.

person = {"name": "Brais", "age": 37, "country": "Galicia"}
for key in person:
    print(key)

# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.

for i in range(10, 0, -1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la lista[30, 10, 30, 20, 30, 40].

list = [30, 10, 30, 20, 30, 40]
counter = 0
for number in list:
    if number == 30:
        counter += 1
print(counter)

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".

names = ["Sara", "Brais", "Pedro"]
for name in names:
    if name == "Brais":
        print("Se encontrÃ³ a Brais")
        break
    print(name)