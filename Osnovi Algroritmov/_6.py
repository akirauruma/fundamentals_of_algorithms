def print_to_console(N):
    for i in range(-N, N+1):
        if i % 2 == 0:
            print(i)

def print_to_file(N):
    with open("output3.txt", "w") as f:
        for i in range(-N, N+1):
            if i % 3 == 0:
                f.write(str(i) + '\n')
N = int(input("Введите значение N: "))
print_to_console(N)
print_to_file(N)
