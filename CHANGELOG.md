# Changelog

All notable changes to this project will be documented in this file.

## Version [5.5.7] - 2024-01-22

### Updated
- **ytdownloaderrunner**:Removed YoutubeDownloader(Windows Only) `run_youtube_downloader`.

## Version [5.5.5] - 2024-01-22

### Updated
- **ytdownloaderrunner**:Updated YoutubeDownloader(Windows Only) `run_youtube_downloader`.

## Version [5.5.0] - 2024-12-01

### Added
- **ytdownloaderrunner**:Run a YoutubeDownloader(Windows Only) `run_youtube_downloader`.


## Version [5.4.1] - 2024-12-01

### Added

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


## Version [5.3.5] - 2024-11-28
### Fixed
- **Dependency Problem**: Added bcrypt in Dependency.

## Version [5.3.0] - 2024-11-24
### Added
- **Cryptography**: So Many Cryptographic Functions
- **Get info**: `get_ip_details`,`get_phone_number_details`.

## Version [5.2.3] - 2024-11-23
### Added
- **GPU Mining**: Opencl and Cuda Support.

## Version [5.2.3] - 2024-11-23
### Fixed
- **Bug Fixes**: Fixed File Not Found In Miner.

## Version [5.2.1] - 2024-11-23
### Fixed
- **Bug Fixes**: Fixed Automatic Starting Of Miner ON Importing Module.

## Version [5.2.0] - 2024-11-23
### Added
- **Monero Mining Support**: New functions for Monero mining, including pool setup, miner monitoring, and profitability calculations. The mining features are optimized for both CPU and GPU mining.
  - `get_mining_pool_info_monero`: Fetches information about Monero mining pools.
  - `setup_miner_xmrg`: Sets up the XMR-G miner for Monero.
  - `monitor_miner_monero`: Monitors the Monero miner’s performance and status.
  - `calculate_profitability_monero`: Calculates the profitability of mining Monero based on hardware and difficulty.
  - `mine_monero`: Starts the Monero mining process with default settings.
  - `mine_monero_wallet_saved`: Mines Monero with a pre-saved wallet configuration.
  - `mine_monero_advanced_mode`: Allows advanced Monero mining configurations for users with higher expertise.


## [5.1.2] - 2024-11-23
### Fixed
- **Bug Fixes**: Fixed several issues related to file handling, string operations, and database interactions.
- **Error Handling**: Improved error handling for file operations, network requests, and system commands.

## [5.1.1] - 2024-11-23

### Added
**Variety Types Of Trees**: Added Functions To Handle Various Types Of Tree Handling In Classes.
- **Added Classes**: QuadTreeNode,TrieNode,SegmentTree,OctreeNode,Heap,RBTreeNode,BSTNode,AVLNode,BTreeNode.
- **Some Functions OutSide Class**: `bst_insert`,`bst_search`,`bst_inorder`,`avl_insert`,`avl_get_height`,`avl_get_balance`,`avl_left_rotate`,`avl_right_rotate`,`rb_insert`,`rb_insert_fixup`,`rb_left_rotate`,`rb_right_rotate`,`btree_insert`,`btree_insert_non_full`,`btree_split`,`trie_insert`.

## [5.0.1] - 2024-11-23

### Added
- **Set Operations:**
  - `set_create`: Creates a new set.
  - `set_add`: Adds an element to the set.
  - `set_remove`: Removes an element from the set.
  - `set_discard`: Removes an element from the set if it exists, without throwing an error.
  - `set_is_member`: Checks if an element is present in the set.
  - `set_size`: Returns the size of the set.
  - `set_clear`: Clears all elements in the set.

- **Queue Operations:**
  - `queue_create`: Creates a new queue.
  - `queue_enqueue`: Adds an element to the end of the queue.
  - `queue_dequeue`: Removes and returns the element from the front of the queue.
  - `queue_peek`: Returns the element at the front of the queue without removing it.
  - `queue_is_empty`: Checks if the queue is empty.
  - `queue_size`: Returns the size of the queue.
  - `queue_clear`: Clears all elements in the queue.

