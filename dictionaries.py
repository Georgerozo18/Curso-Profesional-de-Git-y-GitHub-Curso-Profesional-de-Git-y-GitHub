# dict comprehension

# Ejercicio 1
dict = {}

for i in range(1, 5):
    dict[i] = i * 2
print(dict)

# sintaxis corta
dict_v2 = { i: i * 2 for i in range(1, 5)} 
print(dict_v2)

# Ejercicio 2
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)

# sintaxis corta
population_v2 = { country: random.randint(1, 100) for country in countries}
print(population_v2)

# Ejercicio 3
names = ['jorge', 'fernanda', 'sandra']
ages = [12, 56, 98]
print(list(zip(names, ages)))

new_dict = {names: age for (names, age) in zip(names, ages)}
print(new_dict)