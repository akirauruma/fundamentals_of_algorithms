N = int(input("Введите значение N: "))

with open("output1.txt", "w") as f:
    count = 0
    for i in range(-N, N+1):
        if i % 2 == 0:
            f.write(str(i) + ' ')
            count += 1
            if count == 10:
                f.write('\n')
                count = 0
        if i % 3 == 0:
            print(i)
