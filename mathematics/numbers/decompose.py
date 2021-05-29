"""Discrete number operations.
"""
from mathematics.sequences import Primes
from mathematics.numbers.operations import isqrt

def decompose_efficient(n: int):
    """Decompose the number to its prime factors.

    Args:
        n: the number to decompose.
    
    Returns:
        An array and reminder, such that P(p[i] ** a[i]) * reminder = n
        The primes in the decomposition are less than isqrt(n).
    """
    primes = list(Primes(1, isqrt(n) + 1))
    result = []
    for prime in primes:
        count = 0
        while n % prime == 0:
            n = n // prime
            count += 1
        result.append(count)
        
        if n == 1 or n < prime:
            break
    
    if sum(result) == 0:
        return [], n

    return result, n

def decompose_full(n: int):
    """Decompose the number to its prime factors.

    Args:
        n: the number to decompose.
    
    Returns:
        An array and reminder, such that P(p[i] ** a[i]) * reminder = n
        The primes in the decomposition are less than isqrt(n).
    """
    primes = list(Primes(1, n + 1))
    result = [0] * len(primes)
    for index, prime in enumerate(primes):
        while n % prime == 0:
            n = n // prime
            result[index] += 1
        
        if n == 1:
            break

    return result