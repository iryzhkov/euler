from functools import partial

divisors = map(int, input().split())
n = int(input())

def multiple_of(x, divisor):
    return x % divisor == 0

numbers = set()
for divisor in divisors:
    numbers.update(filter(partial(multiple_of, divisor=divisor), range(1, n)))

print(sum(numbers))