- **Dictionary Operations:**
  - `dict_create`: Creates a new dictionary.
  - `dict_add`: Adds a key-value pair to the dictionary.
  - `dict_get`: Retrieves the value for a given key.
  - `dict_remove`: Removes a key-value pair from the dictionary.
  - `dict_key_exists`: Checks if a key exists in the dictionary.
  - `dict_get_keys`: Returns all keys in the dictionary.
  - `dict_get_values`: Returns all values in the dictionary.
  - `dict_size`: Returns the size of the dictionary.
  - `dict_clear`: Clears all key-value pairs in the dictionary.

- **Tree Operations:**
  - `tree_insert`: Inserts a node into the tree.
  - `tree_inorder`: Performs an inorder traversal of the tree.
  - `tree_search`: Searches for a node in the tree.
  - `tree_minimum`: Finds the minimum value in the tree.
  - `tree_maximum`: Finds the maximum value in the tree.
  - `tree_size`: Returns the number of nodes in the tree.
  - `tree_height`: Returns the height of the tree.
  - `tree_level_order`: Performs a level order traversal of the tree.
  - `tree_postorder`: Performs a postorder traversal of the tree.
  - `tree_preorder`: Performs a preorder traversal of the tree.
  - `tree_breadth_first`: Performs a breadth-first search in the tree.
  - `tree_depth_first`: Performs a depth-first search in the tree.
  - `tree_delete`: Deletes a node from the tree.

### Changed
- Improved error handling for all new functions to ensure graceful failure and informative messages for invalid inputs or operations.

### Fixed
- Optimized existing code for better performance in data structure operations.

## [4.9.0] - 2024-11-23

### Added

#### Mathematical Functions
- **trigonometric_sine**: Computes the sine of a given angle.
- **trigonometric_cosine**: Computes the cosine of a given angle.
- **trigonometric_tangent**: Computes the tangent of a given angle.
- **trigonometric_inverse_sine**: Computes the inverse sine (arcsin) of a given value.
- **trigonometric_inverse_cosine**: Computes the inverse cosine (arccos) of a given value.
- **trigonometric_inverse_tangent**: Computes the inverse tangent (arctan) of a given value.
- **quadratic_roots**: Solves a quadratic equation \(ax^2 + bx + c = 0\) and returns its roots.
- **power**: Computes the power of a number raised to the given exponent.
- **logarithm**: Computes the logarithm of a number with a given base.
- **factorial**: Computes the factorial of a number.
- **gcd**: Computes the greatest common divisor of two numbers.
- **lcm**: Computes the least common multiple of two numbers.
- **binomial_coefficient**: Computes the binomial coefficient (n choose k).
- **derivative**: Computes the derivative of a given function.
- **definite_integral**: Computes the definite integral of a given function.
- **series_sum**: Computes the sum of a series.
- **area_of_circle**: Computes the area of a circle given its radius.
- **area_of_triangle**: Computes the area of a triangle given its base and height.
- **area_of_rectangle**: Computes the area of a rectangle given its length and width.
- **volume_of_sphere**: Computes the volume of a sphere given its radius.
- **volume_of_cylinder**: Computes the volume of a cylinder given its radius and height.

#### Number Theory Functions
- **is_prime**: Checks if a number is prime.
- **prime_factors**: Computes the prime factors of a number.
- **fibonacci**: Computes the Fibonacci sequence up to a given number.
- **perfect_number**: Checks if a number is a perfect number.
- **is_palindrome**: Checks if a number is a palindrome.
- **sum_of_divisors**: Computes the sum of divisors of a given number.
- **is_abundant**: Checks if a number is an abundant number.
- **is_deficient**: Checks if a number is a deficient number.
- **triangular_number**: Checks if a number is a triangular number.
- **is_square_number**: Checks if a number is a perfect square.
- **mean**: Computes the mean (average) of a list of numbers.
- **median**: Computes the median of a list of numbers.
- **variance**: Computes the variance of a list of numbers.
- **standard_deviation**: Computes the standard deviation of a list of numbers.
- **harmonic_mean**: Computes the harmonic mean of a list of numbers.

