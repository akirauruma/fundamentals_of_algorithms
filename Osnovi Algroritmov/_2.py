import random

numbers = [i for i in range(836, 1974) if i % 10 == 0]
chosen_numbers = random.sample(numbers, 12)

with open("output2.txt", "w") as f:
    for num in chosen_numbers:
        f.write('\n' + str(num) + '\n')
