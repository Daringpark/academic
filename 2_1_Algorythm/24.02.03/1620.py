# import sys
# sys.stdin = open('1620.txt', 'r')
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Book_name = {}
for i in range(1, N+1): #이름을 dictionary key로 저장
    Book_name[input().strip()] = i # O(N)
Book_number = list(Book_name.keys()) # pokemon key를 list로 받아주기

for i in range(M):
    K = input().strip()
    if K.isdigit():
        print(Book_number[int(K)-1]) # integer 변환
    else:
        print(Book_name[K])
