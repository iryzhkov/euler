from mathematics.sequences import Primes
from mathematics.numbers.decompose import decompose_efficient

n = int(input())
decomposition, reminder = decompose_efficient(n)
print(max(reminder, Primes(len(decomposition) - 1)))