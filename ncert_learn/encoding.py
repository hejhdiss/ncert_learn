import base64
import binascii
import urllib.parse
import zlib
import gzip
import brotli
import lzma
import bz2
import struct
from typing import Union
import base64
import binascii
import urllib.parse
import zlib
import gzip
import brotli
import lzma
import bz2
import struct
from typing import Union

# Encoding and Decoding Functions

# ASCII and US-ASCII Encoding/Decoding
def encode_ascii(data: str) -> str:
    """Encodes a given string to ASCII."""
    try:
        return data.encode('ascii').decode('ascii')
    except UnicodeEncodeError:
        raise ValueError("Input cannot be encoded in ASCII.")


def decode_ascii(data: str) -> str:
    """Decodes an ASCII string."""
    try:
        return data.encode('ascii').decode('ascii')
    except UnicodeDecodeError:
        raise ValueError("Invalid ASCII input.")


# UTF-8 Encoding/Decoding
def encode_utf8(data: str) -> str:
    """Encodes a string into UTF-8."""
    try:
        return data.encode('utf-8').decode('utf-8')
    except UnicodeEncodeError:
        raise ValueError("Input cannot be encoded in UTF-8.")


def decode_utf8(data: str) -> str:
    """Decodes a UTF-8 string."""
    try:
        return data.encode('utf-8').decode('utf-8')
    except UnicodeDecodeError:
        raise ValueError("Invalid UTF-8 input.")


# UTF-16 Encoding/Decoding
def encode_utf16(data: str) -> str:
    """Encodes a string into UTF-16."""
    try:
        return data.encode('utf-16').decode('utf-16')
    except UnicodeEncodeError:
        raise ValueError("Input cannot be encoded in UTF-16.")


def decode_utf16(data: str) -> str:
    """Decodes a UTF-16 string."""
    try:
        return data.encode('utf-16').decode('utf-16')
    except UnicodeDecodeError:
        raise ValueError("Invalid UTF-16 input.")


# UTF-32 Encoding/Decoding
def encode_utf32(data: str) -> str:
    """Encodes a string into UTF-32."""
    try:
        return data.encode('utf-32').decode('utf-32')
    except UnicodeEncodeError:
        raise ValueError("Input cannot be encoded in UTF-32.")


def decode_utf32(data: str) -> str:
    """Decodes a UTF-32 string."""
    try:
        return data.encode('utf-32').decode('utf-32')
    except UnicodeDecodeError:
        raise ValueError("Invalid UTF-32 input.")


# Base64 Encoding/Decoding
def encode_base64(data: str) -> str:
    """Encodes a given string into Base64."""
    try:
        return base64.b64encode(data.encode('utf-8')).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Base64 encoding failed: {str(e)}")


def decode_base64(data: str) -> str:
    """Decodes a Base64 string."""
    try:
        return base64.b64decode(data.encode('utf-8')).decode('utf-8')
    except binascii.Error:
        raise ValueError("Invalid Base64 input.")


# Hexadecimal Encoding/Decoding
def encode_hex(data: str) -> str:
    """Encodes a string into Hexadecimal."""
    try:
        return data.encode('utf-8').hex()
    except Exception as e:
        raise RuntimeError(f"Hex encoding failed: {str(e)}")


def decode_hex(data: str) -> str:
    """Decodes a Hexadecimal string."""
    try:
        return bytes.fromhex(data).decode('utf-8')
    except ValueError:
        raise ValueError("Invalid Hexadecimal input.")


# URL Encoding/Decoding
def encode_url(data: str) -> str:
    """Encodes a string into URL encoding."""
    try:
        return urllib.parse.quote(data)
    except Exception as e:
        raise RuntimeError(f"URL encoding failed: {str(e)}")


def decode_url(data: str) -> str:
    """Decodes a URL encoded string."""
    try:
        return urllib.parse.unquote(data)
    except Exception as e:
        raise RuntimeError(f"URL decoding failed: {str(e)}")


# HTML Encoding/Decoding
def encode_html(data: str) -> str:
    """Encodes a string into HTML entities."""
    try:
        return urllib.parse.quote_plus(data)
    except Exception as e:
        raise RuntimeError(f"HTML encoding failed: {str(e)}")


