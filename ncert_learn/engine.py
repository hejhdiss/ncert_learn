import ctypes
import os
import numpy as np
import pickle

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct paths to the DLLs dynamically
tensor_ops_path = os.path.join(script_dir, 'engine\\tensor_operations.dll')
nn_layers_path = os.path.join(script_dir, 'engine\\neural_network_layers.dll')
optimizers_path = os.path.join(script_dir, 'engine\\optimizers.dll')
loss_funcs_path = os.path.join(script_dir, 'engine\\loss_functions.dll')

# Load DLLs dynamically with error handling
def load_dll(dll_path):
    if not os.path.exists(dll_path):
        raise FileNotFoundError(f"Missing DLL: {dll_path}")
    try:
        return ctypes.CDLL(dll_path)
    except OSError as e:
        raise RuntimeError(f"Error loading DLL '{dll_path}': {e}")

tensor_ops = load_dll(tensor_ops_path)
nn_layers = load_dll(nn_layers_path)
optimizers = load_dll(optimizers_path)
loss_funcs = load_dll(loss_funcs_path)

# Define ctypes function prototypes if necessary
# [Other function definitions remain unchanged]

# Python-based Model Serialization
def save_model(filename, weights):
    with open(filename, 'wb') as file:
        pickle.dump(weights, file)

def engine_save_model(filename, weights, size):

    """
    Saves the model weights to a file.

    Args:
        filename: The path to the file to save the model to.
        weights: The weights to save.
        size: The size of the weights array.

    Returns:
        None
    """
    

    save_model(filename, weights)

def load_model(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Model file not found: {filename}")
    with open(filename, 'rb') as file:
        return pickle.load(file)

def engine_load_model(filename, weights, size):

    """
    Loads a saved model from a file and copies it into the given 'weights' array.

    Args:
        filename: The name of the file to load the model from.
        weights: The output array where the loaded model is stored.
        size: The size of the model to be loaded.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the size of the loaded model does not match the given size.
    """

    loaded_weights = load_model(filename)
    if len(loaded_weights) != size:
        raise ValueError("Mismatch in model size during load.")
    np.copyto(weights, loaded_weights)

# Helper Functions
def tensor_add(A, B, C, n):
    tensor_ops.engine_tensor_add(
        A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        C.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        n
    )

def engine_tensor_add(A, B, C, n):

    """
    Computes the element-wise sum of two vectors A and B, and stores the result in vector C.

    Args:
        A: The first input vector.
        B: The second input vector.
        C: The output vector where the result is stored.
        n: The size of the input vectors.
    """

    tensor_add(A, B, C, n)

def tensor_dot(A, B, C, n):
    tensor_ops.engine_tensor_dot(
        A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        C.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        n
    )

def engine_tensor_dot(A, B, C, n):

    """
    Computes the dot product of two vectors A and B, and stores the result in vector C.

    Args:
        A: The first vector.
        B: The second vector.
        C: The output vector where the result is stored.
        n: The length of the vectors.
    """

    tensor_dot(A, B, C, n)

def sigmoid_activation(input, output, n):

    nn_layers.engine_sigmoid_activation(
        input.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        output.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        n
    )

def engine_sigmoid_activation(input, output, n):

    """
    Applies the sigmoid activation function to the input data.

    Args:
        input: The input array.
        output: The output array where the result is stored.
        n: The number of elements in the input and output arrays.

    Returns:
        None
    """
    

    sigmoid_activation(input, output, n)

def dense_layer(input, weights, bias, output, input_size, output_size):
    nn_layers.engine_dense_layer(
        input.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        weights.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        bias.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        output.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        input_size, output_size
    )

def engine_dense_layer(input, weights, bias, output, input_size, output_size):

    """
    Executes a dense (fully connected) layer operation on the input data.

    Args:
        input: The input data for the dense layer.
        weights: The weight matrix of the dense layer.
        bias: The bias vector of the dense layer.
        output: The output array where the result is stored.
        input_size: The size of the input vector.
        output_size: The size of the output vector.

    Returns:
        None
    """

    dense_layer(input, weights, bias, output, input_size, output_size)

def sgd_optimizer(params, grads, learning_rate, n):
    optimizers.engine_sgd_optimizer(
        params.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        grads.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        learning_rate, n
    )

def engine_sgd_optimizer(params, grads, learning_rate, n):

    """
    Updates the parameters based on the gradients and learning rate.

    Args:
        params: The model parameters to be updated.
        grads: The gradients of the model parameters.
        learning_rate: The learning rate used in the optimization process.
        n: The total number of elements in the params and grads arrays.

    Returns:
        None
    """

    sgd_optimizer(params, grads, learning_rate, n)

def mse_loss(prediction, target, loss, n):
    loss_funcs.engine_mse_loss(
        prediction.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        target.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        loss.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        n
    )

def engine_mse_loss(prediction, target, loss, n):

    """
    Computes the mean squared error between the prediction and target vectors.

    Args:
        prediction: The output of the model.
        target: The target values.
        loss: The output array where the loss is stored.
        n: The number of elements in the prediction and target arrays.

    Returns:
        None
    """

    mse_loss(prediction, target, loss, n)

# Testing Functions
def test_engine_functions():

    """
    Tests various engine functions for correctness.

    This function performs the following tests:
    - engine_tensor_add: Adds two vectors A and B, stores the result in C, and prints it.
    - engine_tensor_dot: Computes the dot product of vectors A and B, stores the result in C, and prints it.
    - engine_sigmoid_activation: Applies the sigmoid activation function to input_data, stores the result in output_data, and prints it.
    - engine_save_model and engine_load_model: Saves model_weights to a file, loads them back, and verifies the integrity of the saved and loaded weights.

    Raises:
        AssertionError: If the saved and loaded model weights do not match.
    """

    n = 5
    A = np.random.rand(n).astype(np.float32)
    B = np.random.rand(n).astype(np.float32)
    C = np.zeros_like(A)

    print("Testing engine_tensor_add...")
    engine_tensor_add(A, B, C, n)
    print(f"Result (A + B): {C}")

    print("\nTesting engine_tensor_dot...")
    engine_tensor_dot(A, B, C, n)
    print(f"Result (A * B): {C}")

    print("\nTesting engine_sigmoid_activation...")
    input_data = np.random.rand(n).astype(np.float32)
    output_data = np.zeros_like(input_data)
    engine_sigmoid_activation(input_data, output_data, n)
    print(f"Result (Sigmoid): {output_data}")

    print("\nTesting engine_save_model and engine_load_model...")
    model_weights = np.random.rand(n).astype(np.float32)
    engine_save_model("test_model.dat", model_weights, n)
    loaded_weights = np.zeros(n, dtype=np.float32)
    engine_load_model("test_model.dat", loaded_weights, n)
    print(f"Saved Weights: {model_weights}")
    print(f"Loaded Weights: {loaded_weights}")
    assert np.allclose(model_weights, loaded_weights), "Save/Load Model Failed!"
    print("Save/Load Model Passed!")


