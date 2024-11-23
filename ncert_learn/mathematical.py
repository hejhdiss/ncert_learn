import math

# --------------------------- Trigonometric Functions ---------------------------

def trigonometric_sine(angle_degrees):
    """Returns the sine of an angle in degrees."""
    try:
        angle_radians = math.radians(angle_degrees)
        return math.sin(angle_radians)
    except:
        return False

def trigonometric_cosine(angle_degrees):
    """Returns the cosine of an angle in degrees."""
    try:
        angle_radians = math.radians(angle_degrees)
        return math.cos(angle_radians)
    except:
        return False

def trigonometric_tangent(angle_degrees):
    """Returns the tangent of an angle in degrees."""
    try:
        angle_radians = math.radians(angle_degrees)
        return math.tan(angle_radians)
    except:
        return False

def trigonometric_inverse_sine(value):
    """Returns the inverse sine (arcsin) of a value."""
    try:
        if -1 <= value <= 1:
            return math.degrees(math.asin(value))
        else:
            raise ValueError("Value out of range for arcsine")
    except:
        return False

def trigonometric_inverse_cosine(value):
    """Returns the inverse cosine (arccos) of a value."""
    try:
        if -1 <= value <= 1:
            return math.degrees(math.acos(value))
        else:
            raise ValueError("Value out of range for arccosine")
    except:
        return False

def trigonometric_inverse_tangent(value):
    """Returns the inverse tangent (arctan) of a value."""
    try:
        return math.degrees(math.atan(value))
    except:
        return False

# --------------------------- Algebraic Functions ---------------------------

def quadratic_roots(a, b, c):
    """Returns the roots of a quadratic equation ax^2 + bx + c = 0."""
    try:
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2 * a)
            return root,
        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-discriminant) / (2 * a)
            return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)
    except:
        return False

def power(base, exponent):
    """Returns the result of base raised to the exponent."""
    try:
        return math.pow(base, exponent)
    except:
        return False

def logarithm(value, base=10):
    """Returns the logarithm of a value with the specified base."""
    try:
        return math.log(value, base)
    except:
        return False

def factorial(n):
    """Returns the factorial of a number."""
    try:
        return math.factorial(n)
    except:
        return False

def gcd(a, b):
    """Returns the greatest common divisor of two numbers."""
    try:
        while b:
            a, b = b, a % b
        return a
    except:
        return False

def lcm(a, b):
    """Returns the least common multiple of two numbers."""
    try:
        return abs(a * b) // gcd(a, b)
    except:
        return False

def binomial_coefficient(n, k):
    """Returns the binomial coefficient C(n, k)."""
    try:
        if k > n:
            return False
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    except:
        return False

# --------------------------- Calculus Functions ---------------------------

def derivative(func, x, h=1e-5):
    """Returns the derivative of a function at point x using a small value h."""
    try:
        return (func(x + h) - func(x - h)) / (2 * h)
    except:
        return False

def definite_integral(func, a, b, n=1000):
    """Returns the definite integral of a function from a to b using the trapezoidal rule."""
    try:
        step = (b - a) / n
        integral = 0.5 * (func(a) + func(b))
        for i in range(1, n):
            integral += func(a + i * step)
        return integral * step
    except:
        return False

def series_sum(a, r, n):
    """Returns the sum of a geometric series."""
    try:
        if r == 1:
            return a * n
        return a * (1 - r**n) / (1 - r)
    except:
        return False

# --------------------------- Geometry Functions ---------------------------

def area_of_circle(radius):
    """Returns the area of a circle given its radius."""
    try:
        return math.pi * radius ** 2
    except:
        return False

def area_of_triangle(base, height):
    """Returns the area of a triangle given its base and height."""
    try:
        return 0.5 * base * height
    except:
        return False

def area_of_rectangle(length, breadth):
    """Returns the area of a rectangle given its length and breadth."""
    try:
        return length * breadth
    except:
        return False

def volume_of_sphere(radius):
    """Returns the volume of a sphere given its radius."""
    try:
        return (4/3) * math.pi * radius ** 3
    except:
        return False

def volume_of_cylinder(radius, height):
    """Returns the volume of a cylinder given its radius and height."""
    try:
        return math.pi * radius ** 2 * height
    except:
        return False

# --------------------------- Number Theory Functions ---------------------------

def is_prime(n):
    """Returns True if the number is prime, else False."""
    try:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    except:
        return False

def prime_factors(n):
    """Returns a list of prime factors of a number."""
    try:
        factors = []
        for i in range(2, int(math.sqrt(n)) + 1):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 1:
            factors.append(n)
        return factors
    except:
        return False

def fibonacci(n):
    """Returns the nth Fibonacci number."""
    try:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    except:
        return False

def perfect_number(n):
    """Returns True if the number is perfect (sum of divisors = number), else False."""
    try:
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    except:
        return False

def is_palindrome(n):
    """Returns True if the number is a palindrome, else False."""
    try:
        return str(n) == str(n)[::-1]
    except:
        return False

