from mathematics.sequences import Fibbonacci

upper_limit = int(input())
is_even = lambda x: x % 2 == 0
numbers = filter(is_even, Fibbonacci(0, upper_limit))
print(sum(numbers))