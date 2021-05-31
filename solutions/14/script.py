max_number = int(input())

max_idx = 1
memory = {}
def sequence_length(n):
    global max_idx, memory

    if n in memory:
        return memory[n]

    length = 0
    curr = n
    while curr != 1:
        length += 1
        if curr % 2 == 0:
            curr = curr // 2
        else:
            curr = 3 * curr + 1

        if curr in memory:
            length += memory[curr]
            break
    
    memory[n] = length
    if length > memory[max_idx]:
        max_idx = n

    return length

for i in range(1, max_number + 1):
    sequence_length(i)

print(max_idx)