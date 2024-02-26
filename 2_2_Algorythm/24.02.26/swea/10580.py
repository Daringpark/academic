'''
2
3
1 10
5 5
7 7
2
1 1
2 2
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rod_list = []
    for _ in range(N): # space 생성
        s, e = map(int, input().split())
        rod_list.append([s, e])
    cnt = 0
    for i in range(N): # 탐색 과정
        for j in range(N): # Brute-Force를 할거면 완벽하게 탐색하라
            if i != j:
                x_1 = rod_list[i][0]
                x_2 = rod_list[j][0]
                y_1 = rod_list[i][1]
                y_2 = rod_list[j][1]
                if x_1 < x_2  and y_1 > y_2:
                    cnt += 1
    print(f'#{tc} {cnt}')