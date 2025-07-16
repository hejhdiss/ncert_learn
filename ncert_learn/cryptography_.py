from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes as hazmat_hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
import os
import base64
import hashlib
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def aes_encrypt(plaintext, key):
    """
    Encrypts the given plaintext using AES encryption.

    Args:
        plaintext (str): The plaintext to encrypt.
        key (bytes): A 32-byte key for AES encryption (for AES-256).

    Returns:
        dict: A dictionary containing the ciphertext, initialization vector (IV), and encrypted key.
    """
    if not isinstance(key, bytes) or len(key) not in {16, 24, 32}:
        raise ValueError("Key must be bytes and 16, 24, or 32 bytes long (for AES-128, AES-192, or AES-256).")
    
    # Generate a random 16-byte IV
    iv = os.urandom(16)
    
    # Initialize AES Cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Pad the plaintext to a multiple of 16 bytes
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()
    
    # Encrypt the padded plaintext
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    return {
        "ciphertext": ciphertext,
        "iv": iv,
        "key": key
    }

# Example Usage

# 1. Key Generation with Fernet
def generate_key():

    """
    Generates a key for use with the Fernet symmetric encryption algorithm.

    Returns:
        bytes: A 32 byte key suitable for use with Fernet.
    """

    return Fernet.generate_key()

# 2. Encrypt Message with Fernet
def encrypt_message(key, message):

    """
    Encrypts a message using the Fernet symmetric encryption algorithm.

    Args:
        key (bytes): A 32 byte key suitable for use with Fernet.
        message (str): The message to be encrypted.

    Returns:
        bytes: The encrypted message.
    """
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(message.encode())

# 3. Decrypt Message with Fernet
def decrypt_message(key, encrypted_message):
    

    """
    Decrypts a message using the Fernet symmetric encryption algorithm.

    Args:
        key (bytes): A 32 byte key suitable for use with Fernet.
        encrypted_message (bytes): The message to be decrypted.

    Returns:
        str: The decrypted message.
    """
    

    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_message).decode()

# 4. Base64 Encoding/Decoding
def base64_encode(data):

    """
    Encodes data using the Base64 encoding algorithm.

    Args:
        data (bytes): The data to be encoded.

    Returns:
        str: The Base64 encoded data.
    """

    return base64.b64encode(data).decode('utf-8')

def base64_decode(encoded_data):
    """
        Decodes data from Base64 encoding.

        Args:
            encoded_data (str): The Base64 encoded data to be decoded.

        Returns:
            bytes: The decoded data.
    """
    return base64.b64decode(encoded_data.encode('utf-8'))

# 5. Save/Load Key
def save_key_to_file(key, filename):
    """
    Saves a key to a file.

    Args:
        key (bytes): The key to be saved.
        filename (str): The name of the file to be saved to.
    """

    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key_from_file(filename):
    """
    Loads a key from a file.

    Args:
        filename (str): The name of the file to load the key from.

    Returns:
        bytes: The key read from the file.
    """

    with open(filename, "rb") as key_file:
        return key_file.read()

# 6. SHA-256 Hashing
def hash_message(message):

    """
    Hashes a message using the SHA-256 algorithm.

    Args:
        message (str): The message to be hashed.

    Returns:
        bytes: The hash of the message.
    """

    digest = hashes.Hash(hazmat_hashes.SHA256())
    digest.update(message.encode())
    return digest.finalize()

# 7. RSA Sign and Verify
def generate_rsa_keypair():
    """
    Generates a pair of RSA keys.

    Returns:
        tuple: A tuple containing the private and public keys.
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    """
    Signs a message using the RSA private key.

    Args:
        private_key (RSAPrivateKey): The private key to use for signing.
        message (str): The message to sign.

    Returns:
        bytes: The signature of the message.
    """

    return private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

def verify_signature(public_key, message, signature):

    """
    Verifies the signature of a message using the RSA public key.

    Args:
        public_key (RSAPublicKey): The public key to use for verification.
        message (str): The message to verify.
        signature (bytes): The signature of the message.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    

    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except:
        return False

