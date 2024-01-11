import random
countries = ['col', 'mex', 'bol', 'pe']
population_v2 = { country: random.randint(1, 100) for country in countries}
print(population_v2)

result = { country: population for country, population in population_v2.items() if population > 20}
print(result)

#ejercicio 2

text = 'Hola, soy Jorge'
unique = {character: character.upper() for character in text if character in 'aeiou'}
print(unique)
