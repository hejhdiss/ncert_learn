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


# Cryptographic Functions and Information Retrieval Utilities

This section of the project provides cryptographic functions for encoding, decoding, and encryption, as well as utilities to fetch details about IP addresses and phone numbers.

## Cryptographic Functions

The script includes several cryptographic functions to perform common operations such as encoding, decoding, and encryption.

---

## Get Info Functions

These functions allow you to retrieve details about IP addresses and phone numbers.

### `get_ip_details(ip)`

### `get_phone_number_details(phone_number)`

---

### Merge Sort

Merge Sort is a classic **divide-and-conquer** sorting algorithm that works by recursively dividing the input list into two halves until each sublist contains a single element or is empty. Once the sublists are individual or empty, they are merged back together in sorted order. This merging step ensures that the final list is sorted in a highly efficient manner.

- **Time Complexity**: O(n log n) in all cases (best, average, and worst). This consistent time complexity makes Merge Sort highly reliable for large datasets and ensures predictable performance.
- **Space Complexity**: O(n) due to the additional memory required for storing the temporary sublists during the merge process.

Merge Sort is particularly advantageous when dealing with **large datasets** or when a stable sort (where elements with equal values maintain their original relative order) is required. However, it does require additional memory, which can be a limitation in memory-constrained environments. Merge Sort is also one of the **recommended algorithms** for sorting linked lists because it does not require random access to elements, unlike other sorting algorithms such as Quick Sort.

#### Use Case:
Merge Sort is optimal for external sorting, such as when data exceeds the available memory and is stored in external devices (like hard drives or databases), because it efficiently handles data that doesn’t fit entirely into memory at once.

### Quick Sort

Quick Sort is another **divide-and-conquer** algorithm but operates differently. It works by selecting a **pivot** element, then partitioning the list such that elements smaller than the pivot go to the left, and those greater go to the right. This partitioning step ensures that the pivot is placed in its correct sorted position. The sublists (left and right of the pivot) are then recursively sorted.

- **Time Complexity**: O(n log n) on average, but can degrade to O(n²) if the pivot selection is poor (for example, when the smallest or largest element is consistently chosen as the pivot).
- **Space Complexity**: O(log n) for the recursive stack in the average case. However, in the worst case (when the pivot is poorly chosen), the space complexity can degrade to O(n).

Quick Sort is generally faster than Merge Sort for most practical datasets, especially when implemented with a good pivot selection strategy (e.g., random pivot or median-of-three). It is a highly efficient algorithm for **in-memory sorting** due to its low overhead. However, its worst-case performance can be a drawback when sorting already sorted or nearly sorted data.

#### Advantages:
- Faster in practice than Merge Sort for most datasets.
- **In-place sorting**: Unlike Merge Sort, Quick Sort does not require additional memory for storing sublists, making it more memory efficient in terms of space.

#### Disadvantages:
- Worst-case time complexity can degrade to O(n²) when pivot selection is poor.
- Not a stable sort, meaning equal elements may not maintain their relative order.

#### Optimizations:
To avoid the worst-case time complexity, modern implementations of Quick Sort use techniques such as **randomized pivoting** or **median-of-three pivot selection** to improve performance on average.

#### Use Case:
Quick Sort is generally preferred when sorting data that fits in memory and when average performance is critical. It is a great option for **sorting arrays or lists** where speed is crucial and space overhead is a concern.

### Conclusion

Both Merge Sort and Quick Sort are **efficient and widely used sorting algorithms**, each with its unique advantages and trade-offs. 

- **Merge Sort** is optimal for large datasets and guarantees consistent performance, making it suitable for scenarios like external sorting.
- **Quick Sort**, although subject to worst-case scenarios, is often the go-to choice for fast, in-memory sorting due to its lower space complexity and faster average-case performance.

Depending on the specific requirements (e.g., memory availability, stability, data size), one may be more suitable than the other for a particular application.

---

## Version [5.5.7] - 2025-01-22

### Updated
- **ytdownloaderrunner**:Removed YoutubeDownloader(Windows Only) `run_youtube_downloader`.


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

We recommend downloading version 5.5.4, as it includes important bug fixes and new features that enhance performance, usability, and stability. Upgrade today for an improved experience.

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


