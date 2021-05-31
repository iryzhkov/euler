num_digits, n = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

result = str(sum(numbers))[:num_digits]
print(result)