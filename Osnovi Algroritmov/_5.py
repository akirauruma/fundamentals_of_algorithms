x_values = []
y_values = []
x = 10
while x <= 19.0:
    y = 2*x**2 + x**3 - 7*x + 2
    x_values.append(x)
    y_values.append(y)
    x += 1.6
print("Координаты Ох:", x_values)
print("Координаты Оу:", y_values)
print("Произведение первых четырех значений:", y_values[0]*y_values[1]*y_values[2]*y_values[3])
print("Сумма последних девяти значений:", sum(y_values))
