from mathematics.numbers import isqrt
from itertools import combinations_with_replacement

sum_to = int(input())

def generate_triplets(m, n, k):
    if (m <= n):
        return 0, 0, 0
    a = k * (m ** 2 - n ** 2)
    b = k * 2 * m * n
    c = k * (m ** 2 + n ** 2)
    return a, b, c


def find_product():
    ceiling = isqrt(sum_to) + 1
    for k in range(1, ceiling):
        for n, m in combinations_with_replacement(range(1, ceiling), 2):
            a, b, c = generate_triplets(m, n, k)
            if a + b + c == sum_to:
                return a * b * c

print(find_product())