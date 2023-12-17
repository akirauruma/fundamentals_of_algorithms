import random

N, M = 5, 5
A, B = 1, 100
init_array = [[random.randint(A, B) for _ in range(M)] for _ in range(N)]

with open("array.txt", "w") as f:
    for row in init_array:
        f.write(' '.join(map(str, row)) + '\n')
