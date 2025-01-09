# 1. Declara y asigna valores a las siguientes variables:
# â€¢	name: una cadena que contenga tu nombre.
# â€¢	age: un número entero que represente tu edad.
# â€¢	height: un número flotante que represente tu altura.
# â€¢	Imprime cada variable en una lÃ­nea separada.

name = "Fabricio Villalobos"
age = 41
height = 1.75
print("Nombre: ", name)
print("Edad: ", age)
print("Altura: ", height)

# 2. Convierte la variable edad de entero a cadena y concatena la con un texto que diga cuántos años tienes.
age = str(age)
print("Tengo", age, "años")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprí­mela.
is_student = False
print("Soy estudiante: ", is_student)

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
name_lenght = len(name)
print("Tengo", name_lenght, "caracteres en mi nombre")

# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
first_name, sur_name, city_of_origin =  "Fabricio", "Villalobos", "Jalisco"
print("Nombre: ", first_name)
print("Apellido: ", sur_name)
print("Ciudad de origen: ", city_of_origin)

# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.
color = input("¿Cuál es tu color favorito?: ")
print("Tu color favorito es:", color)

# 7. Declara una variable fruit e inicialí­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "manzana"
print(fruit)
fruit = "fresa"
print(fruit)

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego impri­melo.
price = 10.99
price = int(price)
print("Precio:", price)
print(type(price))

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
address = "Calle 123, Colonia 456, Ciudad 789"
address_len = len(address)
print("La dirección tiene", address_len, "caracteres")

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre serÃ¡ un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone: int = 1234567890
print(type(phone))
phone = 9898787676
print(type(phone))