# 8. AES CBC Mode Encryption
def aes_encrypt_cbc(key, plaintext):

    """
    Encrypts a message using AES CBC mode.

    Args:
        key (bytes): A 32 byte key suitable for use with AES.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message, with the IV prepended.
    """

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return iv + ciphertext

def aes_decrypt_cbc(key, encrypted_data):

    """
    Decrypts a message using AES CBC mode.

    Args:
        key (bytes): A 32 byte key suitable for use with AES.
        encrypted_data (bytes): The encrypted message, with the IV prepended.

    Returns:
        str: The decrypted message.
    """

    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_data.decode()

# 9. RSA Public Key Encryption
def rsa_encrypt(public_key, plaintext):

    """
    Encrypts a message using RSA public key encryption with OAEP.

    Args:
        public_key (RSAPublicKey): The public key to use for encryption.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message.
    """

    ciphertext = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# 10. RSA Private Key Decryption
def rsa_decrypt(private_key, ciphertext):

    """
    Decrypts a message using RSA private key decryption with OAEP.

    Args:
        private_key (RSAPrivateKey): The private key to use for decryption.
        ciphertext (bytes): The message to decrypt.

    Returns:
        str: The decrypted message.
    """

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

# 11. PBKDF2 Key Derivation
def pbkdf2_key_derivation(password, salt, iterations=100000):

    """
    Derives a key from a password using the PBKDF2 key derivation function.

    Args:
        password (str): The password to use for key derivation.
        salt (bytes): The salt to use for key derivation.
        iterations (int): The number of iterations to use for key derivation.

    Returns:
        bytes: The derived key.
    """


    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

# 12. ECC Key Generation and Signing
def generate_ecc_keypair():

    """
    Generates a key pair for use with Elliptic Curve Cryptography (ECC) signing.

    Returns:
        tuple: A tuple containing the private and public keys.
    """

    private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_with_ecc(private_key, message):
    """
    Signs a message using the ECC private key.

    Args:
        private_key (ec.EllipticCurvePrivateKey): The private key to use for signing.
        message (str): The message to sign.

    Returns:
        bytes: The signature of the message.
    """
    
    signature = private_key.sign(
        message.encode(),
        ec.ECDSA(hashes.SHA256())
    )
    return signature

# 13. HMAC (Hash-based Message Authentication Code)
def hmac_sha256(key, message):

    """
    Generates an HMAC using SHA-256 for a given key and message.

    Args:
        key (str): The key to use for HMAC generation.
        message (str): The message to authenticate.

    Returns:
        bytes: The generated HMAC as bytes.
    """

    hmac_obj = HMAC(key.encode(), hashes.SHA256(), backend=default_backend())
    hmac_obj.update(message.encode())
    return hmac_obj.finalize()

# 14. SHA-512 Hashing
def sha512_hash(message):

    """
    Generates a SHA-512 hash of a given message.

    Args:
        message (str): The message to hash.

    Returns:
        bytes: The generated hash as bytes.
    """
    digest = hashes.Hash(hazmat_hashes.SHA512())
    digest.update(message.encode())
    return digest.finalize()

# 15. MD5 Hashing
def md5_hash(message):
    """
    Generates an MD5 hash of a given message.

    Args:
        message (str): The message to hash.

    Returns:
        str: The generated hash as a hexadecimal string.
    """
    

    return hashlib.md5(message.encode()).hexdigest()

# 16. AES GCM Encryption
def aes_encrypt_gcm(key, plaintext):
    """
    Encrypts a message using AES GCM mode.

    Args:
        key (bytes): A 32 byte key suitable for use with AES.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message, with the nonce and authentication tag
            prepended.
    """

    nonce = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return nonce + encryptor.tag + ciphertext

def aes_decrypt_gcm(key, encrypted_data):

    """
    Decrypts a message using AES GCM mode.

    Args:
        key (bytes): A 32 byte key suitable for use with AES.
        encrypted_data (bytes): The encrypted message, with the nonce and authentication tag
            prepended.

    Returns:
        str: The decrypted message.
    """

    nonce, tag, ciphertext = encrypted_data[:12], encrypted_data[12:28], encrypted_data[28:]
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_data.decode()

