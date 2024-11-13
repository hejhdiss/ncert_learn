import math
def areaofcircle(radius):

    """
    Calculate the area of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """

    s=radius ** 2
    return math.pi *s
def areaoftriangle(base, height):
    """
    Calculate the area of a triangle given its base and height.

    Parameters:
    base (float): The base length of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """

    
    return 0.5 * base * height
def areaofsquare(side):
    
    """
    Calculate the area of a square given the length of its side.

    Parameters:
    side (float): The length of the side of the square.

    Returns:
    float: The area of the square.
    """

    return side ** 2
def areaofrectangle(length, width):

    """
    Calculate the area of a rectangle given its length and width.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """

    return length * width


def areaofpolygon(noofsides,lengthofeachside):

    """
    Calculate the area of a polygon given its number of sides and the length of its side.

    Parameters:
    noofsides (int): The number of sides of the polygon.
    lengthofeachside (float): The length of each side of the polygon.

    Returns:
    float or str: The area of the polygon. If the number of sides is less than 3, it returns a message.
    """

    n=noofsides
    s=lengthofeachside
    if n < 3:
        return "A polygon must have at least 3 sides."
    return (n * s**2) / (4 * math.tan(math.pi / n))

