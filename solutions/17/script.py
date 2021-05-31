from num2words import num2words

max_number = int(input())

def count_letters(n):
    return len(num2words(n).replace(" ", "").replace("-", ""))

print(sum(map(count_letters, range(1, max_number + 1))))