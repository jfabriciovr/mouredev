# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
num = -7
if num > 0:
    print(f'{num} Es positivo')
elif num == 0:
    print(f'{num} es igual a cero')
else:
    print(f'{num} es negativo')

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
edad = int(input("introduce tu edad: "))
if edad >= 18:
    print("eres mayor dedad")
else:
    print("eres menor de edad")

# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.
texto = input("Ecribe algo o sólo presiona Enter: ")
if not texto:
    print("La cadena de texto está vacía")
else:
    print(f'La texto que escribiste es: {texto}')

# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. 
# Si son iguales, muestra un mensaje indicando la igualdad.
num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe otro número: "))

if num1 > num2:
    print(f'{num1} es mayor que {num2}')
elif num1 < num2:
    print(f'{num1} es menor a {num2}')
else:
    print(f'{num1} y {num2} son iguales')

# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.
num = int(input("Escribe un número: "))
if num%3 == 0 and num%5 ==0:
    print(f'{num} es divisible entre 3 y 5')
else:
    print(f'{num} NO ES divisible entre 3 y 5 al mismo tiempo')


# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.
num = int(input("Escribe un número: "))
if num % 2 == 0:
    print(f'{num} es par')
else:
    print(f'{num} es impar')

# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). 
# Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.
age = int(input("¿Cuántos años tienes?: "))
if age >= 18:
    print("puedes votar")
elif 16 <= age < 18:
    print("necesitas un permiso especial para votar")
else:
    print("no puedes votar")

# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida.
# Si no coincide, muestra un mensaje de error.
password = "password"
user_password = input("Escribe la contraseña correcta para ingresar: ")
if user_password == password:
    print("Acceso permitido")
else:
    print("Acceso denegado")

# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).
numero = int(input("escribe un número: "))
if 10 <= numero <= 20:
    print(f'{numero} está entre 10 y 20')
else:
    print(f'{numero} no está entre 10 y 20')


# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) 
# y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
user_color = input("Escribe rojo, amarillo o verde: ")
if user_color == "rojo":
    print("Debes detenerte")
elif user_color == "amarillo":
    print("precaución")
elif user_color == "verde":
    print("puedes avanzar")
else:
    print("color no válido")