def sum_of_divisors(n):
    """Returns the sum of divisors of a number."""
    try:
        return sum(i for i in range(1, n) if n % i == 0)
    except:
        return False

def is_abundant(n):
    """Returns True if the number is abundant (sum of divisors > number), else False."""
    try:
        return sum_of_divisors(n) > n
    except:
        return False

def is_deficient(n):
    """Returns True if the number is deficient (sum of divisors < number), else False."""
    try:
        return sum_of_divisors(n) < n
    except:
        return False

def triangular_number(n):
    """Returns the nth triangular number."""
    try:
        return n * (n + 1) // 2
    except:
        return False

def is_square_number(n):
    """Returns True if the number is a perfect square, else False."""
    try:
        return math.isqrt(n) ** 2 == n
    except:
        return False

# --------------------------- Probability and Statistics ---------------------------

def mean(numbers):
    """Returns the mean (average) of a list of numbers."""
    try:
        return sum(numbers) / len(numbers)
    except:
        return False

def median(numbers):
    """Returns the median of a list of numbers."""
    try:
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        else:
            return sorted_numbers[mid]
    except:
        return False

def variance(numbers):
    """Returns the variance of a list of numbers."""
    try:
        m = mean(numbers)
        return sum((x - m) ** 2 for x in numbers) / len(numbers)
    except:
        return False

def standard_deviation(numbers):
    """Returns the standard deviation of a list of numbers."""
    try:
        return math.sqrt(variance(numbers))
    except:
        return False

# --------------------------- Miscellaneous Functions ---------------------------

def harmonic_mean(numbers):
    """Returns the harmonic mean of a list of numbers."""
    try:
        return len(numbers) / sum(1/x for x in numbers)
    except:
        return False

def check_armstrong(number):
    """Returns True if the number is an Armstrong number, else False."""
    try:
        digits = [int(digit) for digit in str(number)]
        power = len(digits)
        return number == sum(digit ** power for digit in digits)
    except:
        return False

import math

# --------------------------- Trigonometric Functions ---------------------------

def trigonometric_secant(angle_degrees):
    """Returns the secant of an angle in degrees."""
    try:
        angle_radians = math.radians(angle_degrees)
        return 1 / math.cos(angle_radians)
    except:
        return False

def trigonometric_cosecant(angle_degrees):
    """Returns the cosecant of an angle in degrees."""
    try:
        angle_radians = math.radians(angle_degrees)
        return 1 / math.sin(angle_radians)
    except:
        return False

def trigonometric_cotangent(angle_degrees):
    """Returns the cotangent of an angle in degrees."""
    try:
        angle_radians = math.radians(angle_degrees)
        return 1 / math.tan(angle_radians)
    except:
        return False

def trigonometric_inverse_secant(value):
    """Returns the inverse secant (arcsec) of a value."""
    try:
        if abs(value) >= 1:
            return math.degrees(math.acos(1 / value))
        else:
            raise ValueError("Value out of range for arcsecant")
    except:
        return False

def trigonometric_inverse_cosecant(value):
    """Returns the inverse cosecant (arccsc) of a value."""
    try:
        if abs(value) >= 1:
            return math.degrees(math.asin(1 / value))
        else:
            raise ValueError("Value out of range for arccosecant")
    except:
        return False

def trigonometric_inverse_cotangent(value):
    """Returns the inverse cotangent (arccot) of a value."""
    try:
        return math.degrees(math.atan(1 / value))
    except:
        return False

# --------------------------- Algebraic Functions ---------------------------

def cube_root(value):
    """Returns the cube root of a value."""
    try:
        return value ** (1/3)
    except:
        return False

def nth_root(value, n):
    """Returns the nth root of a value."""
    try:
        return value ** (1/n)
    except:
        return False

def exponential(base, exponent):
    """Returns the result of base raised to the exponent."""
    try:
        return base ** exponent
    except:
        return False

def mod_inverse(a, m):
    """Returns the modular inverse of a under modulo m."""
    try:
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None
    except:
        return False

def absolute(value):
    """Returns the absolute value of a number."""
    try:
        return abs(value)
    except:
        return False

def round_to_decimal(value, places):
    """Rounds a number to the specified decimal places."""
    try:
        return round(value, places)
    except:
        return False

def ceil(value):
    """Returns the ceiling of a value."""
    try:
        return math.ceil(value)
    except:
        return False

def floor(value):
    """Returns the floor of a value."""
    try:
        return math.floor(value)
    except:
        return False

def sine_wave(value, frequency=1, amplitude=1):
    """Returns the sine wave value for a given frequency and amplitude."""
    try:
        return amplitude * math.sin(2 * math.pi * frequency * value)
    except:
        return False

def cosine_wave(value, frequency=1, amplitude=1):
    """Returns the cosine wave value for a given frequency and amplitude."""
    try:
        return amplitude * math.cos(2 * math.pi * frequency * value)
    except:
        return False

# --------------------------- Calculus Functions ---------------------------

