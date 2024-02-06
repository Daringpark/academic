import sys
sys.stdin = open('input_1216.txt')

def is_p(lst, start, end): # 펠린드롬 확인 함수
    if start == 0:
        if lst[:end+1] == lst[end::-1]:
            return True
    else:
        if lst[start:end+1] == lst[end:start-1:-1]:
            return True
    return False

def solve(lst): # 길이만큼 리스트 순회하며 찾는 함수
    # 행, 열 순회
    for i in range(100): # 행 순회, 열 순회
        for j in range(1, 101):  # 초기 위치
            length = 100 - j + 1
            for l in range(length):
                if is_p(lst[i], j, j+l): # if 팰린드롬이 있다면, return cnt;
                    return length
                col_new = '' # string에 추가하기
                for k in range(l): # 100 99 98 97 ...
                    col_new += lst[j+k][i]
                col_new.strip()
                if is_p(col_new, 0, len(col_new)):
                    return length
    else:
        return 0
# 몇 케이스에서 더 낮은 수로 나오는 이유가 return 이후 for문을 다시 돌고 있음

for tc in range(1, 11):
    N = input()
    space = [list(input()) for _ in range(100)]
    max_cnt = 0
    if solve(space): # length가 할당되면 break
        max_cnt = solve(space)
        break
    else :
        max_cnt = 1
#
    print(f'#{tc} {max_cnt}')


