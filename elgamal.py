import math
import random

def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modexp(base, exp, modulus):
    return pow(base, exp, modulus)

def SS(num, iConfidence):
    for _ in range(iConfidence):
        a = random.randint(1, num - 1)
        if gcd(a, num) > 1:
            return False
        if not jacobi(a, num) % num == modexp(a, (num - 1) // 2, num):
            return False
    return True

def jacobi(a, n):
    if a == 0:
        return 1 if n == 1 else 0
    elif a == -1:
        return 1 if n % 2 == 0 else -1
    elif a == 1:
        return 1
    elif a == 2:
        if n % 8 in (1, 7):
            return 1
        elif n % 8 in (3, 5):
            return -1
    elif a >= n:
        return jacobi(a % n, n)
    elif a % 2 == 0:
        return jacobi(2, n) * jacobi(a // 2, n)
    else:
        if a % 4 == 3 and n % 4 == 3:
            return -1 * jacobi(n, a)
        else:
            return jacobi(n, a)

def find_primitive_root(p):
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1
    while True:
        g = random.randint(2, p - 1)
        if not (modexp(g, (p - 1) // p1, p) == 1):
            if not modexp(g, (p - 1) // p2, p) == 1:
                return g

def find_prime(iNumBits, iConfidence):
    while True:
        p = random.randint(2 ** (iNumBits - 2), 2 ** (iNumBits - 1))
        while p % 2 == 0:
            p = random.randint(2 ** (iNumBits - 2), 2 ** (iNumBits - 1))
        while not SS(p, iConfidence):
            p = random.randint(2 ** (iNumBits - 2), 2 ** (iNumBits - 1))
            while p % 2 == 0:
                p = random.randint(2 ** (iNumBits - 2), 2 ** (iNumBits - 1))
        p = p * 2 + 1
        if SS(p, iConfidence):
            return p

