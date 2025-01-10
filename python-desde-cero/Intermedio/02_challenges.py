### challenges ###

'''
EL FAMOSO "FIZZ BUZZ"

Escribe un programa que muestre por consola (con un print) los
números del 1 al 100 (abos incluídos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:

- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

'''
print("*** FIZZ BUZZ ***")
def fizzbuzz():
    for index in range(1,101):
        if index % 3 == 0 and index % 5 == 0: # tenemos que empezar con esta condición porque es el más restrictivo. Si no, va a entrar primero en el caso de que sea múltiplo de 3 o el de 5 pero no va a llegar a evaluar el caso donde sea múltiplo de los dos
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()

"""
ANAGRAMA

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.

- Un anagrama consiste en formar una palabra reordenando TODAS 
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

print("*****  ANAGRAMA ******")
print("la función sorted ordena un string y lo guarda como una lista: ")
print("'bdac'")
print(sorted("bdac")) # ['a', 'b', 'c', 'd']

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower()) # primero lower convierte a minúsculas y luego ordena las palabras y finalmente las compara

print(is_anagram("omar", "Roma")) # True


"""
******* FIBONACCI *********

Escribe un programa que imprima los 50 primeros números de la serie de Fibonacci empezando en 0

- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la SUMA DE LOS DOS ANTERIORES.

0, 1, 1, 2, 3, 5, 8, 13 ...

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) para n > 1

"""
print("*** FIBONACCI ***")

def fibonacci(num_terms):
    prev = 0
    next = 1

    for index in range(num_terms):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci(8)

# método recursivo no es eficiente para números grandes, arriba de 30 ya se empieza a trabar
def fibonacci_recursive(n):
    if n <= 1:
        return n # base case: F(0) = 0, F(1) = 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for i in range(8):
    print(fibonacci_recursive(i))

# método iterativo chatgpt
def fibonacci_iterative(num_t):
    if num_t <= 0:
        return 0
    elif num_t == 1:
        return 1
    
    a, b = 0, 1 # initialize the first two Fibonacci numbers
    for _ in range(2, num_t + 1):
        a, b = b, a + b # update a and b to the next two Fibonacci numbers
    
    return b

for i in range(8):
    print(fibonacci_iterative(i))


"""
ES NUMERO PRIMO

escribe un programa que se encargue de comprobar si un número es o no primo.
hecho esto, imprime los números primos enre 1 y 100

Un número primo es un número natural (mayor a 1) que solo es divisible por sí mismo y por el 1

"""

print("** numeros primos ***")

def is_prime(number):
    if number < 2:
        return False
    for i in range (2, number):
        if number % i == 0:
            return False
    return True


def print_primes(first, last):
    for i in range(first, last+1):
        if is_prime(i):
            print(i)


# función que imprime los números primos del 1 al 100
print_primes(1, 100) 

    
"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática
- si le pasamos "hola mundo" nos retornaría "odnum aloh"

"""
print("invierte cadenas")

def invierte(texto):
    print("texto original: ", texto)
    print("texto invertido: ")
    
    texto_invertido = ""
    text_len = len(texto)

    for i in range(0, text_len):
        texto_invertido += texto[text_len - i-1]
        
    print(texto_invertido)
        


invierte("hola mundo")








