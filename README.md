ElGamal Encryption Algorithm — Python Implementation

1. Introduction
----------------
This project presents a formal implementation of the ElGamal Public-Key Cryptosystem in Python.
The ElGamal algorithm is an asymmetric encryption scheme based on the Diffie–Hellman key exchange principle.
It provides a method for secure message transmission by using two distinct keys: a public key for encryption and a private key for decryption.

The implementation includes key generation, encryption, and decryption, along with mathematical functions for prime number generation,
primitive root determination, and modular arithmetic operations. This program is developed entirely using Python’s standard library,
making it suitable for educational and experimental use.


2. Theoretical Background
--------------------------
The ElGamal encryption system operates over a finite cyclic group and relies on the intractability of the discrete logarithm problem for its security.
Given a large prime p, a primitive root g modulo p, and an exponent x, it is computationally infeasible to determine x from g^x mod p within
polynomial time for sufficiently large values of p.

Mathematical Framework
----------------------
Key Generation:
 - Select a large safe prime number p.
 - Find a primitive root g modulo p.
 - Choose a private key x randomly from [1, p-2].
 - Compute h = g^x mod p.

Public Key: (p, g, h)
Private Key: (p, g, x)

Encryption:
 - Represent the plaintext message M as an integer.
 - Select a random ephemeral key y from [1, p-2].
 - Compute:
   c1 = g^y mod p
   c2 = (M × h^y) mod p
 - The ciphertext is the pair (c1, c2).

Decryption:
 - Compute the shared secret s = c1^x mod p
 - Recover plaintext as M = (c2 × s^(-1)) mod p, where s^(-1) = s^(p-2) mod p.


3. Implementation Details
--------------------------
File Description:
 - elgamal.py : Contains the full implementation including key generation, encryption, decryption, and testing functions.
 - README.txt : Documentation describing algorithm design, usage, and theoretical background.

Class Definitions:
 - PublicKey: Represents the public key (p, g, h, iNumBits)
 - PrivateKey: Represents the private key (p, g, x, iNumBits)

Functional Overview:
 - generate_keys(iNumBits=256, iConfidence=32): Generates a public/private key pair.
 - find_prime(iNumBits, iConfidence): Generates a safe prime number using the Solovay–Strassen test.
 - find_primitive_root(p): Finds a primitive root modulo p.
 - encrypt(publicKey, plaintext): Encrypts a plaintext message using the public key.
 - decrypt(privateKey, ciphertext): Decrypts ciphertext using the private key.
 - encode() / decode(): Handles conversion between text and numerical form.
 - test(): Performs a self-test to validate correctness.


4. Usage Example
----------------
from elgamal import generate_keys, encrypt, decrypt

# Key generation
keys = generate_keys()
private_key = keys['privateKey']
public_key = keys['publicKey']

# Encryption
message = "Hello, this is a test message for ElGamal encryption!"
cipher = encrypt(public_key, message)

# Decryption
decrypted_message = decrypt(private_key, cipher)

print("Original Message: ", message)
print("Encrypted Message: ", cipher)
print("Decrypted Message: ", decrypted_message)


5. Testing
-----------
The test() function performs an encryption-decryption cycle to verify that the decrypted output matches the original message.


6. Dependencies
----------------
 - Python Standard Library (random, math, sys)
 - Compatible with Python 3.4 and above


7. Security Considerations
---------------------------
This implementation is for academic and research purposes only. It is not suitable for production use and lacks advanced
security mechanisms such as padding, side-channel protection, and optimized arithmetic.


8. Conclusion
--------------
This project demonstrates the core principles of the ElGamal public-key cryptosystem, including safe prime generation,
primitive root computation, and modular exponentiation, providing a clear example of asymmetric encryption.
