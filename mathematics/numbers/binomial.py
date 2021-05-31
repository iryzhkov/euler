"""Binomial coefficient calculations.
"""
import numpy as np

class MetaBinomial(type):
    def __call__(cls, *args):
        """Either returns nth prime number of returns primes in range [start, end).

        Returns:
            Either nth prime number of returns primes in range [start, end).
        """
        if len(args) == 1:
            return cls[args[0]]
        elif len(args) == 2:
            return cls.get(*args)

    def __getitem__(cls, key: int):
        """Returns binomial coefficients for (a + b) ** n.

        Args:
            key: n.

        Returns:
            The binomial coefficients for (a + b) ** n.
        """
        cls.update(key)
        return cls._memory[key] 

class Binomial(metaclass=MetaBinomial):
    _memory = [[1]]
    _level = 0

    @classmethod
    def reset(cls):
        """Resets the calculated values.
        """
        cls._memory = [[1]]
        cls._level = 0
    
    @classmethod
    def update(cls, level):
        """Calculates values at level.

        Args:
            levels: the level to which calculate.
        """
        if level <= cls._level:
            return

        prev_level = cls._memory[cls._level]
        for _ in range(cls._level, level):
            new_level = [1] + [prev_level[i] + prev_level[i + 1] for i in range(len(prev_level) - 1)] + [1]
            cls._memory.append(new_level)
            prev_level = new_level
        
        cls._level = level   
    
    @classmethod
    def get(cls, n: int, k: int):
        """Returns binomial coefficient for kth element from (a + b) ** n.

        Args:
            n: the layer number.
            k: the element in the layer.
        
        Returns:
            Binomial coefficient for kth element from (a + b) ** n.
        """
        if k > n or k < 0:
            raise ValueError("K should not be bigger than N")

        cls.update(n)
        return cls._memory[n][k]