# 17. RSA Key Serialization (PEM/DER)
def serialize_rsa_key(key, format_type='PEM'):

    """
    Serializes an RSA key to a PEM or DER encoded string.

    Args:
        key (cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKey): The RSA key to serialize.
        format_type (str): The format to serialize the key in. Defaults to 'PEM'.

    Returns:
        bytes: The serialized RSA key.

    Raises:
        ValueError: If the format_type is not 'PEM' or 'DER'.
    """

    if format_type == 'PEM':
        return key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    elif format_type == 'DER':
        return key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

def deserialize_rsa_key(serialized_key, format_type='PEM'):
    """
    Deserializes an RSA key from a PEM or DER encoded string.

    Args:
        serialized_key (bytes): The serialized RSA key.
        format_type (str): The format to deserialize the key from. Defaults to 'PEM'.

    Returns:
        cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKey: The deserialized RSA key.

    Raises:
        ValueError: If the format_type is not 'PEM' or 'DER'.
    """

    if format_type == 'PEM':
        return serialization.load_pem_private_key(serialized_key, password=None, backend=default_backend())
    elif format_type == 'DER':
        return serialization.load_der_private_key(serialized_key, password=None, backend=default_backend())

# 18. X.509 Certificate Parsing
def parse_x509_certificate(cert_pem):

    """
    Parses an X.509 certificate from a PEM encoded string.

    Args:
        cert_pem (str): The PEM encoded certificate string.

    Returns:
        dict: A dictionary containing information about the certificate. The dictionary contains the following keys:

            * `subject`: The subject of the certificate as a `cryptography.x509.Name` object.
            * `issuer`: The issuer of the certificate as a `cryptography.x509.Name` object.
            * `serial_number`: The serial number of the certificate as an integer.
            * `not_valid_before`: The date and time before which the certificate is not valid as a `datetime.datetime` object.
            * `not_valid_after`: The date and time after which the certificate is not valid as a `datetime.datetime` object.
    """

    cert = load_pem_x509_certificate(cert_pem.encode(), default_backend())
    return {
        'subject': cert.subject,
        'issuer': cert.issuer,
        'serial_number': cert.serial_number,
        'not_valid_before': cert.not_valid_before,
        'not_valid_after': cert.not_valid_after
    }

# 19. Password-Based Encryption (PBE)
def password_based_encryption(password, salt, plaintext):

    """
    Encrypts a message using password-based encryption.

    Derives a key using PBKDF2 key derivation and then encrypts the message
    using AES encryption with the derived key.

    Args:
        password (str): The password to use for deriving the key.
        salt (bytes): The salt to use for deriving the key.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message.
    """

    key = pbkdf2_key_derivation(password, salt)
    return aes_encrypt(key, plaintext)

def password_based_decryption(password, salt, encrypted_data):

    """
    Decrypts a message using password-based encryption.

    Derives a key using PBKDF2 key derivation and then decrypts the message
    using AES encryption with the derived key.

    Args:
        password (str): The password to use for deriving the key.
        salt (bytes): The salt to use for deriving the key.
        encrypted_data (bytes): The message to decrypt.

    Returns:
        bytes: The decrypted message.
    """

    key = pbkdf2_key_derivation(password, salt)
    return decrypt_message(key, encrypted_data)

# Full code ends here
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes as hazmat_hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
import os
import base64
import hashlib
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import bcrypt

# AES CTR Mode Encryption
def aes_encrypt_ctr(key, plaintext):

    """
    Encrypts a message using AES CTR mode encryption.

    Args:
        key (bytes): A 32 byte key suitable for use with AES.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message, with the IV prepended.
    """

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return iv + ciphertext

