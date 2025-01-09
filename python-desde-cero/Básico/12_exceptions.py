### Exception Handling ###
# Manejo de errores

try: 
    #print(1 + "1")
    print(1 + 1)
except:
    print("Except: se ha producido un error")
else:
    print("Else: se ejecuta si no se produce una excepción")
finally:
    print("Finaly: se ejecuta siempre")

'''
Escepciones sólo cuando es un tipo de error en específico:

except: TypeError
except: ValueError
'''
try: 
    print(1 + "1") # aquí el tipo de error es TypeError
except TypeError:
    print("Except: se ha producido un error TypeError") # este si se ejecuta
except ValueError: 
    print("Except: se ha producido un error ValueError") # este no se ejecuta
else:
    print("Else: se ejecuta si no se produce una excepción")
finally:
    print("Finaly: se ejecuta siempre")

## Captura de la información de la excepción
# arroja el error de sistema pero lo guardamos en una variable
# de esta manera guardamos la información detallada del error
try: 
    print(1 + "1")
except ValueError as error:
    print(error)
except Exception as excepcion: # se ejecuta esta opción porque es un TypeError y sólo teníamos ValueError anteriormente
    print(excepcion)








