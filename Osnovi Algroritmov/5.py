with open("data1.txt", "r") as data1:
    float_values = list(map(float, data1.readline().split()))
    int_values = list(map(int, data1.readline().split()))

min_int = min(int_values)
max_float = max(float_values)

print(f"Наименьшее из целых: {min_int}")
print(f"Наибольшее из дробных: {max_float}")