# Generate RSA Keypair and Save to File
def generate_and_save_rsa_keypair(bits=2048, file_prefix='rsa_key'):

    """
    Generates a pair of RSA keys and saves them to file.

    Args:
        bits (int): The size of the key in bits. Defaults to 2048.
        file_prefix (str): The prefix to use for the filenames. Defaults to 'rsa_key'.
    
    Returns:
        tuple: A tuple containing the private and public keys.
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=bits,
        backend=default_backend()
    )
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(f"{file_prefix}_private.pem", "wb") as private_file:
        private_file.write(private_pem)

    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(f"{file_prefix}_public.pem", "wb") as public_file:
        public_file.write(public_pem)
    
    return private_key, public_key

# AES Key Generation (256-bit)
def generate_aes_key():

    """
    Generates a 256-bit AES key.

    Returns:
        bytes: The 256-bit AES key.
    """

    return os.urandom(32)  # 256-bit AES key

# Blowfish Encryption
def blowfish_encrypt(key, plaintext):
    """
    Encrypts a message using the Blowfish cipher in ECB mode.

    Args:
        key (bytes): The key to use for encryption.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message.
    """

    cipher = Cipher(algorithms.Blowfish(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext.encode()) + encryptor.finalize()

# Des3 (Triple DES) Encryption
def des3_encrypt(key, plaintext):

    """
    Encrypts a message using the Triple DES cipher in ECB mode.

    Args:
        key (bytes): The key to use for encryption. Must be 24 bytes long.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message.
    """

    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext.encode()) + encryptor.finalize()

# Elliptic Curve Key Generation (P-256)
def generate_ecc_keypair():

    """
    Generates a key pair for use with Elliptic Curve Cryptography (ECC) signing.

    Returns:
        tuple: A tuple containing the private and public keys.
    """

    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

# RSA Encryption with OAEP (Padding)
def rsa_encrypt_oaep(public_key, plaintext):

    """
    Encrypts a message using the RSA cipher with OAEP padding.

    Args:
        public_key (RSAPublicKey): The public key to use for encryption.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message.
    """

    return public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# ECDSA Signature Verification
def verify_ecdsa_signature(public_key, signature, message):

    """
    Verifies the signature of a message using the ECDSA signature algorithm.

    Args:
        public_key (EllipticCurvePublicKey): The public key to use for verification.
        signature (bytes): The signature of the message.
        message (str): The message to verify.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """

    try:
        public_key.verify(
            signature,
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except:
        return False

# Create HMAC SHA-1
def hmac_sha1(key, message):

    """
    Generates an HMAC using SHA-1 for a given key and message.

    Args:
        key (str): The key to use for HMAC generation.
        message (str): The message to authenticate.

    Returns:
        bytes: The generated HMAC as bytes.
    """

    hmac_obj = HMAC(key.encode(), hashes.SHA1(), backend=default_backend())
    hmac_obj.update(message.encode())
    return hmac_obj.finalize()

# Password Hashing with bcrypt
def bcrypt_hash(password):

    """
    Generates a bcrypt hash from a given password.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The generated bcrypt hash as bytes.
    """

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# AES ECB Mode Encryption
def aes_encrypt_ecb(key, plaintext):

    """
    Encrypts a message using AES ECB mode encryption.

    Args:
        key (bytes): A 32 byte key suitable for use with AES.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message.
    """

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext.encode()) + encryptor.finalize()

# Generate AES Key with PBKDF2
def pbkdf2_aes_key(password, salt):

    """
    Derives a key from a password using the PBKDF2 key derivation function.

    Args:
        password (str): The password to use for key derivation.
        salt (bytes): The salt to use for key derivation.

    Returns:
        bytes: The derived key, suitable for use with AES.
    """

    kdf = PBKDF2HMAC(
        hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Base64 Encoding/Decoding with URL Safe
def base64_urlsafe_encode_(data):

    """
    Encodes data using the URL-safe Base64 encoding algorithm.

    Args:
        data (bytes): The data to be encoded.

    Returns:
        str: The URL-safe Base64 encoded data.
    """

    return base64.urlsafe_b64encode(data).decode()

def base64_urlsafe_decode_(encoded_data):

    """
    Decodes a URL-safe Base64-encoded string into bytes.

    Args:
        encoded_data (str): The URL-safe Base64 encoded data to be decoded.

    Returns:
        bytes: The decoded data as bytes.

    Raises:
        binascii.Error: If the input is not a valid URL-safe Base64 string.
    """

    return base64.urlsafe_b64decode(encoded_data.encode())

# Key Derivation Function (Scrypt)
def scrypt_key_derivation(password, salt):

    """
    Derives a key from a password using the Scrypt key derivation function.

    Args:
        password (str): The password to use for key derivation.
        salt (bytes): The salt to use for key derivation.

    Returns:
        bytes: The derived key, suitable for use with AES.
    """

    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Curve25519 Key Generation
def curve25519_key_generation():

    """
    Generates a Curve25519 key pair.

    Returns:
        bytes: The 32 byte private key.
    """

    private_key = os.urandom(32)
    return private_key

# RSA Public Key Encryption with OAEP
def rsa_encrypt_oaep(public_key, plaintext):

    """
    Encrypts a message using RSA public key encryption with OAEP.

    Args:
        public_key (RSAPublicKey): The public key to use for encryption.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message.
    """

    return public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# RSA Private Key Decryption with OAEP
def rsa_decrypt_oaep(private_key, ciphertext):

    """
    Decrypts a message using RSA private key decryption with OAEP.

    Args:
        private_key (RSAPrivateKey): The private key to use for decryption.
        ciphertext (bytes): The message to decrypt.

    Returns:
        str: The decrypted message.
    """


    return private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# Digital Signature using RSA
def sign_rsa(private_key, message):

    """
    Signs a message using the RSA private key.

    Args:
        private_key (RSAPrivateKey): The private key to use for signing.
        message (str): The message to sign.

    Returns:
        bytes: The signature of the message.
    """


    return private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

# Create SHA-1 Hash
def sha1_hash(message):

    """
    Generates a SHA-1 hash of a given message.

    Args:
        message (str): The message to hash.

    Returns:
        str: The generated hash as a hexadecimal string.
    """

    return hashlib.sha1(message.encode()).hexdigest()

# SHA-256 Hashing with Salt
def sha256_hash_with_salt(message, salt):

    """
    Generates a SHA-256 hash of a given message with a given salt.

    Args:
        message (str): The message to hash.
        salt (str): The salt to use for hashing.

    Returns:
        str: The generated hash as a hexadecimal string.
    """

    return hashlib.sha256(salt + message.encode()).hexdigest()

# Blake2b Hashing
def blake2b_hash(message):
    """
    Generates a BLAKE2b hash of a given message.

    Args:
        message (str): The message to hash.

    Returns:
        str: The generated hash as a hexadecimal string.
    """

    return hashlib.blake2b(message.encode()).hexdigest()

# Generate SHA3-512 Hash
def sha3_512_hash(message):

    """
    Generates a SHA3-512 hash of a given message.

    Args:
        message (str): The message to hash.

    Returns:
        str: The generated hash as a hexadecimal string.
    """

    return hashlib.sha3_512(message.encode()).hexdigest()

# Sodium CryptoBox (Public Key Encryption)
def sodium_cryptobox(public_key, secret_key, message):

    """
    Encrypts a message using the Sodium CryptoBox public key encryption algorithm.

    Args:
        public_key (bytes): The public key to use for encryption.
        secret_key (bytes): The secret key to use for encryption.
        message (str): The message to encrypt.

    Returns:
        bytes: The encrypted message.
    """

    return public_key.encrypt(message.encode())

# Sodium CryptoSign (Signature)
def sodium_cryptosign(secret_key, message):

    """
    Signs a message using the Sodium CryptoSign signature algorithm.

    Args:
        secret_key (bytes): The secret key to use for signing.
        message (str): The message to sign.

    Returns:
        bytes: The signature of the message.
    """

    return secret_key.sign(message.encode())

# AES Key Wrap Algorithm
def aes_key_wrap(key, data):

    """
    Wraps a key using the AES key wrap algorithm with GCM mode.

    Args:
        key (bytes): A 32 byte key suitable for use with AES.
        data (str): The data (key) to be wrapped.

    Returns:
        bytes: The wrapped key.
    """

    cipher = Cipher(algorithms.AES(key), modes.GCM(), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data.encode()) + encryptor.finalize()

# SHA-512 HMAC
def hmac_sha512(key, message):
    """
    Generates an HMAC using SHA-512 for a given key and message.

    Args:
        key (str): The key to use for HMAC generation.
        message (str): The message to authenticate.

    Returns:
        bytes: The generated HMAC as bytes.
    """

    hmac_obj = HMAC(key.encode(), hashes.SHA512(), backend=default_backend())
    hmac_obj.update(message.encode())
    return hmac_obj.finalize()

# Create Digital Certificate
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.x509 import (
    CertificateBuilder,
    Name,
    NameAttribute,
    SubjectAlternativeName,
    DNSName,
    IPAddress,
)
from cryptography.x509.oid import NameOID, ExtensionOID
from cryptography.hazmat.backends import default_backend
import datetime
import ipaddress

def create_certificate(private_key, public_key, subject_name, issuer_name):
    """
    Creates a digital certificate using the given private and public keys, subject name, and issuer name.

    Args:
        private_key (cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKey): The private key to use for signing the certificate.
        public_key (cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey): The public key to use for the certificate.
        subject_name (str): The subject name of the certificate.
        issuer_name (str): The issuer name of the certificate.

    Returns:
        cryptography.x509.Certificate: The generated certificate.
    """
    from cryptography import x509
    
    # Define the subject and issuer name
    subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, subject_name)])
    issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, issuer_name)])

    # Build the certificate
    certificate = (
        CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(public_key)
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
        .add_extension(
            SubjectAlternativeName([DNSName("localhost"), IPAddress(ipaddress.ip_address("127.0.0.1"))]),
            critical=False,
        )
        .sign(private_key, hashes.SHA256(), default_backend())
    )

    return certificate

# Example usage:

# Certificate Chain Validation
def validate_certificate_chain(cert_chain):

    """
    Validates a certificate chain by checking that each certificate in the chain can be loaded and that it contains a public key.

    Args:
        cert_chain (list): A list of PEM encoded certificates.

    Returns:
        bool: True if the certificate chain is valid, False if it is not.
    """

    from cryptography.hazmat.backends import default_backend
    from cryptography.x509 import load_pem_x509_certificate

    for cert in cert_chain:
        try:
            cert_obj = load_pem_x509_certificate(cert, default_backend())
            cert_obj.public_key()
        except Exception as e:
            return False
    return True

# X.509 Certificate Revocation List Parsing
def parse_crl(crl_data):

    """
    Parses a Certificate Revocation List (CRL) from a PEM encoded string.

    Args:
        crl_data (str): The PEM encoded CRL string.

    Returns:
        dict: A dictionary containing revoked certificates, where the keys are the serial numbers and the values are the revoked certificates.
    """

    from cryptography.x509 import load_pem_x509_crl

    crl = load_pem_x509_crl(crl_data)
    revoked_certificates = crl.get_revoked_certificate_by_serial_number()
    return revoked_certificates

# RSA Key Import and Export in PEM Format
def import_rsa_key_from_pem(pem_data):
    """
    Imports an RSA key from a PEM encoded string.

    Args:
        pem_data (str): The PEM encoded key string.

    Returns:
        cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKey: The imported RSA key.
    """


    private_key = serialization.load_pem_private_key(pem_data, password=None, backend=default_backend())
    return private_key

# PKCS7 Padding
def pkcs7_padding(data, block_size=16):
    

    """
    Applies PKCS7 padding to the given data.

    Args:
        data (bytes): The data to pad.
        block_size (int): The block size to pad to. Defaults to 16.

    Returns:
        bytes: The padded data.

    Notes:
        The padding is done by adding bytes to the end of the data, each
        with the value equal to the number of padding bytes.
    """

    padding_length = block_size - (len(data) % block_size)
    return data + bytes([padding_length] * padding_length)



# RC4 Encryption
def rc4_encrypt(key, plaintext):

    """
    Encrypts a message using the RC4 stream cipher.

    Args:
        key (bytes): The key to use for encryption.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message.
    """

    cipher = Cipher(algorithms.ARC4(key), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext.encode())

# Generate RSA Key Pair in PEM Format
def generate_rsa_pem_key_pair(bits=2048):

    """
    Generates a pair of RSA keys in PEM format.

    Args:
        bits (int): The size of the key in bits. Defaults to 2048.

    Returns:
        tuple: A tuple containing the private and public keys as PEM encoded strings.
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=bits,
        backend=default_backend()
    )
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_pem, public_pem

