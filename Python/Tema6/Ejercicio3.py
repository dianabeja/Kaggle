#String methods

planet = 'Pluto'
# ALL CAPS
claim = "Pluto is a planet!"
print(claim.upper())
# all lowercase
print(claim.lower())

# Searching for the first index of a substring
print(claim.index('plan'))
print(claim.startswith(planet))

# false because of missing exclamation mark
print(claim.endswith('planet'))

#Going between strings and lists: .split() and .join()
words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')

print('/'.join([month, day, year]))
print(' 👏 '.join([word.upper() for word in words]))

print(planet + ', we miss you.')
position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")