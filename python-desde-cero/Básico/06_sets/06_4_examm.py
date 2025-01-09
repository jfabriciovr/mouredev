# ¿Qué características tienen los sets?
# No permiten los duplicados

# ¿Cómo se crea un set vacío en Python?
# set()

# ¿Qué operación se usa para eliminar un elemento de un set?
# remove()

# ¿Qué resultado tiene?
set1 = {1, 2}
set2 = {2, 3}
print(set1.union(set2))
# {1, 2, 3}

# ¿Cómo verificas si un elemento está en un set?
# Elemento in set

# ¿Cómo puedo convertir un set en una lista?
# list(set)

# ¿Qué ocurre si intentas agregar un elemento ya existente a un set?
# No se añade el duplicado

# ¿Qué operación devuelve la diferencia entre dos sets?
# difference()

# ¿Cuál es la salida?
print(len({1, 2, 3, 3, 4}))
# 4

# ¿Qué sucede si intentas acceder a un elemento de un set mediante índice?
# Da un error