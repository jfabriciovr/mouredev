### LISTAS ###

my_list = list()
my_other_list = []

print(len(my_list)) # 0
print(len(my_other_list)) # 0


my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list) # [35, 24, 62, 52, 30, 30, 17]
print(len(my_list)) # 7

my_other_list = [35, 1.77, "Brais", "Moure"]
print(my_other_list) # [35, 1.77, 'Brais', 'Moure"]
print(type(my_other_list)) # <class 'list'>
print(my_other_list[0]) # 35
print(my_other_list[1]) # 1.77
print(my_other_list[-1]) # "Moure" es el último elemento
print(my_other_list[-4]) # 35 es el primer elemento
#print(my_other_list[-5]) IndexError
#print(my_other_list[4]) IndexError
print(my_other_list.count("Brais")) # 1 es el número de ocurrencias de un valor


