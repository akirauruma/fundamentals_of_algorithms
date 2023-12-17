import random

N = 10
A, B = 1, 100
array = [random.randint(A, B) for _ in range(N)]
print(array)

for num in array:
    if num % 100 // 10 == num % 10:  # Проверка двух последних цифр
        print(f"Первое число с одинаковыми двумя последними цифрами: {num}")
        break
else:
    print("Заданных чисел не обнаружено.")
