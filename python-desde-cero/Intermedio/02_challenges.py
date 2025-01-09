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

"""
def anagrama(palabra1, palabra2):
    if palabra1 != palabra2:
        for letra1 in palabra1:
            for letra2 in palabra2:
                if letra2 != letra1:
                    break
                
    else:
        print("no es un anagrama")
"""

""" 
def is_anagram(word_one, word_two):
    
    #if word_one.lower() == word_two.lower(): # dos palabras iguales no son anagrama
     #   return "son iguales, no es un anagrama"
    
    return word_one == word_two

print(is_anagram("Amor", "Roma"))
"""  
print(sorted("bdac")) # ['a', 'b', 'c', 'd']

def is_anagram(word_one, word_two):
    print(sorted(word_one.lower()) == sorted(word_two.lower()))

is_anagram("Amor", "Roma")

