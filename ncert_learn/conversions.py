def integertobinary(s):

    """
    Converts an integer to binary format.

    Parameters
    ----------
    s : int
        The integer to convert

    Returns
    -------
    int
        The binary representation of the integer if the input is an integer, otherwise False
    """

    if not('int' in str(type(s))):
        return False
    else:
        g=''
        while s>0:
            g+=str(s%2)
            s=s//2
        return int(g[::-1])
def integertooctal(s):

    """
    Converts an integer to octal format.

    Parameters
    ----------
    s : int
        The integer to convert

    Returns
    -------
    str
        The octal representation of the integer if the input is an integer, otherwise False
    """

    if not('int' in str(type(s))):
        return False
    else:
        return format(s, 'o')
def integertohexadecimal(s):

    """
    Converts an integer to hexadecimal format.

    Parameters
    ----------
    s : int
        The integer to convert

    Returns
    -------
    str
        The hexadecimal representation of the integer if the input is an integer, otherwise False
    """

    if not('int' in str(type(s))):
        return False
    else:
        return hex(s)[2:]
def binarytointeger(s):

    """
    Converts a binary number to an integer.

    Parameters
    ----------
    s : int
        The binary number to convert

    Returns
    -------
    int
        The integer representation of the binary number if the input is an integer, otherwise False
    """

    if not('int' in str(type(s))):
        return False
    else:
        s=str(s)
        return int(s, 2)







