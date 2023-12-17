import random

N = 10
A, B = 1, 100
C, D = 1.0, 10.0
a = [random.randint(A, B) for _ in range(N)]
b = [random.uniform(C, D) for _ in range(N)]



print(a)
print(b)

with open("output.txt", "w") as f:
    for i in range(N):
        f.write(f"array_int[{i}] = {a[i]}; array_double[{i}] = {b[i]}\n")
