num_lines, num_adjesent = map(int, input().split())
n = ""

for i in range(num_lines):
    n += input()

def product(array):
    result = 1
    for i in array:
        result *= int(i)
    return result

print(max([product(n[i:i+num_adjesent]) for i in range(len(n) - num_adjesent)]))