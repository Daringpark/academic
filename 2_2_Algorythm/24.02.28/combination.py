


'''
['A', 'B', 'C', 'D', 'E']
ABC
ABD
ABE

ACD
ACE

ADE

BCD
BCE

BDE

CDE


'''

N, K = 6, 3
arr = ['A', 'B', 'C', 'D', 'E', 'F']
# 직접 짠 combination << 다른 문제를 풀이할 수가 없음...
def combination(n, c):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                for k in range(n): # 이 경우, 하드 코딩...
                    if j < k:
                        res = ''
                        cnt += 1
                        res += arr[i]
                        res += arr[j]
                        res += arr[k]
                        # res값에 저장하면서 결국 NC3으로 만들 수 밖에 없음
                        print(res, cnt)
combination(N, K)

def combination_1(lvl, start):
    if lvl == K:
        print(path)
        return

    # 재귀호출
    for i in range(start, N):
        path.append(arr[i])
        combination_1(lvl+1, i+1)
        path.pop()

path = []
combination_1(0, 0)

die_numbers = 2
def die_rolling(lvl, start):
    if lvl == die_numbers:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        die_rolling(lvl+1, i)
        path.pop()

die_rolling(0,1)




