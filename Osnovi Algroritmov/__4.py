with open("input1.txt", "r") as file:
    array = list(map(int, file.readline().split()))
print(array)

new_array = []
previous_digit = 0
for num in array:
    new_array.append(num * (previous_digit % 10))
    previous_digit = num
print(new_array)
