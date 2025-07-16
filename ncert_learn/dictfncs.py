def dict_add_key_value(d, key, value):
    """Adds a key-value pair to the dictionary."""
    try:
        d[key] = value
        return d
    except Exception as e:
        return False

def dict_remove_key(d, key):
    """Removes a key-value pair from the dictionary."""
    try:
        if key in d:
            del d[key]
            return d
        return False
    except Exception as e:
        return False

def dict_get_value(d, key):
    """Gets the value for a given key in the dictionary."""
    try:
        return d.get(key, None)
    except Exception as e:
        return False

def dict_update_value(d, key, value):
    """Updates the value of an existing key in the dictionary."""
    try:
        if key in d:
            d[key] = value
            return d
        return False
    except Exception as e:
        return False

def dict_contains_key(d, key):
    """Checks if the dictionary contains a specific key."""
    try:
        return key in d
    except Exception as e:
        return False

def dict_get_all_keys(d):
    """Returns a list of all keys in the dictionary."""
    try:
        return list(d.keys())
    except Exception as e:
        return False

def dict_get_all_values(d):
    """Returns a list of all values in the dictionary."""
    try:
        return list(d.values())
    except Exception as e:
        return False

def dict_clear(d):
    """Clears all key-value pairs from the dictionary."""
    try:
        d.clear()
        return d
    except Exception as e:
        return False

def dict_copy(d):
    """Returns a shallow copy of the dictionary."""
    try:
        return d.copy()
    except Exception as e:
        return False

def dict_items(d):
    """Returns a list of all key-value pairs as tuples."""
    try:
        return list(d.items())
    except Exception as e:
        return False

def dict_pop_item(d, key):
    """Removes and returns the value for a specified key."""
    try:
        return d.pop(key, None)
    except Exception as e:
        return False

def dict_update(d, other_dict):
    """Updates the dictionary with another dictionary's key-value pairs."""
    try:
        d.update(other_dict)
        return d
    except Exception as e:
        return False

def dict_setdefault(d, key, default=None):
    """Returns the value of the key if it exists, otherwise inserts the key with the default value."""
    try:
        return d.setdefault(key, default)
    except Exception as e:
        return False

def dict_fromkeys(keys, value=None):
    """Creates a new dictionary with the specified keys and a default value."""
    try:
        return dict.fromkeys(keys, value)
    except Exception as e:
        return False

def dict_get_key_with_max_value(d):
    """Returns the key with the maximum value in the dictionary."""
    try:
        return max(d, key=d.get, default=None)
    except Exception as e:
        return False

def dict_get_key_with_min_value(d):
    """Returns the key with the minimum value in the dictionary."""
    try:
        return min(d, key=d.get, default=None)
    except Exception as e:
        return False
