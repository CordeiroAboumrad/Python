import random

possible_outcomes = (0, 1)
distribution = (0.3, 0.7)

contador_0 = 0
contador_1 = 0
for x in range(0, 100):
    random_number = random.choices(possible_outcomes, distribution)
    print(random_number)
    if random_number[0] == 0:
        contador_0 += 1
    else:
        contador_1 += 1

print(f"quantidade de 0's: {contador_0}\nquantidade de 1's: {contador_1}")
