# import sys
# input = sys.stdin.readline

# 예외처리를 통해서 쉽게 풀려고 함. (KeyError를 Except해주기 위해서)
M = int(input())
cards = list(map(int, input().split()))
our_dict = dict()
for i in range(M):
    try :
        our_dict[cards[i]] += 1
    except KeyError:
        our_dict[cards[i]] = 1

N = int(input())
have_we = list(map(int, input().split()))
for i in range(N):
    try :
        print(our_dict[have_we[i]], end = ' ')
    except KeyError:
        print(0, end = ' ')
        
        
        
# ### get method로 풀이
# n = int(input()) # 불 필요한 입력
# d = {}
# l1 = list(map(int, input().split()))
# for i in l1: d[i] = d.get(i, 0)+1 # get emthod를 사용하여 dictionary 저장
# m = int(input()) # 불 필요한 입력
# l2 = list(map(int, input().split()))
# for i in l2: print(d.get(i, 0), end=' ') # get method를 사용하여 dictionary에서 default값 혹은 기존에 가진 값을 출력