# import sys
# sys.stdin = open('11651.txt', 'r')
#
import sys
input = sys.stdin.readline

N = int(input())

def space():
    number_dict = {}
    for _ in range(N):
        X, Y = map(int, input().split())

        try : number_dict[Y].append(X)
        except KeyError : number_dict[Y] = [X]

    key = list(number_dict.keys())
    key.sort() # y에 대한 정렬
    letter = str()
    for number_y in key:
        value = number_dict[number_y]
        value.sort()
        for number_x in value:
            letter += f'{number_x} {number_y}\n'
    print(letter)

space()

