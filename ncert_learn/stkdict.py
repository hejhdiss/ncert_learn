def createstackdict():

        """
        Creates a new empty stack represented as a dictionary.
        Returns a dictionary.

        >>> createstackdict()
        {}
        """

        return {}
def clearstackdict(a):

        """
        Clears the stack represented as a dictionary.
        No return value.
        """
        

        a.clear()
def pushstackdict(a,b):

        """
        Pushes a dictionary onto the stack.
        No return value.

        >>> stack = createstackdict()
        >>> pushstackdict(stack, {'a': 1})
        {'a': 1}
        >>> pushstackdict(stack, {'b': 2})
        {'a': 1, 'b': 2}
        """

        a.update(b)
        return a
def popstackdict(a):

        """
        Removes and returns the last inserted key-value pair from the stack represented as a dictionary.
        Returns the modified dictionary.
        If the stack is empty, returns -1.

        >>> stack = {'a': 1, 'b': 2}
        >>> popstackdict(stack)
        {'a': 1}
        >>> popstackdict({})
        -1
        """

        if a=={}:
            return -1
        else:
            s=a.pop()
            return(a)
def peekstackdict(a):
    

    """
    Returns the value of the last inserted key in the stack represented as a dictionary without removing it.
    If the stack is empty, returns -1.

    Args:
        a (dict): The stack represented as a dictionary.

    Returns:
        The value of the last inserted key if the stack is not empty, otherwise -1.

    >>> stack = {'a': 1, 'b': 2}
    >>> peekstackdict(stack)
    2
    >>> peekstackdict({})
    -1
    """

    s=a.keys()
    if a=={}:
        return -1
    else:
        return a[s[-1]]
def displaymodestackdict(a):

        """
        Returns a list of the items in the stack represented as a dictionary where each item is a tuple of the key-value pair.
        The list is ordered with the most recently inserted key-value pair at the end of the list.
        If the stack is empty, returns an empty list.

        >>> stack = {'a': 1, 'b': 2}
        >>> displaymodestackdict(stack)
        [('a', 1), ('b', 2)]
        >>> displaymodestackdict({})
        []
        """

        s=[]
        for k,v in a:
            s.append((k,v))
        return s
