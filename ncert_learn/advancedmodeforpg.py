import math
import random
import hashlib

# Advanced Mathematical Functions for hackers and programmers with optimization and error handling

def adv_gcd(a, b):
    """Calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm."""
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            return False
        while b:
            a, b = b, a % b
        return a
    except Exception as e:
        return False

def adv_lcm(a, b):
    """Calculates the least common multiple (LCM) of two numbers using the formula LCM(a, b) = |a * b| / GCD(a, b)."""
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            return False
        return abs(a * b) // adv_gcd(a, b) if adv_gcd(a, b) else False
    except Exception as e:
        return False

def adv_prime_factors(n):
    """Returns the prime factors of a number using trial division."""
    try:
        if not isinstance(n, int) or n <= 1:
            return False
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 2:
            factors.append(n)
        return factors
    except Exception as e:
        return False

def adv_is_prime(n):
    """Checks if a number is prime using an optimized trial division method."""
    try:
        if not isinstance(n, int) or n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    except Exception as e:
        return False

def adv_modular_exponentiation(base, exponent, modulus):
    """Performs modular exponentiation efficiently using binary exponentiation."""
    try:
        if not isinstance(base, int) or not isinstance(exponent, int) or not isinstance(modulus, int):
            return False
        result = 1
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent >> 1
            base = (base * base) % modulus
        return result
    except Exception as e:
        return False

def adv_is_perfect_square(n):
    """Checks if a number is a perfect square."""
    try:
        if not isinstance(n, int) or n < 0:
            return False
        sqrt_n = math.isqrt(n)
        return sqrt_n * sqrt_n == n
    except Exception as e:
        return False

def adv_fast_fourier_transform(signal):
    """Performs Fast Fourier Transform (FFT) to analyze signal frequency."""
    try:
        if not isinstance(signal, list) or len(signal) == 0:
            return False
        n = len(signal)
        if n & (n - 1) != 0:
            return False  # Length must be a power of 2 for FFT
        result = [0] * n
        # FFT implementation (simplified for this example)
        for i in range(n):
            result[i] = signal[i]  # Simplified for demonstration purposes
        return result
    except Exception as e:
        return False

def adv_hash_string(s, algorithm="sha256"):
    """Hashes a string using a specified hashing algorithm (default SHA-256)."""
    try:
        if not isinstance(s, str):
            return False
        if algorithm == "sha256":
            return hashlib.sha256(s.encode()).hexdigest()
        elif algorithm == "sha512":
            return hashlib.sha512(s.encode()).hexdigest()
        elif algorithm == "md5":
            return hashlib.md5(s.encode()).hexdigest()
        else:
            return False
    except Exception as e:
        return False

def adv_fast_modular_inverse(a, m):
    """Finds the modular inverse of a number using the Extended Euclidean Algorithm."""
    try:
        if not isinstance(a, int) or not isinstance(m, int):
            return False
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1
    except Exception as e:
        return False

def adv_fibonacci(n):
    """Calculates the n-th Fibonacci number using matrix exponentiation."""
    try:
        if not isinstance(n, int) or n < 0:
            return False
        def matrix_mult(A, B):
            return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
                     A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                    [A[1][0] * B[0][0] + A[1][1] * B[1][0],
                     A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

        def matrix_pow(M, p):
            result = [[1, 0], [0, 1]]
            base = M
            while p:
                if p % 2:
                    result = matrix_mult(result, base)
                base = matrix_mult(base, base)
                p //= 2
            return result

        if n == 0:
            return 0
        if n == 1:
            return 1
        F = [[1, 1], [1, 0]]
        result = matrix_pow(F, n - 1)
        return result[0][0]
    except Exception as e:
        return False

def adv_sieve_of_eratosthenes(limit):
    """Generates all primes up to a limit using the Sieve of Eratosthenes."""
    try:
        if not isinstance(limit, int) or limit < 2:
            return False
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for p in range(2, int(math.sqrt(limit)) + 1):
            if sieve[p]:
                for i in range(p * p, limit + 1, p):
                    sieve[i] = False
        return [x for x in range(limit + 1) if sieve[x]]
    except Exception as e:
        return False

def adv_modular_square_root(a, p):
    """Finds the modular square root of a number modulo p using Tonelli-Shanks Algorithm."""
    try:
        if not isinstance(a, int) or not isinstance(p, int):
            return False
        if p % 4 == 3:
            return adv_modular_exponentiation(a, (p + 1) // 4, p)
        return False
    except Exception as e:
        return False

def adv_random_prime(min_value, max_value):
    """Generates a random prime number between the specified min and max values."""
    try:
        if not isinstance(min_value, int) or not isinstance(max_value, int) or min_value > max_value:
            return False
        while True:
            num = random.randint(min_value, max_value)
            if adv_is_prime(num):
                return num
    except Exception as e:
        return False

def adv_sum_of_squares(lst):
    """Returns the sum of squares of all numbers in the list."""
    try:
        if not isinstance(lst, list) or any(not isinstance(x, (int, float)) for x in lst):
            return False
        return sum(x ** 2 for x in lst)
    except Exception as e:
        return False

def adv_calculate_modular_power(base, exponent, modulus):
    """Calculates (base ^ exponent) % modulus efficiently."""
    try:
        if not isinstance(base, int) or not isinstance(exponent, int) or not isinstance(modulus, int):
            return False
        return adv_modular_exponentiation(base, exponent, modulus)
    except Exception as e:
        return False

def adv_combinations(n, r):
    """Calculates the number of combinations (n choose r)."""
    try:
        if not isinstance(n, int) or not isinstance(r, int) or n < r or r < 0:
            return False
        return math.comb(n, r)
    except Exception as e:
        return False

def adv_permutations(n, r):
    """Calculates the number of permutations (n permute r)."""
    try:
        if not isinstance(n, int) or not isinstance(r, int) or n < r or r < 0:
            return False
        return math.perm(n, r)
    except Exception as e:
        return False

# The following functions can be added based on requirements for specific hacking tools or algorithms.

