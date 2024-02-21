
def enq(n):
    # 완전 이진 트리 방식
    global last
    last += 1
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last # 부모 자식 비교를 위해서
    p = c//2 # 부모번호를 계산 이진트리
    while p >= 1 and h[p] < h[c]: # 자식이 더 클 경우, 그 자리를 교체해라
        h[p], h[c] = h[c], h[p]
        # 룰에 맞게 부모와 자식을 초기화
        c = p
        p = c//2

def deq():
    global last
    tmp = h[last]
    h[1] = h[last]
    last -= 1
    p = 1




N = 10
h = [0]*N+1
last = 0