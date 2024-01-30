number = 123456
N = 6

def babygin(numbers):
    lst = [0] * 12
    for n in range(6):
        lst[numbers%10] += 1
        numbers //= 10

    i = 0
    while i < 10 :

        return 10


print(babygin(number))
