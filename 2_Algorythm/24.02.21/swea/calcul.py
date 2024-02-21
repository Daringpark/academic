import sys
sys.stdin = open("calcul.txt")

def cal(oper, A, B):
    if oper == '+':
        return A+B
    elif oper == '-':
        return A-B
    elif oper == '*':
        return A*B
    else:
        return A/B if B else 0

def solve():
    order = N + 1 # order식으로 하고 싶어서
    # if graph_operator[order//2]: # 첫 번째 시행, operator가 있으면, 무조건 연산을 하게금 입력이 들어온다.
    #     graph[order//2] = cal(graph_operator[order//2], graph[order-1], graph[order])
    while not result_graph[1]: # root node까지 채워질 때,
        order -= 1
        if len(graph[order]) != 1:
            lt = int(graph[order][1])
            rt = int(graph[order][2])
            result_graph[order] = cal(graph[order][0], result_graph[lt], result_graph[rt])
        else : result_graph[order] = int(graph[order][0])
    return result_graph[1]

for tc in range(1, 11):
    N = int(input()) #정점 개수
    graph = [0] * (N+1) # oper, lt, rt
    result_graph = [0] * (N+1) # 값을 저장
    for i in range(N):
        temp = input().split()
        graph[int(temp[0])] = temp[1:]
    # print(graph)
    # print(graph_operator)

    print(f'#{tc} {round(solve())}')