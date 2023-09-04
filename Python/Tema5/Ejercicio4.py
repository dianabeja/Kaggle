def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

print(count_negatives([5, -1, -2, 0, 3]))

def count_negatives(nums):
    return len([num for num in nums if num < 0])

print(count_negatives([5, -1, -2, 0, 3]))
