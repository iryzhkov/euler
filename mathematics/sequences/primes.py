"""A sequence of prime numbers.
"""
from mathematics.numbers import isqrt
from mathematics.algorithms import binary_search

import numpy as np

MAX_SEARCH_SIZE = 20000000


class MetaPrimes(type):
    def __contains__(cls, n: int):
        """Checks if n is prime.

        Args:
            n: a number to check.

        Returns:
            True is n is prime, False otherwise.
        """
        n_sqrt = isqrt(n)
        cls.update(n_sqrt)
        for prime in cls._primes:
            if prime > n_sqrt:
                break
            if n % prime == 0:
                return False            

        return True

    def __call__(cls, *args):
        """Either returns nth prime number of returns primes in range [start, end).

        Returns:
            Either nth prime number of returns primes in range [start, end).
        """
        if len(args) == 1:
            return cls[args[0]]
        elif len(args) == 2:
            return cls.range(*args)

    def __getitem__(cls, key: int):
        """Returns nth prime number.

        Args:
            key: the index of prime number.

        Returns:
            The nth prime number.
        """
        while key >= len(cls._primes):
            cls.update(min(cls._last_checked ** 2, cls._last_checked + MAX_SEARCH_SIZE))
        return cls._primes[key]
    
    def range(cls, start: int, end: int):
        """Returns primes in range [start, end).

        Args:
            start: the minimum value of the range, inclusive.
            end: the maximum value of the range, exclusive.
        
        Returns:
            Iterator with primes in the provided range.
        """
        cls.update(end)
        index = binary_search(cls._primes, start)
        while index < len(cls._primes) and cls._primes[index] < end:
            yield cls._primes[index]
            index += 1
        

class Primes(metaclass=MetaPrimes):
    _primes = [2]
    _last_checked = 2

    @classmethod
    def reset(cls):
        """Resets the calculated primes.
        """
        cls._primes = [2]
        cls._last_checked = 2

    @classmethod
    def update(cls, n: int):
        """Updates the prime list to include numbers up to n.

        Args:
            n: the upper limit.
        """
        if cls._last_checked > n or n <= 2:
            return

        if n % 2 == 1:
            n += 1
        
        cls.update(isqrt(n))

        seive_length = (n - cls._last_checked) // 2
        sieve = [True] * seive_length

        for prime in cls._primes[1:]:
            if prime ** 2 > cls._last_checked:
                start_index = prime ** 2 - cls._last_checked
            else:
                reminder = cls._last_checked % prime
                start_index = (prime - reminder) % prime
                if start_index % 2 == 0:
                    start_index += prime
            
            start_index = start_index // 2
            for i in range(start_index, seive_length, prime):
                sieve[i] = False

        for index, is_prime in enumerate(sieve):
            if is_prime:
                number = cls._last_checked + 1 + 2 * index
                cls._primes.append(number)

        cls._last_checked = n