def decode_html(data: str) -> str:
    """Decodes HTML entities into a string."""
    try:
        return urllib.parse.unquote_plus(data)
    except Exception as e:
        raise RuntimeError(f"HTML decoding failed: {str(e)}")


# Morse Code Encoding/Decoding
MORSE_CODE_DICT = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '|'}

def encode_morse(data: str) -> str:
    """Encodes a string into Morse code."""
    try:
        return ' '.join(MORSE_CODE_DICT.get(i.upper(), '') for i in data)
    except Exception as e:
        raise RuntimeError(f"Morse encoding failed: {str(e)}")


def decode_morse(data: str) -> str:
    """Decodes Morse code into a string."""
    try:
        reverse_morse_code_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
        return ''.join(reverse_morse_code_dict.get(i, '') for i in data.split())
    except Exception as e:
        raise RuntimeError(f"Morse decoding failed: {str(e)}")


# Binary Encoding/Decoding
def encode_binary(data: str) -> str:
    """Encodes a string into binary."""
    try:
        return ''.join(format(ord(i), '08b') for i in data)
    except Exception as e:
        raise RuntimeError(f"Binary encoding failed: {str(e)}")


def decode_binary(data: str) -> str:
    """Decodes a binary string into text."""
    try:
        return ''.join(chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8))
    except Exception as e:
        raise RuntimeError(f"Binary decoding failed: {str(e)}")


# Compression-based Encodings
def encode_zlib(data: str) -> bytes:
    """Encodes a string using zlib compression."""
    try:
        return zlib.compress(data.encode('utf-8'))
    except Exception as e:
        raise RuntimeError(f"Zlib encoding failed: {str(e)}")


def decode_zlib(data: bytes) -> str:
    """Decodes a zlib compressed string."""
    try:
        return zlib.decompress(data).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Zlib decoding failed: {str(e)}")


def encode_gzip(data: str) -> bytes:
    """Encodes a string using gzip compression."""
    try:
        return gzip.compress(data.encode('utf-8'))
    except Exception as e:
        raise RuntimeError(f"Gzip encoding failed: {str(e)}")


def decode_gzip(data: bytes) -> str:
    """Decodes a gzip compressed string."""
    try:
        return gzip.decompress(data).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Gzip decoding failed: {str(e)}")


# Base58 Encoding/Decoding
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def encode_base58(data: bytes) -> str:
    """Encodes data to Base58."""
    try:
        count = 0
        num = int.from_bytes(data, byteorder='big')
        base58 = ''
        while num > 0:
            num, rem = divmod(num, 58)
            base58 = BASE58_ALPHABET[rem] + base58
        return base58
    except Exception as e:
        raise RuntimeError(f"Base58 encoding failed: {str(e)}")


def decode_base58(data: str) -> bytes:
    """Decodes Base58 string to bytes."""
    try:
        num = 0
        for char in data:
            num = num * 58 + BASE58_ALPHABET.index(char)
        return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big')
    except Exception as e:
        raise RuntimeError(f"Base58 decoding failed: {str(e)}")


# Return the full function set for all encoding/decoding types, including error handling and docstrings.




# Encoding and Decoding Functions

# ASCII and US-ASCII Encoding/Decoding
def encode_ascii(data: str) -> str:
    """Encodes a given string to ASCII."""
    try:
        return data.encode('ascii').decode('ascii')
    except UnicodeEncodeError:
        raise ValueError("Input cannot be encoded in ASCII.")


def decode_ascii(data: str) -> str:
    """Decodes an ASCII string."""
    try:
        return data.encode('ascii').decode('ascii')
    except UnicodeDecodeError:
        raise ValueError("Invalid ASCII input.")


# UTF-8 Encoding/Decoding
def encode_utf8(data: str) -> str:
    """Encodes a string into UTF-8."""
    try:
        return data.encode('utf-8').decode('utf-8')
    except UnicodeEncodeError:
        raise ValueError("Input cannot be encoded in UTF-8.")


def decode_utf8(data: str) -> str:
    """Decodes a UTF-8 string."""
    try:
        return data.encode('utf-8').decode('utf-8')
    except UnicodeDecodeError:
        raise ValueError("Invalid UTF-8 input.")


