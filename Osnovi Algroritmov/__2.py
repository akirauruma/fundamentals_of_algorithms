import random

N = 10
A, B = 1, 100
array = [random.choice([i for i in range(A, B+1) if i % 2 == 0]) for _ in range(N)]
print(array)
