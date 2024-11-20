# Extended Functions for string operations

def str_reverse(s):
    """Reverses the input string."""
    return s[::-1]

def str_to_upper(s):
    """Converts the input string to uppercase."""
    return s.upper()

def str_to_lower(s):
    """Converts the input string to lowercase."""
    return s.lower()

def str_is_palindrome(s):
    """Checks if the input string is a palindrome."""
    return s == str_reverse(s)

def str_count_occurrences(s, substring):
    """Counts occurrences of a substring in the input string."""
    return s.count(substring)

def str_is_alpha(s):
    """Checks if the string contains only alphabetic characters."""
    return s.isalpha()

def str_is_digit(s):
    """Checks if the string contains only digits."""
    return s.isdigit()

def str_find_substring(s, substring):
    """Finds the first occurrence of a substring in the input string."""
    return s.find(substring)

def str_replace_substring(s, old, new):
    """Replaces occurrences of a substring with another substring."""
    return s.replace(old, new)

def str_split_words(s):
    """Splits the string into words."""
    return s.split()

def str_strip_spaces(s):
    """Removes leading and trailing spaces from the string."""
    return s.strip()

def str_startswith(s, prefix):
    """Checks if the string starts with a specific prefix."""
    return s.startswith(prefix)

def str_endswith(s, suffix):
    """Checks if the string ends with a specific suffix."""
    return s.endswith(suffix)

def str_isalnum(s):
    """Checks if the string contains only alphanumeric characters."""
    return s.isalnum()

def str_isdigit(s):
    """Checks if the string contains only digits."""
    return s.isdigit()

def str_title_case(s):
    """Converts the string to title case."""
    return s.title()

def str_find_substring(s, substring):
    """Finds the first occurrence of a substring."""
    return s.find(substring)

def str_concat(s1, s2):
    """Concatenates two strings."""
    return s1 + s2

def str_join(separator, iterable):
    """Joins the elements of an iterable into a single string with a separator."""
    return separator.join(iterable)
