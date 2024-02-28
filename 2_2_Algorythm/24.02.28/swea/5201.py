
'''
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
'''
'''
18 13 12 11x 2
20 20 17 9 9
18 13 12 2
= 45
'''

'''
1
3 2
1 5 3
8 3
'''
'''
5 3 1x (trucks False)
8 3
5 3
= 8
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort()
    trucks.sort()
    # 뒤에 있는걸 기준으로 하나씩 제거하는 형태면 될 것 같다.
    # 트럭 용량이 맞지 않을 경우, 그 다음 idx로 넘어간다.
    # 다시 맞을 경우는 idx -1로 초기화 시켜준다.
    idx = N-1
    max_amount = 0
    while idx != -1:   # 트럭을 다 사용할 경우, 시뮬레이션 종료
        if containers and trucks and containers[idx] <= trucks[-1]: # 트럭이나 컨테이너에 있는 값이 아예 없으면 시뮬레이션을 종료해야 된다.
            trucks.pop() # 제거
            max_amount += containers.pop(idx)
            idx -= 1
        else : # 0까지 idx를 내려준다.
            idx -= 1 # 해당하는 컨테이너를 찾지 못한 경우이기에 한 칸 뒤로 넘어간다.
    print(f'#{tc} {max_amount}')