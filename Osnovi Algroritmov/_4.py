count = 0
while count < 10:
    number = input("Введите целое число: ")
    first_digit = int(number[0])
    last_digit = int(number[-1])
    print(f"Сумма первой и последней цифры: {first_digit + last_digit}")
    count += 1
