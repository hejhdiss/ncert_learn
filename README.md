# ncert_learn Module

`ncert_learn` is a comprehensive Python module designed to support NCERT Class 12 Computer Science students. It offers a wide range of utility functions across various topics, including Python programming, MySQL database interactions, mathematical operations, data structures, network security, and more.

## Key Features

### Mathematical Functions
- **Prime number check**: Check if a number is prime.
- **Armstrong, Strong, Niven, and Palindrome checks**: Check for various types of numbers.
- **Fibonacci numbers, even/odd checks**: Compute Fibonacci series, check even/odd.
- **Advanced functions**: GCD, LCM, prime factorization, modular exponentiation, fast Fourier transform.
- **New Advanced Functions**: adv_gcd, adv_lcm, adv_prime_factors, adv_is_prime.

### Trigonometric Functions
- **Sine, Cosine, Tangent**: Computes trigonometric values.
- **Inverse Sine, Cosine, Tangent**: Computes inverse trigonometric values.

### Geometric Calculations
- **Area and volume for various shapes** like circles, rectangles, triangles, spheres, and cylinders.

### Mathematical Functions
- **Quadratic roots, power, logarithm, factorial, gcd, lcm, binomial coefficient, derivative, definite integral, series sum**.
- **Advanced Mathematical Functions**: Cube root, nth root, exponential, modular inverse, absolute value, rounding, ceiling, flooring.

### Number Theory Functions
- **Prime Factors, Fibonacci, Perfect Numbers, Palindrome, Sum of Divisors, Abundant Numbers, Deficient Numbers, Triangular Numbers, Square Numbers**, and more.

### Data Structures
- **Stack Operations**: Push, pop, peek, and display.
- **Sorting Algorithms**: Bubble Sort, Insertion Sort.

### MySQL Operations
- **Manage databases and tables.**
- **Execute queries with optimized database management** (`mysql_execute_advanced_mode`).

### File Handling
- **Text, binary, and CSV file management.**
- **ZIP file operations**: Compress, extract, list contents.

### System Utilities
- **Fetch system information, manage services like XAMPP MySQL/Apache**.

### Numerical Functions
- **Mathematical operations**: `numerical_add`, `numerical_subtract`, `numerical_multiply`, `numerical_divide`.
- **Advanced numerical computations**: `numerical_zeros`, `numerical_ones`, `numerical_reshape`, `numerical_dot`, `numerical_inv`, `numerical_det`, `numerical_svd`.
- **Statistical functions**: `numerical_mean`, `numerical_median`, `numerical_variance`, `numerical_std`.

### Cryptographic Functions
- **Encoding/Decoding**: Base64, Hex, Caesar cipher, and more.
- **Advanced encoding methods** like Base58, URL encoding, Huffman encoding, etc.

### Machine Learning Functions
- **Preprocessing**: Handle missing values, normalize, standardize data.
- **Create and evaluate models**: Linear regression, decision trees, random forests.
- **Metrics**: Accuracy, mean squared error.
- **Visualization**: Feature importance, decision boundaries.

### API Functions
- **CRUD operations for item management**: `api_create_item`, `api_read_item`, `api_update_item`, `api_delete_item`.
- **User management**: `api_create_user`, `api_authenticate_user`, `api_upload_file`, `api_bulk_insert_items`.

### Search Algorithms
- **Binary Search, Linear Search, Jump Search, Exponential Search, Ternary Search, Interpolation Search**.

### Code Quality Tools
- **Format and lint Python code**: `format_code`, `lint_code`, `check_code_quality`.

---

## Version [5.0.1] - 2024-11-23

### Added

#### Set Operations
- **set_create**: Creates a new set.
- **set_add**: Adds an element to the set.
- **set_remove**: Removes an element from the set.
- **set_discard**: Removes an element from the set if it exists, without throwing an error.
- **set_is_member**: Checks if an element is present in the set.
- **set_size**: Returns the size of the set.
- **set_clear**: Clears all elements in the set.

#### Queue Operations
- **queue_create**: Creates a new queue.
- **queue_enqueue**: Adds an element to the end of the queue.
- **queue_dequeue**: Removes and returns the element from the front of the queue.
- **queue_peek**: Returns the element at the front of the queue without removing it.
- **queue_is_empty**: Checks if the queue is empty.
- **queue_size**: Returns the size of the queue.
- **queue_clear**: Clears all elements in the queue.

#### Dictionary Operations
- **dict_create**: Creates a new dictionary.
- **dict_add**: Adds a key-value pair to the dictionary.
- **dict_get**: Retrieves the value for a given key.
- **dict_remove**: Removes a key-value pair from the dictionary.
- **dict_key_exists**: Checks if a key exists in the dictionary.
- **dict_get_keys**: Returns all keys in the dictionary.
- **dict_get_values**: Returns all values in the dictionary.
- **dict_size**: Returns the size of the dictionary.
- **dict_clear**: Clears all key-value pairs in the dictionary.

#### Tree Operations
- **tree_insert**: Inserts a node into the tree.
- **tree_inorder**: Performs an inorder traversal of the tree.
- **tree_search**: Searches for a node in the tree.
- **tree_minimum**: Finds the minimum value in the tree.
- **tree_maximum**: Finds the maximum value in the tree.
- **tree_size**: Returns the number of nodes in the tree.
- **tree_height**: Returns the height of the tree.
- **tree_level_order**: Performs a level order traversal of the tree.
- **tree_postorder**: Performs a postorder traversal of the tree.
- **tree_preorder**: Performs a preorder traversal of the tree.
- **tree_breadth_first**: Performs a breadth-first search in the tree.
- **tree_depth_first**: Performs a depth-first search in the tree.
- **tree_delete**: Deletes a node from the tree.

---

### Network Security & Utilities

This module includes functionalities for SQL injection testing, network scanning, and local service management. It integrates tools such as **sqlmap**, **nmap**, and **XAMPP** to help users perform security-related tasks and manage services effectively.

---

## Installation

To install `ncert_learn`, use pip:

```bash
pip install ncert_learn
```
Alternatively, clone the repository and install manually:

```bash
git clone https://github.com/hejhdiss/ncert_learn.git
cd ncert_learn
python setup.py install
```
## Disclaimer

This module is intended for educational purposes only. Using this module for any illegal activities is strictly prohibited. The authors and contributors are not responsible for any misuse of the module.

## Changelog

All notable changes to this project are documented in the [Changelog](https://github.com/hejhdiss/ncert_learn/blob/main/CHANGELOG.md).

## Recommendation

We recommend downloading version 5.0.1, as it includes important bug fixes and new features that enhance performance, usability, and stability. Upgrade today for an improved experience.



