## Modules
'''
Los módulos en Python son archivos con extensión .py que contienen funciones, variables, clases 
y sentencias ejecutables. Permiten organizar el código de manera lógica y reutilizar código. 

Para importar un módulo, se puede hacer desde otro archivo de Python ubicado en la misma ruta. 
El nombre del módulo debe corresponder con el nombre del archivo. 

Algunos ejemplos de módulos en Python son: 

- datetime: Permite trabajar con fechas y horas, con métodos como now(), datetime() y today()
- numbers: Define una jerarquía abstracta de tipos numéricos
- math: Contiene funciones matemáticas para números complejos
- cmath: Contiene funciones matemáticas para números complejos
- decimal: Permite representaciones exactas de números decimales
'''

import module # importa todo el contenido de module.py
module.sum_three_values(2, 3, 45) # necesitamos escribir module y punto para acceder a alguna función


from module import sum_three_values # aquí sólo importamos una función en particular que está dentro del archivo modules.py
sum_three_values(4, 54, 32) # aquí no es necesario anteponer la palabra "module" porque ya estamos importando una función en particular


# Módulos de Python que no tenemos acceso por default
# pero que podemos importar cuando se requiera

import math

print(math.factorial(6)) # 720
print(math.pi) # 3.1415...
print(math.pow(2, 8)) # 2 elevado a la 8 potencia

# Aplicar un alias a una función
from math import pi as PI_VALUE
print(PI_VALUE) # 3.1415...









