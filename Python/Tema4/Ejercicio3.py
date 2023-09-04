#List methods

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# Pluto is a planet darn it!
planets.append('Pluto')
help(planets.append)
print(planets)
planets.pop()
print(planets)
#Searching lists
print(planets.index('Earth'))

# Is Earth a planet?
print("Earth" in planets)

# Is Calbefraques a planet?
print("Calbefraques" in planets)

help(planets)

