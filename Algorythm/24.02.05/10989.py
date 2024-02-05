# import sys
# sys.stdin = open('10989.txt','r')
import sys
input = sys.stdin.readline

N = int(input())
number_dict = {}
def solve(): # 함수 사용으로 시간 줄이기
    for i in range(N): # O(N)
        number = int(input())
        try :
            number_dict[number] += 1
        except KeyError :
            number_dict[number] = 1
    number_list = list(number_dict.keys()) # O(K)
    number_list.sort()

    for n in number_list: # O(K+N)
        for _ in range(number_dict[n]):
            print(n)

solve()