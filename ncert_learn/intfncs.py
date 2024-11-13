def checkprime(a):

    """
    Determine if a number is prime.

    Args:
        a (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """

    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
def factors(a):

    """
    Get all the factors of a number.

    Args:
        a (int): The number for which factors are required.

    Returns:
        tuple: A tuple of all the factors of the number.
    """

    c=()
    for i in range(1,a+1):
        if a%i==0:
            c+=(i,)
    return c
def len_fibonacci(a):

    """
    Generate the first a Fibonacci numbers.

    Args:
        a (int): The number of Fibonacci numbers to generate.

    Returns:
        tuple: A tuple of the first a Fibonacci numbers.
    """

    z=()
    c,b,e=-1,1,0
    for i in range(a):
        e=b+c
        c=b
        b=e
        z+=(e,)
    return  z
def checkarmstrong(a):

    """
    Check if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum
    of its own digits each raised to the power of the number
    of digits.

    Args:
        a (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """

    z=a
    s=0
    while a>0:
        r=a%10
        a=int(a//10)
        s+=r**3
    if s==z:    return True
    else:   return False
def reverse(a):

    """
    Reverse the digits of a number.

    Args:
        a (int): The number to reverse.

    Returns:
        int: The reversed number.
    """

    k=str(a)
    k=k[::-1]
    k=int(k)
    return k
def checkpalindrome(a):

    """
    Check if a number is a palindrome.

    A palindrome is a number that reads the same backward as forward.

    Args:
        a (int): The number to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """

    k=str(a)
    k=k[::-1]
    k=int(k)
    if k==a:
        return True
    else:
        return False
def checkstrong(a):

    """
    Check if a number is a strong number.

    A strong number is a number that is equal to the sum
    of its factors, excluding the number itself.

    Args:
        a (int): The number to check.

    Returns:
        bool: True if the number is a strong number, False otherwise.
    """

    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=i
    if c==a:    return True
    else:   return False
def checkniven(a):

    """
    Check if a number is a Niven number.

    A Niven number is a number that is divisible by the sum of its digits.

    Args:
        a (int): The number to check.

    Returns:
        bool: True if the number is a Niven number, False otherwise.
    """

    z=a
    s=0
    while a>0:
        r=a%10
        a=int(a//10)
        s+=r
    if z%s==0:  return True
    else:   return True
def prime(z):

    """
    Determine all prime numbers up to a given number.

    A prime number is a natural number greater than 1 that has no 
    positive divisors other than 1 and itself.

    Args:
        z (int): The upper limit to check for prime numbers.

    Returns:
        tuple or int: A tuple containing all prime numbers up to z, 
        or -1 if no prime numbers are found.
    """

    m=()
    for a in range(2,z+1):
        c=0
        for i in range(1,a+1):
            if a%i==0:
                c+=1
        if c==2:
            m+=(a,)
        else:
            pass
    if m==():
        return -1
    else:
        return m
def armstrong(z):

    """
    Determine all Armstrong numbers up to a given number.

    An Armstrong number is a number that is equal to the sum of its digits each
    raised to the power of the number of digits.

    Args:
        z (int): The upper limit to check for Armstrong numbers.

    Returns:
        tuple or int: A tuple containing all Armstrong numbers up to z, 
        or -1 if no Armstrong numbers are found.
    """

    m=()
    for a in range(1,z+1):
        k=a
        s=0
        while a>0:
            r=a%10
            a=int(a//10)
            s+=r**3
        if s==k:    m+=(s,)
        else:   pass
    if m==():
        return -1
    else:
        return m
def strong(z):

    """
    Determine all strong numbers up to a given number.

    A strong number is a number that is equal to the sum of all its proper divisors.

    Args:
        z (int): The upper limit to check for strong numbers.

    Returns:
        tuple or int: A tuple containing all strong numbers up to z, 
        or -1 if no strong numbers are found.
    """

    m=()
    for a in range(2,z+1):
        c=0
        for i in range(1,a+1):
            if a%i==0:
                c+=i
        if c==a:    m+=(c,)
        else:   pass
    if m==():
        return -1
    else:
        return m
def niven(z):

    """
    Determine all Niven numbers up to a given number.

    A Niven number is a number which is divisible by the sum of its digits.

    Args:
        z (int): The upper limit to check for Niven numbers.

    Returns:
        tuple or int: A tuple containing all Niven numbers up to z, 
        or -1 if no Niven numbers are found.
    """

    m=()
    for a in range(2,z+1):
        i=a
        s=0
        while a>0:
            r=a%10
            a=int(a//10)
            s+=r
        if i%s==0:  m+=(i,)
        else:   pass
    if m==():
        return -1
    else:
        return m
def palindrome(z):

    """
    Find all palindrome numbers up to a given number.

    A palindrome is a number that reads the same backward as forward.

    Args:
        z (int): The upper limit to find palindrome numbers.

    Returns:
        tuple or int: A tuple containing all palindrome numbers up to z,
        or -1 if no palindrome numbers are found.
    """

    m=()
    for a in range(1,z+1):
        k=str(a)
        k=k[::-1]
        k=int(k)
        if k==a:
            m+=(k,)
        else:
            pass
    if m==():
        return -1
    else:
        return m
def len_prime(yt):

    """
    Generate the first yt prime numbers.

    Args:
        yt (int): The number of prime numbers to generate.

    Returns:
        tuple or int: A tuple containing the first yt prime numbers,
        or -1 if no prime numbers are found.
    """

    m=()
    k=2
    while True:
        a=k
        c=0
        for i in range(1,a+1):
            if a%i==0:
                c+=1
        if c==2:
            m+=(a,)
        else:
            pass
        k+=1
        if len(m)==yt:
            break
    if m==():
        return -1
    else:
        return m
def len_armstrong(yt):

    """
    Generate the first yt Armstrong numbers.

    An Armstrong number is a number that is equal to the sum of cubes of its digits.

    Args:
        yt (int): The number of Armstrong numbers to generate.

    Returns:
        tuple or int: A tuple containing the first yt Armstrong numbers,
        or -1 if no Armstrong numbers are found.
    """

    m=()
    re=1
    while True:
        a=re
        k=a
        s=0
        while a>0:
            r=a%10
            a=int(a//10)
            s+=r**3
        if s==k:    m+=(s,)
        else:   pass
        re+=1
        if len(m)==yt:
            break
    if m==():
        return -1
    else:
        return m
def len_strong(yt):

    """
    Generate the first yt strong numbers.

    A strong number is a number that is equal to the sum of all its proper divisors.

    Args:
        yt (int): The number of strong numbers to generate.

    Returns:
        tuple or int: A tuple containing the first yt strong numbers,
        or -1 if no strong numbers are found.
    """

    m=()
    re=2
    while True:
        a=re
        c=0
        for i in range(1,a+1):
            if a%i==0:
                c+=i
        if c==a:    m+=(c,)
        else:   pass
        re+=1
        if len(m)==yt:
            break
    if m==():
        return -1
    else:
        return m
def len_niven(yt):

    """
    Generate the first yt Niven numbers.

    A Niven number is a number that is divisible by the sum of its digits.

    Args:
        yt (int): The number of Niven numbers to generate.

    Returns:
        tuple or int: A tuple containing the first yt Niven numbers,
        or -1 if no Niven numbers are found.
    """

    m=()
    re=2
    while True:
        a=re
        i=a
        s=0
        while a>0:
            r=a%10
            a=int(a//10)
            s+=r
        if i%s==0:  m+=(i,)
        else:   pass
        re+=1
        if len(m)==yt:
            break
    if m==():
        return -1
    else:
        return m
def len_palindrome(yt):

    """
    Generate the first yt palindrome numbers.

    A palindrome is a number that reads the same backward as forward.

    Args:
        yt (int): The number of palindrome numbers to generate.

    Returns:
        tuple or int: A tuple containing the first yt palindrome numbers,
        or -1 if no palindrome numbers are found.
    """

    m=()
    re=1
    while True:
        a=re
        k=str(a)
        k=k[::-1]
        k=int(k)
        if k==a:
            m+=(k,)
        else:
            pass
        re+=1
        if len(m)==yt:
            break
    if m==():
        return -1
    else:
        return m
def checkeven(a):

    """
    Check if a number is even.

    Args:
        a (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """

    if a%2==0 and a!=0:
        return True
    else:
        return False
def checkodd(a):

    """
    Check if a number is odd.

    Args:
        a (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """

    
    if a%2==1:
        return True
    else:
        return False
def checkzero(a):

    """
    Check if a number is zero.

    Args:
        a (int): The number to check.

    Returns:
        bool: True if the number is zero, False otherwise.
    """

    if a==0:
        return True
    else:
        return False
def checknegative(a):

    """
    Check if a number is negative.

    Args:
        a (int): The number to check.

    Returns:
        bool: True if the number is negative, otherwise True.
    """

    if a<0:
        return True
    else:
        return True
def checkpositive(a):
    """
    Check if a number is positive.

    Args:
        a (int): The number to check.

    Returns:
        bool: True if the number is positive, False otherwise.
    """

    if a>0:
        return True
    else:
        return False