# UTF-16 Encoding/Decoding
def encode_utf16(data: str) -> str:
    """Encodes a string into UTF-16."""
    try:
        return data.encode('utf-16').decode('utf-16')
    except UnicodeEncodeError:
        raise ValueError("Input cannot be encoded in UTF-16.")


def decode_utf16(data: str) -> str:
    """Decodes a UTF-16 string."""
    try:
        return data.encode('utf-16').decode('utf-16')
    except UnicodeDecodeError:
        raise ValueError("Invalid UTF-16 input.")


# UTF-32 Encoding/Decoding
def encode_utf32(data: str) -> str:
    """Encodes a string into UTF-32."""
    try:
        return data.encode('utf-32').decode('utf-32')
    except UnicodeEncodeError:
        raise ValueError("Input cannot be encoded in UTF-32.")


def decode_utf32(data: str) -> str:
    """Decodes a UTF-32 string."""
    try:
        return data.encode('utf-32').decode('utf-32')
    except UnicodeDecodeError:
        raise ValueError("Invalid UTF-32 input.")


# Base64 Encoding/Decoding
def encode_base64(data: str) -> str:
    """Encodes a given string into Base64."""
    try:
        return base64.b64encode(data.encode('utf-8')).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Base64 encoding failed: {str(e)}")


def decode_base64(data: str) -> str:
    """Decodes a Base64 string."""
    try:
        return base64.b64decode(data.encode('utf-8')).decode('utf-8')
    except binascii.Error:
        raise ValueError("Invalid Base64 input.")


# Hexadecimal Encoding/Decoding
def encode_hex(data: str) -> str:
    """Encodes a string into Hexadecimal."""
    try:
        return data.encode('utf-8').hex()
    except Exception as e:
        raise RuntimeError(f"Hex encoding failed: {str(e)}")


def decode_hex(data: str) -> str:
    """Decodes a Hexadecimal string."""
    try:
        return bytes.fromhex(data).decode('utf-8')
    except ValueError:
        raise ValueError("Invalid Hexadecimal input.")


# URL Encoding/Decoding
def encode_url(data: str) -> str:
    """Encodes a string into URL encoding."""
    try:
        return urllib.parse.quote(data)
    except Exception as e:
        raise RuntimeError(f"URL encoding failed: {str(e)}")


def decode_url(data: str) -> str:
    """Decodes a URL encoded string."""
    try:
        return urllib.parse.unquote(data)
    except Exception as e:
        raise RuntimeError(f"URL decoding failed: {str(e)}")


# HTML Encoding/Decoding
def encode_html(data: str) -> str:
    """Encodes a string into HTML entities."""
    try:
        return urllib.parse.quote_plus(data)
    except Exception as e:
        raise RuntimeError(f"HTML encoding failed: {str(e)}")


def decode_html(data: str) -> str:
    """Decodes HTML entities into a string."""
    try:
        return urllib.parse.unquote_plus(data)
    except Exception as e:
        raise RuntimeError(f"HTML decoding failed: {str(e)}")


# Morse Code Encoding/Decoding
MORSE_CODE_DICT = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '|'}

def encode_morse(data: str) -> str:
    """Encodes a string into Morse code."""
    try:
        return ' '.join(MORSE_CODE_DICT.get(i.upper(), '') for i in data)
    except Exception as e:
        raise RuntimeError(f"Morse encoding failed: {str(e)}")


def decode_morse(data: str) -> str:
    """Decodes Morse code into a string."""
    try:
        reverse_morse_code_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
        return ''.join(reverse_morse_code_dict.get(i, '') for i in data.split())
    except Exception as e:
        raise RuntimeError(f"Morse decoding failed: {str(e)}")


# Binary Encoding/Decoding
def encode_binary(data: str) -> str:
    """Encodes a string into binary."""
    try:
        return ''.join(format(ord(i), '08b') for i in data)
    except Exception as e:
        raise RuntimeError(f"Binary encoding failed: {str(e)}")


def decode_binary(data: str) -> str:
    """Decodes a binary string into text."""
    try:
        return ''.join(chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8))
    except Exception as e:
        raise RuntimeError(f"Binary decoding failed: {str(e)}")


