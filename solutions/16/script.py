number, power = map(int, input().split())
print(sum(int(c) for c in str(number ** power)))