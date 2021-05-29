from mathematics.sequences import Primes
from mathematics.numbers.decompose import decompose_full

n = int(input())

decompositions = [decompose_full(i) for i in range(1, n+1)]
max_length = max(map(len, decompositions))
powers = [0] * max(map(len, decompositions))
for decomposition in decompositions:
    for i in range(len(decomposition)):
        powers[i] = max(powers[i], decomposition[i])

result = 1
for i, p in enumerate(powers):
    result *= Primes(i) ** p
print(result)
