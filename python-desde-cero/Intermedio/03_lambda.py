## lambdas ###

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

def sum_three_values(valor):
    return lambda first_value, second_value: first_value + second_value + valor

print(sum_three_values(5)(2, 3))