# Elliptic Curve Diffie-Hellman (ECDH)
def ecdh_shared_secret(private_key, public_key):

    """
    Computes the shared secret using Elliptic Curve Diffie-Hellman (ECDH).

    Args:
        private_key (EllipticCurvePrivateKey): The private key used for the exchange.
        public_key (EllipticCurvePublicKey): The public key used for the exchange.

    Returns:
        bytes: The shared secret derived from the private and public keys.
    """

    shared_secret = private_key.exchange(ec.ECDH(), public_key)
    return shared_secret

# Generate AES Key for PBE
def generate_aes_key_pbe(password, salt):

    """
    Derives a 256-bit AES key from a password using the PBKDF2 key derivation function.

    Args:
        password (str): The password to use for key derivation.
        salt (bytes): The salt to use for key derivation.

    Returns:
        bytes: The derived AES key.
    """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# AES CFB Mode Encryption
def aes_encrypt_cfb(key, plaintext):

    """
    Encrypts a message using AES CFB mode encryption.

    Args:
        key (bytes): A 32 byte key suitable for use with AES.
        plaintext (str): The message to encrypt.

    Returns:
        bytes: The encrypted message, with the IV prepended.
    """

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return iv + encryptor.update(plaintext.encode()) + encryptor.finalize()

 

