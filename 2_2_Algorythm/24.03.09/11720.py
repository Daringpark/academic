
N = int(input())
number = int(input())
res = 0
while number != 0:
    res += number%10
    number //= 10
print(res)