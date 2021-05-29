"""Fibbonacci Sequence.
"""
from mathematics.algorithms import binary_search


class MetaFibbonacci(type):
    def __contains__(cls, n: int):
        """Checks if n is fibbonnacci number.

        Args:
            n: a number to check.

        Returns:
            True is n is a fibbonnacci number, False otherwise.
        """
        cls.update(n)
        index = binary_search(cls._numbers, n)
        return cls._numbers[index] == n

    def __call__(cls, *args):
        """Either returns nth fibbonacci number of returns fibbonacci numbers in range [start, end).

        Returns:
            Either nth prime number of returns primes in range [start, end).
        """
        if len(args) == 1:
            return cls[args[0]]
        elif len(args) == 2:
            return cls.range(*args)

    def __getitem__(cls, key: int):
        """Returns nth fibbonacci number.

        Args:
            key: the index of fibbonacci number.

        Returns:
            The nth fibbonacci number.
        """
        while key >= len(cls._numbers):
            cls.update(cls._numbers[-1] + cls._numbers[-2] + 1)
        return cls._numbers[key]
    
    def range(cls, start: int, end: int):
        """Returns fibbonacci numbers in range [start, end).

        Args:
            start: the minimum value of the range, inclusive.
            end: the maximum value of the range, exclusive.
        
        Returns:
            Iterator with fibbonacci numbers in the provided range.
        """
        cls.update(end)
        index = binary_search(cls._numbers, start)
        while index < len(cls._numbers) and cls._numbers[index] < end:
            yield cls._numbers[index]
            index += 1
        

class Fibbonacci(metaclass=MetaFibbonacci):
    _numbers = [0, 1, 1]

    @classmethod
    def reset(cls):
        """Resets the calculated fibbonacci numbers.
        """
        cls._numbers = [0, 1, 1]

    @classmethod
    def update(cls, n: int):
        """Updates the fibbonacci numbers list to include numbers up to n.

        Args:
            n: the upper limit.
        """
        while cls._numbers[-1] + cls._numbers[-2] <= n:
            cls._numbers.append(cls._numbers[-1] + cls._numbers[-2])