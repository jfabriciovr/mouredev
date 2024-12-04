### Operadores AritmÃ©ticos ###

# Operaciones con enteros
print("Operaciones con enteros")
print(3 + 4) # 7
print(3 - 4) # -1
print(3 * 4) # 12
print(3 / 4) # 0.75
print(10 % 3) # 1
print(10 // 3) # 3 
print(2 ** 3) # 8
print(2 ** 3 + 3 - 7 / 1 // 4) # 10.0

# Operaciones con cadenas de texto
print("Operaciones con cadenas de texto") 
print("Hola " + "Python " + "¿Qué tal?") # Hola Python ¿Qué tal?
print("Hola " + str(5)) # Hola 5

# Operaciones mixtas
print("Hola " * 5) # HolaHolaHolaHolaHola
print("Hola " * (2 ** 3)) # HolaHolaHolaHolaHolaHolaHolaHolaHola

my_float = 2.5 * 2 # 5.0
print("Hola " * int(my_float)) # "Hola " * 5 = HolaHolaHolaHolaHola

### Operadores Comparativos ###

# Operaciones con enteros
print("Operadores con enteros")
print(3 > 4) # False
print(3 < 4) # True
print(3 >= 4) # False
print(4 <= 4) # True
print(3 == 4) # False
print(3 != 4) # True

# Operaciones con cadenas de texto (evalúa por orden alfabético)
print("Operaciones con cadenas de texto")
print("Hola" > "Python") # False
print("Hola" < "Python") # True
print("aaaa" >= "abaa")  # OrdenaciÃ³n alfabÃ©tica por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python") # True
print("Hola" == "Hola") # True
print("Hola" != "Python") # True

### Operadores LÃ³gicos ###

# Basada en el Ãlgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print("Operaciones basadas en Álgebra de Boole")
print(3 > 4 and "Hola" > "Python") # False
print(3 > 4 or "Hola" > "Python")  # False
print(3 < 4 and "Hola" < "Python") # True
print(3 < 4 or "Hola" > "Python") # True
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # True
print(not (3 > 4)) # True