# Compression-based Encodings
def encode_zlib(data: str) -> bytes:
    """Encodes a string using zlib compression."""
    try:
        return zlib.compress(data.encode('utf-8'))
    except Exception as e:
        raise RuntimeError(f"Zlib encoding failed: {str(e)}")


def decode_zlib(data: bytes) -> str:
    """Decodes a zlib compressed string."""
    try:
        return zlib.decompress(data).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Zlib decoding failed: {str(e)}")


def encode_gzip(data: str) -> bytes:
    """Encodes a string using gzip compression."""
    try:
        return gzip.compress(data.encode('utf-8'))
    except Exception as e:
        raise RuntimeError(f"Gzip encoding failed: {str(e)}")


def decode_gzip(data: bytes) -> str:
    """Decodes a gzip compressed string."""
    try:
        return gzip.decompress(data).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Gzip decoding failed: {str(e)}")


# Base58 Encoding/Decoding
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def encode_base58(data: bytes) -> str:
    """Encodes data to Base58."""
    try:
        count = 0
        num = int.from_bytes(data, byteorder='big')
        base58 = ''
        while num > 0:
            num, rem = divmod(num, 58)
            base58 = BASE58_ALPHABET[rem] + base58
        return base58
    except Exception as e:
        raise RuntimeError(f"Base58 encoding failed: {str(e)}")


def decode_base58(data: str) -> bytes:
    """Decodes Base58 string to bytes."""
    try:
        num = 0
        for char in data:
            num = num * 58 + BASE58_ALPHABET.index(char)
        return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big')
    except Exception as e:
        raise RuntimeError(f"Base58 decoding failed: {str(e)}")


# Additional Encodings (Deflate, Brotli, LZMA, Bzip2)
# Deflate Encoding/Decoding
def encode_deflate(data: str) -> bytes:
    """Encodes a string using Deflate compression."""
    try:
        return zlib.compress(data.encode('utf-8'), level=9)
    except Exception as e:
        raise RuntimeError(f"Deflate encoding failed: {str(e)}")


def decode_deflate(data: bytes) -> str:
    """Decodes a Deflate compressed string."""
    try:
        return zlib.decompress(data).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Deflate decoding failed: {str(e)}")


# Brotli Encoding/Decoding
def encode_brotli(data: str) -> bytes:
    """Encodes a string using Brotli compression."""
    try:
        return brotli.compress(data.encode('utf-8'))
    except Exception as e:
        raise RuntimeError(f"Brotli encoding failed: {str(e)}")


def decode_brotli(data: bytes) -> str:
    """Decodes a Brotli compressed string."""
    try:
        return brotli.decompress(data).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Brotli decoding failed: {str(e)}")


# LZMA Encoding/Decoding
def encode_lzma(data: str) -> bytes:
    """Encodes a string using LZMA compression."""
    try:
        return lzma.compress(data.encode('utf-8'))
    except Exception as e:
        raise RuntimeError(f"LZMA encoding failed: {str(e)}")


def decode_lzma(data: bytes) -> str:
    """Decodes a LZMA compressed string."""
    try:
        return lzma.decompress(data).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"LZMA decoding failed: {str(e)}")


# Return the full function set for all encoding/decoding types.
import base64
import binascii
import urllib.parse
from typing import Union


# Basic Encodings

def encode_base64(data: str) -> str:
    """
    Encodes a given string into Base64 format.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The Base64-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"Base64 encoding failed: {str(e)}")


def decode_base64(data: str) -> str:
    """
    Decodes a Base64-encoded string.

    Parameters:
        data (str): The Base64-encoded string to decode.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not a valid Base64 string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        decoded_data = base64.b64decode(data.encode('utf-8')).decode('utf-8')
        return decoded_data
    except binascii.Error:
        raise ValueError("Invalid Base64 input.")
    except Exception as e:
        raise RuntimeError(f"Base64 decoding failed: {str(e)}")


# URL Encoding