def second_derivative(func, x, h=1e-5):
    """Returns the second derivative of a function at point x."""
    try:
        return (func(x + h) - 2 * func(x) + func(x - h)) / (h ** 2)
    except:
        return False

def integrate_by_simpsons_rule(func, a, b, n=1000):
    """Returns the integral of a function from a to b using Simpson's rule."""
    try:
        h = (b - a) / n
        integral = func(a) + func(b)
        for i in range(1, n, 2):
            integral += 4 * func(a + i * h)
        for i in range(2, n, 2):
            integral += 2 * func(a + i * h)
        return integral * h / 3
    except:
        return False

def nth_derivative(func, x, n, h=1e-5):
    """Returns the nth derivative of a function at point x."""
    try:
        for i in range(n):
            func = lambda x: (func(x + h) - func(x - h)) / (2 * h)
        return func(x)
    except:
        return False

def tangent_line_at_point(func, x, h=1e-5):
    """Returns the equation of the tangent line at point x for a function."""
    try:
        slope = (func(x + h) - func(x)) / h
        intercept = func(x) - slope * x
        return f"y = {slope}x + {intercept}"
    except:
        return False

# --------------------------- Geometry Functions ---------------------------

def area_of_parallelogram(base, height):
    """Returns the area of a parallelogram."""
    try:
        return base * height
    except:
        return False

def perimeter_of_rectangle(length, breadth):
    """Returns the perimeter of a rectangle."""
    try:
        return 2 * (length + breadth)
    except:
        return False

def perimeter_of_circle(radius):
    """Returns the perimeter (circumference) of a circle."""
    try:
        return 2 * math.pi * radius
    except:
        return False

def surface_area_of_sphere(radius):
    """Returns the surface area of a sphere given its radius."""
    try:
        return 4 * math.pi * radius ** 2
    except:
        return False

def surface_area_of_cylinder(radius, height):
    """Returns the surface area of a cylinder."""
    try:
        return 2 * math.pi * radius * (radius + height)
    except:
        return False

def volume_of_cone(radius, height):
    """Returns the volume of a cone."""
    try:
        return (1/3) * math.pi * radius**2 * height
    except:
        return False

def volume_of_pyramid(base_area, height):
    """Returns the volume of a pyramid given base area and height."""
    try:
        return (1/3) * base_area * height
    except:
        return False

# --------------------------- Number Theory Functions ---------------------------

def is_composite(n):
    """Returns True if the number is composite, else False."""
    try:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    except:
        return False

def count_divisors(n):
    """Returns the number of divisors of a number."""
    try:
        divisors = [i for i in range(1, n+1) if n % i == 0]
        return len(divisors)
    except:
        return False

def is_perfect_square(n):
    """Returns True if the number is a perfect square."""
    try:
        return math.isqrt(n) ** 2 == n
    except:
        return False

def sum_of_squares(n):
    """Returns the sum of squares of the first n natural numbers."""
    try:
        return sum(i**2 for i in range(1, n+1))
    except:
        return False

def sum_of_cubes(n):
    """Returns the sum of cubes of the first n natural numbers."""
    try:
        return sum(i**3 for i in range(1, n+1))
    except:
        return False

def triangular_number(n):
    """Returns the nth triangular number."""
    try:
        return n * (n + 1) // 2
    except:
        return False

def pentagonal_number(n):
    """Returns the nth pentagonal number."""
    try:
        return n * (3 * n - 1) // 2
    except:
        return False

def hexagonal_number(n):
    """Returns the nth hexagonal number."""
    try:
        return n * (2 * n - 1)
    except:
        return False

def factorial_of_prime(n):
    """Returns the factorial of a prime number."""
    try:
        if is_prime(n):
            return math.factorial(n)
        return False
    except:
        return False

def check_strong_number(number):
    """Returns True if the number is a strong number, else False."""
    try:
        sum_fact = sum(math.factorial(int(digit)) for digit in str(number))
        return sum_fact == number
    except:
        return False

# --------------------------- Probability and Statistics ---------------------------

def mode(numbers):
    """Returns the mode (most frequent value) of a list of numbers."""
    try:
        from collections import Counter
        count = Counter(numbers)
        return count.most_common(1)[0][0]
    except:
        return False

def geometric_mean(numbers):
    """Returns the geometric mean of a list of numbers."""
    try:
        product = 1
        for num in numbers:
            product *= num
        return product ** (1 / len(numbers))
    except:
        return False

# --------------------------- Miscellaneous Functions ---------------------------

def check_palindrome(text):
    """Returns True if the string is a palindrome, else False."""
    try:
        return text == text[::-1]
    except:
        return False

def reverse_string(text):
    """Returns the reversed version of a string."""
    try:
        return text[::-1]
    except:
        return False

def to_lowercase(text):
    """Converts a string to lowercase."""
    try:
        return text.lower()
    except:
        return False

def to_uppercase(text):
    """Converts a string to uppercase."""
    try:
        return text.upper()
    except:
        return False

def unique_elements(numbers):
    """Returns a list of unique elements in a list."""
    try:
        return list(set(numbers))
    except:
        return False
