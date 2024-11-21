def list_append_item(lst, item):
    """Appends an item to the list."""
    try:
        lst.append(item)
        return lst
    except Exception as e:
        return False

def list_remove_item(lst, item):
    """Removes the first occurrence of an item from the list."""
    try:
        if item in lst:
            lst.remove(item)
            return lst
        return False
    except Exception as e:
        return False

def list_insert_item(lst, index, item):
    """Inserts an item at a specified index in the list."""
    try:
        lst.insert(index, item)
        return lst
    except Exception as e:
        return False

def list_pop_item(lst, index=-1):
    """Pops an item from the list at the specified index."""
    try:
        if -len(lst) <= index < len(lst):  # Handle negative indices
            return lst.pop(index)
        return False
    except Exception as e:
        return False

def list_find_index(lst, item):
    """Finds the index of the first occurrence of an item in the list."""
    try:
        return lst.index(item) if item in lst else -1
    except Exception as e:
        return False

def list_contains_item(lst, item):
    """Checks if the list contains a specific item."""
    try:
        return item in lst
    except Exception as e:
        return False

def list_sort(lst, reverse=False):
    """Sorts the list in ascending or descending order."""
    try:
        lst.sort(reverse=reverse)
        return lst
    except Exception as e:
        return False

def list_reverse(lst):
    """Reverses the order of the items in the list."""
    try:
        lst.reverse()
        return lst
    except Exception as e:
        return False

def list_clear(lst):
    """Clears all items from the list."""
    try:
        lst.clear()
        return lst
    except Exception as e:
        return False

def list_copy(lst):
    """Returns a shallow copy of the list."""
    try:
        return lst.copy()
    except Exception as e:
        return False

def list_extend(lst, other_lst):
    """Extends the list by appending elements from another list."""
    try:
        lst.extend(other_lst)
        return lst
    except Exception as e:
        return False

def list_count(lst, item):
    """Counts how many times an item appears in the list."""
    try:
        return lst.count(item)
    except Exception as e:
        return False

def list_min(lst):
    """Returns the minimum item from the list."""
    try:
        return min(lst)
    except Exception as e:
        return False

def list_max(lst):
    """Returns the maximum item from the list."""
    try:
        return max(lst)
    except Exception as e:
        return False

def list_sum(lst):
    """Returns the sum of all items in the list."""
    try:
        return sum(lst)
    except Exception as e:
        return False

def list_mean(lst):
    """Returns the mean (average) of all items in the list."""
    try:
        return sum(lst) / len(lst) if lst else None
    except Exception as e:
        return False

def list_unique(lst):
    """Returns a list of unique items from the list."""
    try:
        return list(set(lst))
    except Exception as e:
        return False

def list_combine(lst1, lst2):
    """Combines two lists into one."""
    try:
        return lst1 + lst2
    except Exception as e:
        return False

def list_difference(lst1, lst2):
    """Returns the items in lst1 that are not in lst2."""
    try:
        return list(set(lst1) - set(lst2))
    except Exception as e:
        return False

def list_intersection(lst1, lst2):
    """Returns the items that are common in both lists."""
    try:
        return list(set(lst1) & set(lst2))
    except Exception as e:
        return False

def list_is_empty(lst):
    """Checks if the list is empty."""
    try:
        return len(lst) == 0
    except Exception as e:
        return False
