import time

def currenttime():

    """
    Returns the current time in the format HH:MM:SS.

    Returns
    -------
    str
        The current time in the format HH:MM:SS.
    """


    return time.ctime()[11:20]
def processtime():

    """
    Returns the sum of the system and user CPU time of the current process.
    
    Returns
    -------
    float
        The sum of the system and user CPU time of the current process.
    """

    return time.process_time()
def monotonic():

    """
    Returns the value (in fractional seconds) of a performance counter, which is a 
    clock with the highest available resolution to measure a short duration. It does 
    include time elapsed during sleep and is system-wide. The reference point of the 
    returned value is undefined, so that only the difference between the results of 
    consecutive calls is valid.
    """

    return time.monotonic()
def threadtime():

    """
    Returns the sum of the system and user CPU time of the current thread.

    Returns
    -------
    float
        The sum of the system and user CPU time of the current thread.
    """

    return time.thread_time()
