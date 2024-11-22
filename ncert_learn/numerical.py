import numpy as np
from numpy.linalg import LinAlgError

# Mathematical Operations
def numerical_add(arr1, arr2):
    """
    Adds two arrays element-wise.

    :param arr1: First input array
    :param arr2: Second input array
    :return: Resultant array after element-wise addition
    :raises ValueError: If arrays have different shapes
    """
    try:
        if arr1.shape != arr2.shape:
            raise ValueError("Arrays must have the same shape for element-wise addition.")
        return np.add(arr1, arr2)
    except Exception as e:
        return str(e)


def numerical_subtract(arr1, arr2):
    """
    Subtracts second array from the first array element-wise.

    :param arr1: First input array
    :param arr2: Second input array
    :return: Resultant array after element-wise subtraction
    :raises ValueError: If arrays have different shapes
    """
    try:
        if arr1.shape != arr2.shape:
            raise ValueError("Arrays must have the same shape for element-wise subtraction.")
        return np.subtract(arr1, arr2)
    except Exception as e:
        return str(e)


def numerical_multiply(arr1, arr2):
    """
    Multiplies two arrays element-wise.

    :param arr1: First input array
    :param arr2: Second input array
    :return: Resultant array after element-wise multiplication
    :raises ValueError: If arrays have different shapes
    """
    try:
        if arr1.shape != arr2.shape:
            raise ValueError("Arrays must have the same shape for element-wise multiplication.")
        return np.multiply(arr1, arr2)
    except Exception as e:
        return str(e)


def numerical_divide(arr1, arr2):
    """
    Divides the first array by the second array element-wise.

    :param arr1: First input array
    :param arr2: Second input array
    :return: Resultant array after element-wise division
    :raises ValueError: If arrays have different shapes
    :raises ZeroDivisionError: If division by zero occurs
    """
    try:
        if arr1.shape != arr2.shape:
            raise ValueError("Arrays must have the same shape for element-wise division.")
        if np.any(arr2 == 0):
            raise ZeroDivisionError("Division by zero encountered.")
        return np.divide(arr1, arr2)
    except Exception as e:
        return str(e)


# Array Creation and Manipulation
def numerical_zeros(shape):
    """
    Creates an array of zeros with the given shape.

    :param shape: Shape of the array to be created
    :return: Array filled with zeros
    """
    try:
        return np.zeros(shape)
    except Exception as e:
        return str(e)


def numerical_ones(shape):
    """
    Creates an array of ones with the given shape.

    :param shape: Shape of the array to be created
    :return: Array filled with ones
    """
    try:
        return np.ones(shape)
    except Exception as e:
        return str(e)


def numerical_reshape(arr, new_shape):
    """
    Reshapes the input array to a new shape.

    :param arr: Input array
    :param new_shape: New shape for the array
    :return: Reshaped array
    :raises ValueError: If the total number of elements does not match
    """
    try:
        return np.reshape(arr, new_shape)
    except Exception as e:
        return str(e)


# Linear Algebra Operations
def numerical_dot(arr1, arr2):
    """
    Computes the dot product of two arrays.

    :param arr1: First array
    :param arr2: Second array
    :return: Dot product of arr1 and arr2
    :raises ValueError: If the shapes are incompatible for dot product
    """
    try:
        return np.dot(arr1, arr2)
    except Exception as e:
        return str(e)


def numerical_inv(arr):
    """
    Computes the inverse of a matrix.

    :param arr: Input matrix
    :return: Inverse of the matrix
    :raises ValueError: If the matrix is singular and cannot be inverted
    """
    try:
        return np.linalg.inv(arr)
    except LinAlgError:
        return "Matrix is singular and cannot be inverted."
    except Exception as e:
        return str(e)


def numerical_det(arr):
    """
    Computes the determinant of a matrix.

    :param arr: Input matrix
    :return: Determinant of the matrix
    :raises ValueError: If the matrix is not square
    """
    try:
        return np.linalg.det(arr)
    except Exception as e:
        return str(e)


# Random Sampling Functions
def numerical_randint(low, high, size):
    """
    Returns random integers from low (inclusive) to high (exclusive).

    :param low: Lower bound for integers
    :param high: Upper bound for integers
    :param size: Number of integers to generate
    :return: Array of random integers
    :raises ValueError: If low >= high
    """
    try:
        if low >= high:
            raise ValueError("Low bound must be less than high bound.")
        return np.random.randint(low, high, size)
    except Exception as e:
        return str(e)


def numerical_randn(size):
    """
    Returns an array of random values sampled from a standard normal distribution.

    :param size: Size of the desired array
    :return: Array of random values from the standard normal distribution
    """
    try:
        return np.random.randn(size)
    except Exception as e:
        return str(e)


# Statistical Operations
def numerical_mean(arr):
    """
    Computes the mean of the array.

    :param arr: Input array
    :return: Mean of the array
    """
    try:
        return np.mean(arr)
    except Exception as e:
        return str(e)


def numerical_median(arr):
    """
    Computes the median of the array.

    :param arr: Input array
    :return: Median of the array
    """
    try:
        return np.median(arr)
    except Exception as e:
        return str(e)


def numerical_variance(arr):
    """
    Computes the variance of the array.

    :param arr: Input array
    :return: Variance of the array
    """
    try:
        return np.var(arr)
    except Exception as e:
        return str(e)


def numerical_std(arr):
    """
    Computes the standard deviation of the array.

    :param arr: Input array
    :return: Standard deviation of the array
    """
    try:
        return np.std(arr)
    except Exception as e:
        return str(e)


# String Operations
def numerical_string_length(arr):
    """
    Computes the length of each string in the array.

    :param arr: Array of strings
    :return: Array of string lengths
    """
    try:
        return np.char.str_len(arr)
    except Exception as e:
        return str(e)


def numerical_string_upper(arr):
    """
    Converts all strings in the array to uppercase.

    :param arr: Array of strings
    :return: Array of strings in uppercase
    """
    try:
        return np.char.upper(arr)
    except Exception as e:
        return str(e)


def numerical_string_lower(arr):
    """
    Converts all strings in the array to lowercase.

    :param arr: Array of strings
    :return: Array of strings in lowercase
    """
    try:
        return np.char.lower(arr)
    except Exception as e:
        return str(e)


# Advanced Linear Algebra
def numerical_svd(arr):
    """
    Performs singular value decomposition (SVD) on a matrix.

    :param arr: Input matrix
    :return: Tuple containing the singular values and matrices from the SVD
    """
    try:
        return np.linalg.svd(arr)
    except Exception as e:
        return str(e)

