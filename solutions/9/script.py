from mathematics.numbers import isqrt

sum_to = int(input())

def generate_triplets(m, n):
    a = (m ** 2 - n ** 2)
    b = 2 * m * n
    c = (m ** 2 + n ** 2)
    return a, b, c

def find_product():
    ceiling = isqrt(sum_to) + 1
    for m in range(1, ceiling):
        for n in range(1, m):
            a, b, c = generate_triplets(m, n)
            current_sum = a + b + c
            if current_sum != 0 and sum_to % current_sum == 0:
                k = sum_to // current_sum
                return a * b * c * (k ** 3)

print(find_product())