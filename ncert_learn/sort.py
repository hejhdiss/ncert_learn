def bubblesort(a):

    """Bubblesort Algorithm for sorting a list of numbers in ascending order.

    It takes a list of numbers as argument and returns a sorted list in ascending order. If the argument is not a list, it returns False. If the list is empty, it returns an empty list.

    The algorithm works by repeatedly swapping the adjacent elements if they are in wrong order. It continues to pass through the list until the list is sorted. The time complexity of this algorithm is O(n^2).

    Parameters:
    a (list): the list of numbers to be sorted

    Returns:
    list: the sorted list in ascending order
    """

    if not('list' in str(type(a))):
        return False
    elif a==[]:
        return []
    else:
        n=len(a)
        for i in range(n-1):
            for j in range(n-i-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
        return a

def insertionsort(a):

    """
    Insertion Sort Algorithm for sorting a list of numbers in ascending order.

    This function sorts a list of numbers using the insertion sort algorithm. It takes a list as input and returns the sorted list in ascending order. If the input is not a list, it returns False. If the list is empty, it returns an empty list.

    The insertion sort algorithm works by iterating through the list and comparing each element with the elements in the sorted portion of the list. If an element is smaller, it is shifted to the correct position within the sorted portion. This process is repeated until the entire list is sorted. The time complexity of this algorithm is O(n^2).

    Parameters:
    a (list): The list of numbers to be sorted.

    Returns:
    list: The sorted list in ascending order, or False if the input is not a list.
    """

    if not('list' in str(type(a))):
        return False
    elif a==[]:
        return []
    else:
        for i in range(len(a)):
            for j in range(len(a)-i-1,0,-1):
                if a[j-1]>a[j]:
                    a[j-1],a[j]=a[j],a[j-1]
                else:
                    break
        return a
def merge_sort(a):
    """Merge Sort Algorithm for sorting a list of numbers in ascending order.

    It recursively divides the list into two halves, sorts each half, and then merges the sorted halves.
    The time complexity of this algorithm is O(n log n), making it more efficient than Bubble Sort.

    Parameters:
    a (list): the list of numbers to be sorted

    Returns:
    list: the sorted list in ascending order
    """
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    
    return merge_list(left, right)

def merge_list(left, right):
    

    """
    Merges two sorted lists into a single sorted list.

    This function takes two sorted lists, `left` and `right`, and merges them
    into a new sorted list. It iterates through both lists, comparing elements
    and appending the smaller element to the result list. Once one of the lists
    is exhausted, the remaining elements from the other list are appended to
    the result.

    Parameters:
    left (list): The first sorted list.
    right (list): The second sorted list.

    Returns:
    list: A new list containing all elements from `left` and `right`, sorted in
    ascending order.
    """

    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def quick_sort(a):
    """Quick Sort Algorithm for sorting a list of numbers in ascending order.

    It selects a pivot element, partitions the list around the pivot, and recursively sorts the sublists.
    The time complexity of this algorithm is O(n log n) on average.

    Parameters:
    a (list): the list of numbers to be sorted

    Returns:
    list: the sorted list in ascending order
    """
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)



