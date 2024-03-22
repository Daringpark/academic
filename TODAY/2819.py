



def dfs(s, n, r):
    
    # 기저조건 : n == 7 일때, 저장하고 종료하기
    if n == 7:
        result.add(r)
        return



    
    r += matrix[s[0]][s[1]]

        for dr, dc in drdc:
            new_row = s[0] + dr
            new_col = s[1] + dc

            if 0 <= row










T = int(input())


drdc = [[-1,0], [0,1], [0,-1], [1,0]]
for tc in range(1, T+1):
    
    matrix = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            start = [i,j]
            dfs(start, 0, '')