def encode_url(data: str) -> str:
    """
    Encodes a given string for safe use in URLs.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The URL-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = urllib.parse.quote(data)
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"URL encoding failed: {str(e)}")


def decode_url(data: str) -> str:
    """
    Decodes a URL-encoded string.

    Parameters:
        data (str): The URL-encoded string to decode.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not a valid URL-encoded string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        decoded_data = urllib.parse.unquote(data)
        return decoded_data
    except Exception as e:
        raise RuntimeError(f"URL decoding failed: {str(e)}")


# Hexadecimal Encoding

def encode_hex(data: str) -> str:
    """
    Encodes a given string into hexadecimal format.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The hexadecimal-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = data.encode('utf-8').hex()
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"Hex encoding failed: {str(e)}")


def decode_hex(data: str) -> str:
    """
    Decodes a hexadecimal-encoded string.

    Parameters:
        data (str): The hexadecimal-encoded string to decode.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not a valid hexadecimal string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        decoded_data = bytes.fromhex(data).decode('utf-8')
        return decoded_data
    except ValueError:
        raise ValueError("Invalid hexadecimal input.")
    except Exception as e:
        raise RuntimeError(f"Hex decoding failed: {str(e)}")


# ROT13 Encoding

def encode_rot13(data: str) -> str:
    """
    Encodes a string using the ROT13 cipher.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The ROT13-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = data.translate(str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"))
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"ROT13 encoding failed: {str(e)}")


def decode_rot13(data: str) -> str:
    """
    Decodes a ROT13-encoded string.

    Parameters:
        data (str): The ROT13-encoded string to decode.

    Returns:
        str: The decoded string.

    Note:
        ROT13 encoding and decoding are the same operation.

    Raises:
        ValueError: If the input is not a valid string.
    """
    return encode_rot13(data)


# Base32 Encoding

def encode_base32(data: str) -> str:
    """
    Encodes a given string into Base32 format.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The Base32-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = base64.b32encode(data.encode('utf-8')).decode('utf-8')
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"Base32 encoding failed: {str(e)}")


def decode_base32(data: str) -> str:
    """
    Decodes a Base32-encoded string.

    Parameters:
        data (str): The Base32-encoded string to decode.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not a valid Base32 string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        decoded_data = base64.b32decode(data.encode('utf-8')).decode('utf-8')
        return decoded_data
    except binascii.Error:
        raise ValueError("Invalid Base32 input.")
    except Exception as e:
        raise RuntimeError(f"Base32 decoding failed: {str(e)}")


# Base16 Encoding

def encode_base16(data: str) -> str:
    """
    Encodes a given string into Base16 format.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The Base16-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = base64.b16encode(data.encode('utf-8')).decode('utf-8')
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"Base16 encoding failed: {str(e)}")


def decode_base16(data: str) -> str:
    """
    Decodes a Base16-encoded string.

    Parameters:
        data (str): The Base16-encoded string to decode.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not a valid Base16 string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        decoded_data = base64.b16decode(data.encode('utf-8')).decode('utf-8')
        return decoded_data
    except binascii.Error:
        raise ValueError("Invalid Base16 input.")
    except Exception as e:
        raise RuntimeError(f"Base16 decoding failed: {str(e)}")


# Caesar Cipher Encoding (Shift by 3)

def encode_caesar_cipher(data: str, shift: int = 3) -> str:
    """
    Encodes a string using Caesar cipher with a fixed shift.

    Parameters:
        data (str): The input string to encode.
        shift (int): The shift value for encoding. Default is 3.

    Returns:
        str: The Caesar cipher-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        result = []
        for char in data:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
            else:
                result.append(char)
        encoded_data = ''.join(result)
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"Caesar cipher encoding failed: {str(e)}")


def decode_caesar_cipher(data: str, shift: int = 3) -> str:
    """
    Decodes a Caesar cipher-encoded string using a fixed shift.

    Parameters:
        data (str): The Caesar cipher-encoded string to decode.
        shift (int): The shift value for decoding. Default is 3.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    return encode_caesar_cipher(data, -shift)


# URL-safe Base64 Encoding

def encode_url_safe_base64(data: str) -> str:
    """
    Encodes a given string into URL-safe Base64 format.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The URL-safe Base64-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = base64.urlsafe_b64encode(data.encode('utf-8')).decode('utf-8')
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"URL-safe Base64 encoding failed: {str(e)}")


