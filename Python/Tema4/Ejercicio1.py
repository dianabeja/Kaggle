#Lists
primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]
my_favourite_things = [32, 'raindrops on roses', help]

print("1",primes)
print("\n2",planets)
print("\n3",hands)
print("\n4",my_favourite_things)

#Indexing
print("Indexing")
print("\n",planets[0])
print("\n",planets[1])
print("\n",planets[-1])
print("\n",planets[-2])

#Slicing
print("\n",planets[0:3])
print("\n",planets[:3])
print("\n",planets[3:])

# All the planets except the first and last
print("\n",planets[1:-1])

# The last 3 planets
print("\n",planets[-3:])

#Changing lists
planets[3] = 'Malacandra'
print("\n",planets)

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

#List functions
print("\n",len(planets))

# The planets sorted in alphabetical order
print("\n",sorted(planets))

primes = [2, 3, 5, 7]
print("\n",sum(primes))

print("\n",max(primes))