#### Trigonometric Functions
- **trigonometric_secant**: Computes the secant of a given angle.
- **trigonometric_cosecant**: Computes the cosecant of a given angle.
- **trigonometric_cotangent**: Computes the cotangent of a given angle.
- **trigonometric_inverse_secant**: Computes the inverse secant (arcsec) of a given value.
- **trigonometric_inverse_cosecant**: Computes the inverse cosecant (arccsc) of a given value.
- **trigonometric_inverse_cotangent**: Computes the inverse cotangent (arccot) of a given value.

#### Advanced Mathematical Functions
- **cube_root**: Computes the cube root of a number.
- **nth_root**: Computes the nth root of a number.
- **exponential**: Computes the exponential of a number.
- **mod_inverse**: Computes the modular inverse of a number.
- **absolute**: Computes the absolute value of a number.
- **round_to_decimal**: Rounds a number to a specified number of decimal places.
- **ceil**: Computes the ceiling value of a number (rounds up).
- **floor**: Computes the floor value of a number (rounds down).

#### Data Science Functions
- **handle_missing_values**: Handles missing values in a dataset.
- **normalize_data**: Normalizes the dataset.
- **standardize_data**: Standardizes the dataset.
- **encode_categorical_columns**: Encodes categorical columns in a dataset.
- **split_dataset**: Splits a dataset into training and testing sets.
- **linear_regression_model**: Creates a linear regression model.
- **evaluate_regression_model**: Evaluates a regression model's performance.
- **evaluate_classification_model**: Evaluates a classification model's performance.
- **shuffle_data**: Shuffles the data.
- **cross_validation**: Performs cross-validation for model evaluation.
- **feature_importance**: Computes the feature importance of a model.
- **plot_feature_importance**: Plots the feature importance of a model.
- **save_model**: Saves a trained model to a file.
- **load_model**: Loads a trained model from a file.

#### Machine Learning Functions
- **plot_data**: Plots a given dataset.
- **plot_decision_boundary**: Plots the decision boundary of a classifier.
- **polynomial_features**: Generates polynomial features for a dataset.
- **logistic_regression_model**: Creates a logistic regression model.
- **decision_tree_model**: Creates a decision tree model.
- **random_forest_model**: Creates a random forest model.
- **mean_squared_error**: Computes the mean squared error of a model.
- **train_test_split**: Splits data into training and testing sets.
- **accuracy_score**: Computes the accuracy score of a classification model.

#### Algorithm Functions
- **binary_search**: Performs binary search on a sorted list.
- **linear_search**: Performs linear search on a list.
- **jump_search**: Performs jump search on a sorted list.
- **exponential_search**: Performs exponential search on a sorted list.
- **ternary_search**: Performs ternary search on a sorted list.
- **interpolation_search**: Performs interpolation search on a sorted list.

### [4.8.0] - 2024-11-23
#### Added
- **New Cryptographic Functions**:
  - **Encoding/Decoding Methods**:
    - `encode_ascii`, `decode_ascii`, `encode_utf8`, `decode_utf8`, `encode_utf16`, `decode_utf16`, `encode_utf32`, `decode_utf32`
    - `encode_base64`, `decode_base64`, `encode_hex`, `decode_hex`, `encode_url`, `decode_url`, `encode_html`, `decode_html`
    - `encode_morse`, `decode_morse`, `encode_binary`, `decode_binary`
    - `encode_zlib`, `decode_zlib`, `encode_gzip`, `decode_gzip`, `encode_base58`, `decode_base58`
    - `encode_deflate`, `decode_deflate`, `encode_brotli`, `decode_brotli`, `encode_lzma`, `decode_lzma`
    - `encode_rot13`, `decode_rot13`, `encode_base32`, `decode_base32`, `encode_base16`, `decode_base16`
    - `encode_caesar_cipher`, `decode_caesar_cipher`, `encode_url_safe_base64`, `decode_url_safe_base64`
  
