def createstacklst():

        """Creates an empty stack implemented as a list.

        Returns:
            list: An empty list to be used as a stack.
        """

        return []
def clearstacklst(a):
        """Clears the stack implemented as a list.

        This function clears the stack by emptying the list. It does not return any value.

        Parameters:
            a (list): The stack implemented as a list to be cleared.
        """

        a.clear()
def pushstacklst(a,b):
        

        """Pushes an item onto the stack implemented as a list.

        Parameters:
            a (list): The stack implemented as a list.
            b (object): The item to be pushed onto the stack.

        Returns:
            list: The modified stack implemented as a list.
        """

        a.append(b)
        return a
def popstacklst(a):

        """Pops an item from the stack implemented as a list.

        If the stack is empty, -1 is returned. Otherwise, the popped item is returned
        and the stack is modified.

        Parameters:
            a (list): The stack implemented as a list.

        Returns:
            object: The popped item if the stack is not empty, -1 otherwise.
        """

        if a==[]:
            return -1
        else:
            s=a.pop()
            return(a)
def peekstacklst(a):

        """Returns the top element from the stack implemented as a list without removing it.

        If the stack is empty, -1 is returned. Otherwise, the top element is returned.

        Parameters:
            a (list): The stack implemented as a list.

        Returns:
            object: The top element if the stack is not empty, -1 otherwise.
        """

        if a==[]:
            return -1
        else:
            return a[-1]
def displaymodestacklst(a):

        """Returns a modified version of the stack implemented as a list by reversing the order of its elements.

        Parameters:
            a (list): The stack implemented as a list to be modified.

        Returns:
            list: The modified stack implemented as a list with the order of its elements reversed.
        """

        s=[]
        for i in range(-1,(len(a)*-1)-1,-1):
            s.append(a[i])
        return s
