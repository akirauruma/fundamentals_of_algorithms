import random

N = 10
A, B = -100, 100
array = [random.randint(A, B) for _ in range(N)]
with open("output4.txt", "w") as f:
    for num in array:
        f.write(str(num) + '\n')
    if len(array) % 2 == 0:
        half = len(array) // 2
    else:
        half = len(array) // 2 + 1
    f.write(f"Минимальный положительный элемент в первой половине массива: {min([i for i in array[:half] if i > 0])}\n")
    f.write(f"Максимальный отрицательный элемент во второй половине массива: {max([i for i in array[half:] if i < 0])}\n")
