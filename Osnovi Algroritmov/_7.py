def calculation(x, y, z):
    return x * y + z

with open("input.txt", "r") as file:
    x = int(file.readline().strip())
    y = int(file.readline().strip())
    z = int(file.readline().strip())

if x and y and z:
    print(calculation(x, y, z))
else:
    print("Недопустимое значение переменной.")
