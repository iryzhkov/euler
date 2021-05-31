from mathematics.numbers.decompose import decompose_full

import numpy as np

min_divisors = int(input())

memory = {}
def num_divisors(n):
    if n in memory:
        return memory[n]
    
    decomposition = np.array(decompose_full(n)) + 1
    memory[n] = np.product(decomposition)
    return memory[n]

def num_divisors_triangle(index):
    if index % 2 == 0:
        return num_divisors(index // 2) * num_divisors(index + 1)
    else:
        return num_divisors(index) * num_divisors((index + 1) // 2)

n = 1
while num_divisors_triangle(n) <= min_divisors:
    n += 1

print((n * (n + 1)) // 2)
