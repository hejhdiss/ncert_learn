def str_reverse(s):
    """Reverses the input string."""
    try:
        return s[::-1]
    except Exception as e:
        return False

def str_to_upper(s):
    """Converts the input string to uppercase."""
    try:
        return s.upper()
    except Exception as e:
        return False

def str_to_lower(s):
    """Converts the input string to lowercase."""
    try:
        return s.lower()
    except Exception as e:
        return False

def str_is_palindrome(s):
    """Checks if the input string is a palindrome."""
    try:
        return s == str_reverse(s)
    except Exception as e:
        return False

def str_count_occurrences(s, substring):
    """Counts occurrences of a substring in the input string."""
    try:
        return s.count(substring)
    except Exception as e:
        return False

def str_is_alpha(s):
    """Checks if the string contains only alphabetic characters."""
    try:
        return s.isalpha()
    except Exception as e:
        return False

def str_is_digit(s):
    """Checks if the string contains only digits."""
    try:
        return s.isdigit()
    except Exception as e:
        return False

def str_find_substring(s, substring):
    """Finds the first occurrence of a substring in the input string."""
    try:
        return s.find(substring)
    except Exception as e:
        return False

def str_replace_substring(s, old, new):
    """Replaces occurrences of a substring with another substring."""
    try:
        return s.replace(old, new)
    except Exception as e:
        return False

def str_split_words(s):
    """Splits the string into words."""
    try:
        return s.split()
    except Exception as e:
        return False

def str_strip_spaces(s):
    """Removes leading and trailing spaces from the string."""
    try:
        return s.strip()
    except Exception as e:
        return False

def str_startswith(s, prefix):
    """Checks if the string starts with a specific prefix."""
    try:
        return s.startswith(prefix)
    except Exception as e:
        return False

def str_endswith(s, suffix):
    """Checks if the string ends with a specific suffix."""
    try:
        return s.endswith(suffix)
    except Exception as e:
        return False

def str_isalnum(s):
    """Checks if the string contains only alphanumeric characters."""
    try:
        return s.isalnum()
    except Exception as e:
        return False

def str_title_case(s):
    """Converts the string to title case."""
    try:
        return s.title()
    except Exception as e:
        return False

def str_concat(s1, s2):
    """Concatenates two strings."""
    try:
        return s1 + s2
    except Exception as e:
        return False

def str_join(separator, iterable):
    """Joins the elements of an iterable into a single string with a separator."""
    try:
        return separator.join(iterable)
    except Exception as e:
        return False
