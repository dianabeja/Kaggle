def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    nombre=arrivals.index(name)
    return nombre >= len(arrivals) / 2 and nombre != len(arrivals) - 1

# Check your answer
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
print(fashionably_late(party_attendees,"Fleda"))
print(fashionably_late(party_attendees,"Mona"))