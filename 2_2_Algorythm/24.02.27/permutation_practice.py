
'''
N = 3~8
'''
def make_permutation(x):
    global permutation_list
    if x == N:
        comp = []
        for i in range(N):
            comp.append(path[i])
        permutation_list.append(comp)
        return
    for i in range(N):
        if visited[i]: continue
        visited[i] = 1
        path.append(i)
        make_permutation(x+1)
        path.pop()
        visited[i] = 0

def solve():
    max_sum_value = 0
    pos = []
    for order in permutation_list:
        row = 0
        sum_value = 0
        for i in order:
            if matrix[row][i] >= 0:
                sum_value += matrix[row][i]
            else:
                sum_value = -1
                break
            row += 1
        print(sum_value, order)
        if sum_value > max_sum_value:
            max_sum_value = sum_value
            pos = order
    return max_sum_value, pos

N = 4
max_value = 0
matrix = [[1,2,3,4],
          [2,-3,4,5],
          [4,2,-1,1],
          [2,4,10,8]]
path = []
visited = [0] * (N+1)
permutation_list = []
make_permutation(0)
print(permutation_list)
### 하나의 list 내에 저장해서 사용할 수 있게
print(solve())