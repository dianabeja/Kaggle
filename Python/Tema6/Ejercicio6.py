def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return len(zip_code) == 5 and zip_code.isdigit()
# Check your answer
print(is_valid_zip("12345"))