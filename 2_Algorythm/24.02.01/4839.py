import sys
sys.stdin = open('4839.txt', 'r')

T = int(input())
# A는 l을 변경, B는 R을 변경
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    lt = 1
    rt = P

    cntA = 0
    cntB = 0
    while rt >= lt: # 좌측 뿌리가 우측 뿌리보다 커졌을 때
        c = (lt + rt) // 2
        if c == A:
            break
        elif c > A:
            rt = c
            cntA += 1
        else:
            lt = c
            cntA += 1
    lt = 1
    rt = P
    while rt >= lt: # 좌측 뿌리가 우측 뿌리보다 커졌을 때
        c = (lt + rt) // 2
        if c == B:
            break
        elif c > B:
            rt = c
            cntB += 1
        else:
            lt = c
            cntB += 1
    if cntA < cntB:
        print(f'#{tc} A')
    elif cntA > cntB:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')