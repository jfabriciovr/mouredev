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