# Generate SHA256 HMAC
def hmac_sha256(key, message):

    """
    Generates an HMAC using SHA-256 for a given key and message.

    Args:
        key (str): The key to use for HMAC generation.
        message (str): The message to authenticate.

    Returns:
        bytes: The generated HMAC as bytes.
    """

    hmac_obj = HMAC(key.encode(), hashes.SHA256(), backend=default_backend())
    hmac_obj.update(message.encode())
    return hmac_obj.finalize()

# Create MD5 HMAC
def hmac_md5(key, message):

    """
    Generates an HMAC using MD5 for a given key and message.

    Args:
        key (str): The key to use for HMAC generation.
        message (str): The message to authenticate.

    Returns:
        bytes: The generated HMAC as bytes.
    """

    hmac_obj = HMAC(key.encode(), hashes.MD5(), backend=default_backend())
    hmac_obj.update(message.encode())
    return hmac_obj.finalize()

# RSA Signing and Verification
def rsa_sign_and_verify(private_key, public_key, message):

    """
    Signs a message using an RSA private key and verifies the signature using the public key.

    Args:
        private_key (RSAPrivateKey): The private key to use for signing.
        public_key (RSAPublicKey): The public key to use for verification.
        message (str): The message to sign and verify.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """

    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except:
        return False

