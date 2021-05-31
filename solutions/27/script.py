from mathematics.sequences import Primes

max_a, max_b = map(int, input().split())

def sequence_length(a, b):
    length = 0
    while (length ** 2 + a * length + b) in Primes:
        length += 1
    return length

max_length = -1
result = 0

for b in Primes(1, max_b + 1):
    for a in range(max(-max_a + 1, -b + 1), max_a):
        length = sequence_length(a, b)
        if length > max_length:
            max_length = length
            result = a * b

print(result)