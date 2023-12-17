number = int(input("Введите шестизначное число: "))
while number > 0:
    print(f"{number} / 10 = {number // 10}")
    number //= 10
