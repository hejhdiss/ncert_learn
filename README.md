# ncert_learn

**ncert_learn** is a comprehensive Python module designed to support NCERT Class 12 Computer Science students. It offers a wide range of utility functions across various topics, including Python programming, MySQL database interactions, mathematical operations, data structures, system utilities, and more.

## Key Features

### **Mathematical Functions**
- Prime number check
- Armstrong, Strong, Niven, and Palindrome checks
- Fibonacci numbers, even/odd checks, and more
- Advanced functions like GCD, LCM, prime factorization, modular exponentiation, and fast Fourier transform
- **New Advanced Mathematical Functions**:
  - `adv_gcd`, `adv_lcm`, `adv_prime_factors`, `adv_is_prime`

### **Data Structures**
- Stack operations using lists and dictionaries:
  - Push, pop, peek, and display

### **Geometric Calculations**
- Area calculations for:
  - Circles, rectangles, squares, polygons, and triangles

### **Number Conversions**
- Convert integers to binary, octal, hexadecimal, and vice versa

### **MySQL Operations**
- Connect to MySQL, manage databases and tables, execute queries
- **Advanced MySQL Features**:
  - Optimized database management with `mysql_execute_advanced_mode`

### **Sorting Algorithms**
- Implementations of Bubble Sort and Insertion Sort

### **File Handling**
- Read, write, and manage text, CSV, and binary files
- File operations like:
  - Copying, reading specific lines, clearing contents
  - Creating directories, renaming, moving, and extracting ZIP files

### **System Utilities**
- Fetch information about the operating system, processor, network connectivity, and Python interpreter

### **Package Management**
- Install and manage Python libraries, including bulk installations from a list

### **Time Management**
- Access current time, process time, monotonic time, and thread time

### **XAMPP Utilities**
- Start/stop XAMPP MySQL and Apache services
- Check PHPMyAdmin access

### **Zip File Handling**
- Handle ZIP files:
  - List contents, extract files, and add files

### **Nmap Scans**
- Perform network scans such as:
  - Intense scan, quick scan, OS detection, and more

### **SQLMap Scans**
- Perform SQL injection tests using SQLMap

### **Text, Binary, and CSV File Operations**
- Overwrite and manipulate text, binary, and CSV files with advanced handling

### **Advanced Mathematical and Cryptographic Functions**
- Functions for:
  - GCD, LCM, prime factors, modular exponentiation, Fibonacci, and more
- Advanced hashing, modular inverse, and fast Fourier transforms

### **List Operations**
- Advanced list handling functions:
  - Sorting, reversing, finding, combining, and counting items

### **String Operations**
- String manipulation:
  - Case conversion, concatenation, joining, and counting occurrences

### **Dictionary Operations**
- Manage key-value pairs in dictionaries:
  - Add, remove, update, and fetch values

### **Numerical Functions**
- Mathematical operations:
  - `numerical_add`, `numerical_subtract`, `numerical_multiply`, `numerical_divide`
- Advanced numerical computations:
  - `numerical_zeros`, `numerical_ones`, `numerical_reshape`, `numerical_dot`
- Matrix operations:
  - `numerical_inv`, `numerical_det`, `numerical_svd`
- Statistical computations:
  - `numerical_mean`, `numerical_median`, `numerical_variance`, `numerical_std`
- String-related operations:
  - `numerical_string_length`, `numerical_string_upper`, `numerical_string_lower`
- Random number generation:
  - `numerical_randint`, `numerical_randn`

### **Plotting Functions**
- Create various visualizations such as:
  - `plot_histogram`, `plot_line`, `plot_scatter`, `plot_bar`, `plot_pie`
  - `plot_box`, `plot_heatmap`, `plot_stacked_bar`, `plot_area`
  - Advanced plots:
    - `plot_violin`, `plot_pair`, `plot_3d`, `plot_hexbin`, `plot_contour`

### **API Functions**
- Comprehensive API-like functionalities:
  - `api_create_item`, `api_read_item`, `api_update_item`, `api_delete_item`
  - `api_create_user`, `api_read_user`, `api_delete_user`, `api_authenticate_user`
  - `api_upload_file`, `api_download_file`, `api_bulk_insert_items`
  - `api_filter_items`, `api_export_data`, `api_user_interface`

### **Cryptographic Functions**:
- **Encoding/Decoding Methods**:
  - `encode_ascii`, `decode_ascii`, `encode_utf8`, `decode_utf8`, `encode_utf16`, `decode_utf16`, `encode_utf32`, `decode_utf32`
  - `encode_base64`, `decode_base64`, `encode_hex`, `decode_hex`, `encode_url`, `decode_url`, `encode_html`, `decode_html`
  - `encode_morse`, `decode_morse`, `encode_binary`, `decode_binary`
  - `encode_zlib`, `decode_zlib`, `encode_gzip`, `decode_gzip`, `encode_base58`, `decode_base58`
  - `encode_deflate`, `decode_deflate`, `encode_brotli`, `decode_brotli`, `encode_lzma`, `decode_lzma`
  - `encode_rot13`, `decode_rot13`, `encode_base32`, `decode_base32`, `encode_base16`, `decode_base16`
  - `encode_caesar_cipher`, `decode_caesar_cipher`, `encode_url_safe_base64`, `decode_url_safe_base64`

### **Functionality for Extracting Functions from Python Files**:
  - `get_function_names_from_python_file_list`: Extracts function names from a Python file and returns them as a list.
  - `get_function_names_from_python_file_str`: Extracts function names from a string of Python code and returns them as a list.
  
---

## Changelog  

All notable changes to this project are documented in the [Changelog](CHANGELOG.md).  

## Recommendation: Upgrade to Version 4.8.0

We recommend downloading **version 4.8.0**, as it includes important bug fixes and new features that enhance performance, usability, and stability. Upgrade today for an improved experience.

## Disclaimer
This module is intended for educational purposes only. Using this module for any illegal activities is strictly prohibited. The authors and contributors are not responsible for any misuse of the module.

## Installation

To install **ncert_learn**, use `pip`:

```bash
pip install ncert_learn
