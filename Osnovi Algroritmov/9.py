num = input("Введите шестизначное целое число: ")

if len(num) != 6 or not num.isdigit():
    print("Введено не шестизначное число.")
else:
    if num[:3] == num[5:2:-1]:
        print("Число симметрично.")
    else:
        print("Число несимметрично.")
