#Strings are sequences

# Indexing
planet = 'Pluto'
print(planet[0])
# Slicing
print(planet[-3:])
# How long is this string?
print(len(planet))

# Yes, we can even loop over them
print([char+'! ' for char in planet])

planet[0] = 'B'
# planet.append doesn't work either
print(planet)