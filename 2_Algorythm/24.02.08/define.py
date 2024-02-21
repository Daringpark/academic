import sys
sys.stdin = open('define.txt')

def machine():
    if a == 1 or a == 5 or a == 6:
        return a
    elif a == 4 or a == 9:
        if b%2 == 1:
            return a
        else:
            return (a+2)%10
    else:
        if a == 3 or a == 7:
            x = [1,7,9,3]
            if a == 3: return x[-(b%4)]
            else: return x[b%4]
        elif a == 0:
            return 10
        else:
            x = [6,8,4,2]
            if a == 2: return x[-(b%4)]
            else: return x[(b%4)]

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    a = a%10
    print(machine())