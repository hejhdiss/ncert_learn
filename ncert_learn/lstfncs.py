# Extended Functions for list operations

def list_append_item(lst, item):
    """Appends an item to the list."""
    lst.append(item)
    return lst

def list_remove_item(lst, item):
    """Removes the first occurrence of an item from the list."""
    if item in lst:
        lst.remove(item)
        return lst
    return False

def list_insert_item(lst, index, item):
    """Inserts an item at a specified index in the list."""
    lst.insert(index, item)
    return lst

def list_pop_item(lst, index=-1):
    """Pops an item from the list at the specified index."""
    if 0 <= index < len(lst):
        return lst.pop(index)
    return False

def list_find_index(lst, item):
    """Finds the index of the first occurrence of an item in the list."""
    if item in lst:
        return lst.index(item)
    return -1

def list_contains_item(lst, item):
    """Checks if the list contains a specific item."""
    return item in lst

def list_sort(lst, reverse=False):
    """Sorts the list in ascending or descending order."""
    lst.sort(reverse=reverse)
    return lst

def list_reverse(lst):
    """Reverses the order of the items in the list."""
    lst.reverse()
    return lst

def list_clear(lst):
    """Clears all items from the list."""
    lst.clear()
    return lst

def list_copy(lst):
    """Returns a shallow copy of the list."""
    return lst.copy()

def list_extend(lst, other_lst):
    """Extends the list by appending elements from another list."""
    lst.extend(other_lst)
    return lst

def list_count(lst, item):
    """Counts how many times an item appears in the list."""
    return lst.count(item)

def list_min(lst):
    """Returns the minimum item from the list."""
    return min(lst)

def list_max(lst):
    """Returns the maximum item from the list."""
    return max(lst)

def list_sum(lst):
    """Returns the sum of all items in the list."""
    return sum(lst)

def list_mean(lst):
    """Returns the mean (average) of all items in the list."""
    return sum(lst) / len(lst) if lst else None

def list_unique(lst):
    """Returns a list of unique items from the list."""
    return list(set(lst))

def list_combine(lst1, lst2):
    """Combines two lists into one."""
    return lst1 + lst2

def list_difference(lst1, lst2):
    """Returns the items in lst1 that are not in lst2."""
    return list(set(lst1) - set(lst2))

def list_intersection(lst1, lst2):
    """Returns the items that are common in both lists."""
    return list(set(lst1) & set(lst2))

def list_is_empty(lst):
    """Checks if the list is empty."""
    return len(lst) == 0
