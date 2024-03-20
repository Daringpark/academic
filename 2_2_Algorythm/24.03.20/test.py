def make_set(data):
    idx = datas.index(data)
    p[idx] = idx

def find_set(data):
    idx = datas.index(data)
    while idx != p[idx]:
        idx = p[idx]
    # 대표값 출력
    return idx

def union_old(data1, data2):
    # 기존 데이터의 인덱스를 가지고 있는 모체의 인덱스를 idx1,2로 받는다.
    # depth를 생각하지 않음
    idx1 = p[datas.index(data1)]
    idx2 = p[datas.index(data2)]
    idx = min(idx1, idx2)
    p[idx1] = p[idx2] = idx

def union(data1, data2):
    # 기존 데이터의 인덱스를 가지고 있는 모체의 인덱스를 idx1,2로 받는다.
    idx1 = p[datas.index(data1)]
    idx2 = p[datas.index(data2)]
    link(idx1, idx2)

def link(idx1, idx2):
    if rank[idx1] < rank[idx2]:
        p[idx1] = idx2
    else:
        p[idx2] = idx1
        if rank[idx1] == rank[idx2]:
            rank[idx1] += 1 

datas = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
p = [-1] * len(datas)
rank = [0] * len(datas)
for data in datas:
    make_set(data)
# p[2] = 0
# p[5] = 4
print(p)
print(rank)
union('A1', 'A3')
union('B2', 'B3')
union('C2', 'B3')
union('B1', 'B2')
print(p)
print(rank)
print(find_set('A3'))
print(find_set('B3'))


