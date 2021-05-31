import numpy as np

size = int(input())
values = [np.array(list(map(int, input().split()))) for _ in range(size)]

best_results = [values[0][:]]

for curr_values in values[1:]:
    t = best_results[-1].copy()
    first = np.insert(t, 0, 0)
    second = np.append(t, 0) 
    best_option = np.amax(np.stack([first, second]), axis=0)
    best_results.append(best_option + curr_values)

print(max(best_results[-1]))