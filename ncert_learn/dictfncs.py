# Extended Functions for dictionary operations

def dict_add_key_value(d, key, value):
    """Adds a key-value pair to the dictionary."""
    d[key] = value
    return d

def dict_remove_key(d, key):
    """Removes a key-value pair from the dictionary."""
    if key in d:
        del d[key]
        return d
    return False

def dict_get_value(d, key):
    """Gets the value for a given key in the dictionary."""
    return d.get(key, None)

def dict_update_value(d, key, value):
    """Updates the value of an existing key in the dictionary."""
    if key in d:
        d[key] = value
        return d
    return False

def dict_contains_key(d, key):
    """Checks if the dictionary contains a specific key."""
    return key in d

def dict_get_all_keys(d):
    """Returns a list of all keys in the dictionary."""
    return list(d.keys())

def dict_get_all_values(d):
    """Returns a list of all values in the dictionary."""
    return list(d.values())

def dict_clear(d):
    """Clears all key-value pairs from the dictionary."""
    d.clear()
    return d

def dict_copy(d):
    """Returns a shallow copy of the dictionary."""
    return d.copy()

def dict_items(d):
    """Returns a list of all key-value pairs as tuples."""
    return list(d.items())

def dict_pop_item(d, key):
    """Removes and returns the value for a specified key."""
    return d.pop(key, None)

def dict_update(d, other_dict):
    """Updates the dictionary with another dictionary's key-value pairs."""
    d.update(other_dict)
    return d

def dict_setdefault(d, key, default=None):
    """Returns the value of the key if it exists, otherwise inserts the key with the default value."""
    return d.setdefault(key, default)

def dict_fromkeys(keys, value=None):
    """Creates a new dictionary with the specified keys and a default value."""
    return dict.fromkeys(keys, value)

def dict_get_key_with_max_value(d):
    """Returns the key with the maximum value in the dictionary."""
    return max(d, key=d.get, default=None)

def dict_get_key_with_min_value(d):
    """Returns the key with the minimum value in the dictionary."""
    return min(d, key=d.get, default=None)