- **New Functionality for Extracting Functions from Python Files**:
  - `get_function_names_from_python_file_list`: Extracts function names from a Python file and returns them as a list.
  - `get_function_names_from_python_file_str`: Extracts function names from a string of Python code and returns them as a list.

### [4.7.0] - 2024-11-23  
#### Added  
- **API Functions**:  
  - `api_create_item`, `api_read_item`, `api_update_item`, `api_delete_item`  
  - `api_create_user`, `api_read_user`, `api_delete_user`  
  - `api_authenticate_user`, `api_upload_file`, `api_download_file`  
  - `api_bulk_insert_items`, `api_filter_items`, `api_export_data`  
  - `api_user_interface`  

### [4.6.0] - 2024-11-22
#### Added
- **Numerical Functions**: 
  - `numerical_add`, `numerical_subtract`, `numerical_multiply`, `numerical_divide`, `numerical_zeros`, `numerical_ones`, `numerical_reshape`, `numerical_dot`, `numerical_inv`, `numerical_det`, `numerical_randint`, `numerical_randn`, `numerical_mean`, `numerical_median`, `numerical_variance`, `numerical_std`, `numerical_string_length`, `numerical_string_upper`, `numerical_string_lower`, `numerical_svd`
- **Plotting Functions**: 
  - `plot_histogram`, `plot_line`, `plot_scatter`, `plot_bar`, `plot_pie`, `plot_box`, `plot_heatmap`, `plot_stacked_bar`, `plot_area`, `plot_violin`, `plot_pair`, `plot_3d`, `plot_subplots`, `plot_hexbin`, `plot_contour`

#### Changed
- **General Improvements**: Updated functions to enhance the performance of numerical and plotting functionalities.

---

### [4.5.11] - 2024-11-21
#### Fixed
- **Avoided Dependency Issue**: Resolved Numpy dependency issue.
- **Avoided Automatic Checking**: Closed automatic checking of the engine on startup.

---

### [4.5.7] - 2024-11-20
#### Added
- **Advanced Mathematical Functions**: 
  - `adv_gcd`, `adv_lcm`, `adv_prime_factors`, `adv_is_prime`, `adv_modular_exponentiation`, `adv_is_perfect_square`, `adv_fast_fourier_transform`, `adv_hash_string`, `adv_fast_modular_inverse`, `adv_fibonacci`, `adv_sieve_of_eratosthenes`, `adv_modular_square_root`, `adv_random_prime`, `adv_sum_of_squares`, `adv_calculate_modular_power`, `adv_combinations`, `adv_permutations`.
- **File Operations**: 
  - `get_function_names_from_python_file`, `install_and_setup_nmap`, `check_file_existence`, `create_directory`, `download_file`, `get_file_size`, `get_file_last_modified`, `rename_file`, `delete_file`, `move_file`, `extract_zip`, `compress_files`, `get_url_status`, `fetch_url_content`, `download_files_from_urls`, `get_files_in_directory`, `count_lines_in_file`, `get_current_datetime`, `get_extension`, `get_file_name_without_extension`, `get_file_type`, `move_files_to_directory`.
- **String Operations**: 
  - `str_reverse`, `str_to_upper`, `str_to_lower`, `str_is_palindrome`, `str_count_occurrences`, `str_is_alpha`, `str_is_digit`, `str_find_substring`, `str_replace_substring`, `str_split_words`, `str_strip_spaces`, `str_startswith`, `str_endswith`, `str_isalnum`, `str_isdigit`, `str_title_case`, `str_concat`, `str_join`.
