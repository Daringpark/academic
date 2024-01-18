import random

numbers = range(1, 46)

lotto = random.sample(numbers, 6)
lotto = sorted(lotto)

print(lotto)
