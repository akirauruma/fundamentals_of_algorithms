with open("data.txt", "r") as data:
    chars = data.readline().strip()
    int_values = list(map(int, data.readline().split()))

print(f"{chars}, {int_values}")
print(f"Среднее арифметическое: {sum(int_values)/len(int_values)}")
