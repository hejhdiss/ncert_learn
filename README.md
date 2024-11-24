# ncert_learn Module

`ncert_learn` is a comprehensive Python module designed to support NCERT Class 12 Computer Science students. It offers a wide range of utility functions across various topics, including Python programming, MySQL database interactions, mathematical operations, data structures, network security, and more.

---

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

### Variety Types Of Trees
- **Added Classes**: QuadTreeNode,TrieNode,SegmentTree,OctreeNode,Heap,RBTreeNode,BSTNode,AVLNode,BTreeNode.
- **Some Functions OutSide Class**: `bst_insert`,`bst_search`,`bst_inorder`,`avl_insert`,`avl_get_height`,`avl_get_balance`,`avl_left_rotate`,`avl_right_rotate`,`rb_insert`,`rb_insert_fixup`,`rb_left_rotate`,`rb_right_rotate`,`btree_insert`,`btree_insert_non_full`,`btree_split`,`trie_insert`.
---

## Version [5.2.1] - 2024-11-23

### Added
- **Monero Mining Support**: New functions for Monero mining, including pool setup, miner monitoring, and profitability calculations. The mining features are optimized for both CPU and GPU mining.
  - `get_mining_pool_info_monero`: Fetches information about Monero mining pools.
  - `setup_miner_xmrg`: Sets up the XMR-G miner for Monero.
  - `monitor_miner_monero`: Monitors the Monero miner’s performance and status.
  - `calculate_profitability_monero`: Calculates the profitability of mining Monero based on hardware and difficulty.
  - `mine_monero`: Starts the Monero mining process with default settings.
  - `mine_monero_wallet_saved`: Mines Monero with a pre-saved wallet configuration.
  - `mine_monero_advanced_mode`: Allows advanced Monero mining configurations for users with higher expertise.

## Why Monero?

Monero (XMR) was chosen for inclusion in the **ncert_learn** module due to several key factors that make it an ideal choice for mining within this educational module:

### 1. **Privacy and Security**
Monero is well-known for its strong focus on privacy and security. It uses advanced cryptographic techniques, such as ring signatures and stealth addresses, to ensure that transactions remain untraceable and private. This makes it a great choice for users interested in secure and anonymous transactions.

### 2. **Compatibility with Various Hardware**
Monero mining is highly compatible with a range of hardware, including CPU and GPU. This flexibility allows a wide audience of users to participate in mining, whether they have low-end or high-end devices. Additionally, Monero's mining algorithm, RandomX, is optimized for general-purpose CPUs, making it ideal for users with non-specialized hardware.

### 3. **Decentralization**
Monero has a strong emphasis on decentralization, ensuring that mining can be done by a broad group of individuals, rather than a few large mining pools. This helps maintain the integrity and security of the Monero network, making it a valuable choice for users who prioritize decentralization.

### 4. **Mining Efficiency**
Monero's mining algorithm, RandomX, is known for being more efficient on general-purpose hardware compared to many other cryptocurrencies. This makes it a more accessible and practical choice for users who want to mine with minimal investment in specialized mining equipment.

### 5. **Scalability**
Monero has a dynamic block size limit, meaning that it can adjust its block size based on network demand. This feature helps to keep transaction fees low and enables the network to scale more effectively in the future as the number of users and transactions grows.

### 6. **Community and Support**
Monero has a large, active, and dedicated community of developers and miners. This strong community support ensures ongoing development, regular updates, and a collaborative approach to problem-solving, which is important for maintaining a healthy and secure network.

For these reasons, Monero was selected for its combination of privacy, compatibility, decentralization, efficiency, and community support—making it an excellent choice for inclusion in the **ncert_learn** module.


## Important Note

This module has a wide range of functionalities, but it is **optimized for Windows** to ensure all features work properly and efficiently. While it is possible to use the module on other operating systems, for the full experience and to ensure optimal performance, we recommend using **Windows**.

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

We recommend downloading version 5.2.3, as it includes important bug fixes and new features that enhance performance, usability, and stability. Upgrade today for an improved experience.

## How to Upgrade

To upgrade to the latest version of **ncert_learn**:

```bash
pip install --upgrade ncert_learn
```
## Contributions

We welcome contributions to the project. Please fork the repository, create a feature branch, and submit a pull request for review. For any issues or suggestions, feel free to open an issue on the [GitHub repository](https://github.com/hejhdiss/ncert_learn).

## Acknowledgments

A big thank you to the contributors and the community for their support in making this release possible. Special thanks to those who helped with Monero mining features.

For more information, visit the official documentation: [ncert_learn Documentation](https://hejhdiss.github.io/ncert_learn-website/)

You can also find **ncert_learn** on [PyPI](https://pypi.org/project/ncert-learn/).


