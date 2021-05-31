import numpy as np

height, width, n = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(height)]
array = np.array(array)

def max_product_in_list(a):
    if len(a) < n:
        return 0

    value = np.product(a[:n])
    result = value
    for i in range(len(a) - n):
        value = (value * a[i + n]) // a[i]
        result = max(result, value)

    return result

def max_product_in_lists(lists):
    return max(map(max_product_in_list, lists))

def get_diagonals(a):
    return [a.diagonal(i) for i in range(len(a))] + [a.diagonal(i, 1, 0) for i in range(1, a.shape[1])]

result = max(max_product_in_lists(array), max_product_in_lists(array.T),
             max_product_in_lists(get_diagonals(array)), max_product_in_lists(get_diagonals(np.flip(array, 1))))
print(result)