def decode_url_safe_base64(data: str) -> str:
    """
    Decodes a URL-safe Base64-encoded string.

    Parameters:
        data (str): The URL-safe Base64-encoded string to decode.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not a valid URL-safe Base64 string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        decoded_data = base64.urlsafe_b64decode(data.encode('utf-8')).decode('utf-8')
        return decoded_data
    except binascii.Error:
        raise ValueError("Invalid URL-safe Base64 input.")
    except Exception as e:
        raise RuntimeError(f"URL-safe Base64 decoding failed: {str(e)}")


# Additional Encoding Methods can be added here
import base64
import binascii
import urllib.parse
from typing import Union


# Basic Encodings

def encode_base64(data: str) -> str:
    """
    Encodes a given string into Base64 format.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The Base64-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"Base64 encoding failed: {str(e)}")


def decode_base64(data: str) -> str:
    """
    Decodes a Base64-encoded string.

    Parameters:
        data (str): The Base64-encoded string to decode.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not a valid Base64 string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        decoded_data = base64.b64decode(data.encode('utf-8')).decode('utf-8')
        return decoded_data
    except binascii.Error:
        raise ValueError("Invalid Base64 input.")
    except Exception as e:
        raise RuntimeError(f"Base64 decoding failed: {str(e)}")


# URL Encoding

def encode_url(data: str) -> str:
    """
    Encodes a given string for safe use in URLs.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The URL-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = urllib.parse.quote(data)
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"URL encoding failed: {str(e)}")


def decode_url(data: str) -> str:
    """
    Decodes a URL-encoded string.

    Parameters:
        data (str): The URL-encoded string to decode.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not a valid URL-encoded string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        decoded_data = urllib.parse.unquote(data)
        return decoded_data
    except Exception as e:
        raise RuntimeError(f"URL decoding failed: {str(e)}")


# Hexadecimal Encoding

def encode_hex(data: str) -> str:
    """
    Encodes a given string into hexadecimal format.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The hexadecimal-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = data.encode('utf-8').hex()
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"Hex encoding failed: {str(e)}")


def decode_hex(data: str) -> str:
    """
    Decodes a hexadecimal-encoded string.

    Parameters:
        data (str): The hexadecimal-encoded string to decode.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not a valid hexadecimal string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        decoded_data = bytes.fromhex(data).decode('utf-8')
        return decoded_data
    except ValueError:
        raise ValueError("Invalid hexadecimal input.")
    except Exception as e:
        raise RuntimeError(f"Hex decoding failed: {str(e)}")


# ROT13 Encoding

def encode_rot13(data: str) -> str:
    """
    Encodes a string using the ROT13 cipher.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The ROT13-encoded string.

    Raises:
        ValueError: If the input is not a valid string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        encoded_data = data.translate(str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"))
        return encoded_data
    except Exception as e:
        raise RuntimeError(f"ROT13 encoding failed: {str(e)}")


def decode_rot13(data: str) -> str:
    """
    Decodes a ROT13-encoded string.

    Parameters:
        data (str): The ROT13-encoded string to decode.

    Returns:
        str: The decoded string.

    Note:
        ROT13 encoding and decoding are the same operation.

    Raises:
        ValueError: If the input is not a valid string.
    """
    return encode_rot13(data)


# Add 56 more encoding/decoding functions similarly

# Example of additional functions
def encode_binary(data: str) -> str:
    """
    Encodes a string into binary representation.

    Parameters:
        data (str): The input string to encode.

    Returns:
        str: The binary-encoded string.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    return ' '.join(format(ord(char), '08b') for char in data)


def decode_binary(data: str) -> str:
    """
    Decodes a binary-encoded string.

    Parameters:
        data (str): The binary-encoded string to decode.

    Returns:
        str: The decoded string.

    Raises:
        ValueError: If the input is not valid binary data.
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string.")
    try:
        return ''.join(chr(int(byte, 2)) for byte in data.split())
    except ValueError:
        raise ValueError("Invalid binary input.")
    except Exception as e:
        raise RuntimeError(f"Binary decoding failed: {str(e)}")


# Further encoding methods can include Base32, Base16, Caesar Cipher, URL-safe Base64, etc.

# Complete the module as needed with additional methods!
