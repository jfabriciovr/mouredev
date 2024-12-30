### Conditionals ###

# if

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condiciÃ³n del if")

my_condition = 5 * 5 # 25

if my_condition == 10: # false, por lo que no se ejecuta este código
    print("Se ejecuta la condiciÃ³n del segundo if")
# if, elif, else
if my_condition > 10 and my_condition < 20: # false, por lo que no se ejecuta este código
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25: # true, y este código sí se ejecuta.
    print("Es igual a 25")
else: # este código es ignorado ya que se cumplió el código anterior
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

# Condicional con ispección de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacÃ­a")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")