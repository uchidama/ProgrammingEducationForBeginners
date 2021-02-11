import random

n = random.randint(1, 100)
print(n)

if n > 90:
    print("SR!!!!")
elif n > 70:
    print("Rare!")
else:
    print("Normal")

