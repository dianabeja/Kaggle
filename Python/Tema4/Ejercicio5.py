def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None
    return L[1]

# Check your answer

L=[1,2,3,4,5,6,7,8,9]
print(select_second(L))