"""Discrete number operations.
"""
def isqrt(n: int):
    """Returns the biggest number such that result ** 2 <= n.

    Args:
        n: the input number.

    Returns:
        x, such that x ** 2 <= n and (x + 1) ** 2 > n
    """
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x