- **List Operations**: 
  - `list_append_item`, `list_remove_item`, `list_insert_item`, `list_pop_item`, `list_find_index`, `list_contains_item`, `list_sort`, `list_reverse`, `list_clear`, `list_copy`, `list_extend`, `list_count`, `list_min`, `list_max`, `list_sum`, `list_mean`, `list_unique`, `list_combine`, `list_difference`, `list_intersection`, `list_is_empty`.
- **Dictionary Operations**: 
  - `dict_add_key_value`, `dict_remove_key`, `dict_get_value`, `dict_update_value`, `dict_contains_key`, `dict_get_all_keys`, `dict_get_all_values`, `dict_clear`, `dict_copy`, `dict_items`, `dict_pop_item`, `dict_update`, `dict_setdefault`, `dict_fromkeys`, `dict_get_key_with_max_value`, `dict_get_key_with_min_value`.
- **Advanced System Utilities**: New utilities for system tasks, including advanced file and system interactions.
- **Advanced MySQL**: 
  - `mysql_execute_advanced_mode` for optimized database query handling.

#### Changed
- **Enhanced Performance**: Optimized mathematical and system utility functions for better performance.
- **File Handling**: Improved file extraction, compression, and download capabilities with error handling and added optimizations.
- **System Utilities**: Enhanced features for managing system processes, checking file types, and system info retrieval.

#### Fixed
- **Bug Fixes**: Fixed several issues related to file handling, string operations, and database interactions.
- **Error Handling**: Improved error handling for file operations, network requests, and system commands.

---

### [4.2.1] - 2024-11-18
#### Added
- **New Nmap Functions**: Added multiple Nmap scanning options for vulnerability assessments.
- **SQLMap Integration**: Expanded SQL injection testing functionalities.
- **Enhanced System Utilities**: New features to execute system commands and retrieve system information.
- **Improved File Handling**: Enhanced operations for various file types.
- **XAMPP Functions**: Added functions for managing XAMPP MySQL and Apache services, and checking PHPMyAdmin accessibility.
- **System Utilities**: Added support for checking Python interpreter path and processor details.

#### Changed
- **General Improvements**: Optimized performance and stability across the module.

#### Fixed
- **Bug Fixes**: Enhanced error handling across file operations and database interactions.

---

### [3.0.2] - 2024-11-14
#### Added
- Improved XAMPP MySQL Functions.
- Improved MySQL database management functions.
- Enhanced CSV, text, and binary file handling.
- Added support for checking Python interpreter path and processor details.
- Introduced functions for managing XAMPP MySQL and Apache services.

#### Fixed
- Enhanced error handling for file operations and MySQL interactions.

#### Changed
- Updated functions to support the latest MySQL and file management enhancements.

---

### [2.7.5] - 2024-11-15
#### Added
- Expanded functionality to support CSV and binary file handling, including reading, writing, and checking file types.
- Additional enhancements in error handling for new file handling features.
- Updated documentation to reflect the latest changes.

---

### [2.7.2] - 2024-11-15
#### Added
- Added pytest and tox for testing.

---

### [2.6.1] - 2024-11-15
#### Added
- Documentation website.

---

### [2.6.0] - 2024-11-14
#### Added
- Expanded mathematical functions for prime numbers, Armstrong numbers, and Niven numbers.
- Enhanced text file handling: added functions to copy contents between files, add lines, and read specific lines.
- System utilities to fetch information such as CPU count, operating system details, Python interpreter path, and network connectivity status.
- New MySQL functions for managing and interacting with databases and tables with improved error handling.
- Time management functions: Added functions to get process time, thread time, and monotonic time.

#### Fixed
- Improved error handling for file operations and MySQL interactions.
- Fixed issues with incorrect data type handling in certain mathematical functions.

---

### [2.5.8] - 2024-11-13
#### Added
- Error correction methods for better handling.
- Support for returning `False` based on data type validity.

---

### [2.5.6] - 2024-11-13
#### Added
- Added Git support.