# Generate Random Number (Secure)
def generate_secure_random():

    """
    Generates 16 bytes of secure random data.

    Returns:
        bytes: 16 bytes of cryptographically secure random data.
    """

    return os.urandom(16)
import hashlib
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import json
import time

# Cryptographic Time-Stamping
def cryptographic_timestamp(message):
    # Creating a timestamp using current time and hashing the message with timestamp

    """
    Creates a cryptographic timestamp for a given message.

    This function creates a timestamp using the current UNIX time, appends it to the given message, and then hashes the result using SHA-256. The resulting hash and timestamp are returned.

    Args:
        message (str): The message to timestamp.

    Returns:
        dict: A dictionary containing the timestamp and hash of the message with timestamp.
    """

    timestamp = int(time.time())  # Current UNIX timestamp
    message_with_timestamp = f"{message} | Timestamp: {timestamp}"
    
    # Creating a hash of the message with timestamp
    hash_object = hashes.Hash(hashes.SHA256())
    hash_object.update(message_with_timestamp.encode())
    timestamp_hash = hash_object.finalize()
    
    # Return the hash and timestamp
    return {
        "timestamp": timestamp,
        "message_hash": base64.b64encode(timestamp_hash).decode()
    }

# NTRU Encryption (Simplified)
# Note: Full NTRU encryption implementation typically requires a library that supports NTRU, 
# but here is a placeholder logic showing how the encryption might look.

