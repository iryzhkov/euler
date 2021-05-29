n = int(input())

sum_sqares = (n * (n + 1) * (2*n + 1)) // 6
sum_sqared = ((n * (n + 1)) // 2) ** 2

print(sum_sqared - sum_sqares)