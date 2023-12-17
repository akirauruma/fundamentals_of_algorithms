import random


int1 = random.randint(-8, 12)
int2 = random.randint(-8, 12)
float1 = random.uniform(-8, 12)
float2 = random.uniform(-8, 12)


with open("output.txt", "w") as output:
    output.write(f"{int1}\n")
    output.write(f"{int2}\n")
    output.write(f"{float1:.2f}\n")
    output.write(f"{float2:.2f}\n")