def ntru_encrypt(message):
    # Placeholder for NTRU encryption - typically requires specific cryptography library

    """
    Encrypts a message using the NTRU encryption algorithm.

    This is a placeholder function, and real-world encryption would require a specific cryptography library.

    Args:
        message (str): The message to encrypt.

    Returns:
        str: The encrypted message.

    Note:
        This is a simplified example and does not actually use NTRU encryption. In a real-world scenario, you would need to use a library that supports NTRU encryption.
    """

    encrypted_message = hashlib.sha256(message.encode()).hexdigest()  # Fake encryption for demonstration
    return encrypted_message

# Zero-Knowledge Proofs (ZKP)
# A simplified version of a Zero-Knowledge Proof (ZKP) for demonstrating proof that someone knows a secret.
def zero_knowledge_proof(secret):
    # ZKP simplified for illustration: This demonstrates proof without revealing the secret
    """
    Simplified Zero-Knowledge Proof (ZKP) for demonstration purposes.

    Demonstrates proof that someone knows a secret without revealing the secret.

    This is a gross simplification of a real-world ZKP, and should not be used in production.

    Args:
        secret (str): The secret to prove knowledge of.

    Returns:
        str: The proof of knowledge (a SHA-256 hash of the secret).

    Note:
        This is a simplified example and should not be used for any real-world cryptographic purposes.
    """

    proof = hashlib.sha256(secret.encode()).hexdigest()
    # In a real-world scenario, this would involve complex cryptographic protocols.
    return proof

# EdDSA (Edwards Curve Signature) - Ed25519
def eddsa_sign(private_key, message):
    # Generate the signing key from the private key

    """
    Signs a message using the Ed25519 signature algorithm.

    Args:
        private_key (bytes): The private key to use for signing.
        message (str): The message to sign.

    Returns:
        str: The signature of the message, encoded as a base64 string.

    Note:
        This function uses the Ed25519 signature algorithm, which is a specific
        implementation of the EdDSA signature algorithm.
    """

    signing_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_key)
    
    # Sign the message
    signature = signing_key.sign(message.encode())
    
    # Return the signature
    return base64.b64encode(signature).decode()

# EdDSA Signature Verification
def eddsa_verify(public_key, message, signature):

    """
    Verifies the signature of a message using the Ed25519 signature algorithm.

    Args:
        public_key (bytes): The public key to use for verification.
        message (str): The message to verify.
        signature (str): The signature of the message, encoded as a base64 string.

    Returns:
        bool: True if the signature is valid, False if the signature is invalid or an error occurred.

    Note:
        This function uses the Ed25519 signature algorithm, which is a specific
        implementation of the EdDSA signature algorithm.
    """

    try:
        # Convert base64-encoded signature back to bytes
        signature_bytes = base64.b64decode(signature)
        
        # Convert the public key into a Ed25519PublicKey object
        public_key_object = ed25519.Ed25519PublicKey.from_public_bytes(public_key)
        
        # Verify the signature
        public_key_object.verify(signature_bytes, message.encode())
        
        return True  # Signature is valid
    except Exception as e:
        return False  # Signature is invalid or an error occurred


