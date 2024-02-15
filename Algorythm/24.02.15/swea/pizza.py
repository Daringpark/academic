import sys
sys.stdin = open('pizza.txt')

# 10 중 8개 맞
def pizza_time():
    while len(count_list) != M-1: # M-1개의 피자를 꺼내기 전까지 돌아감
        if cheese and len(firepit) != N: # 피자 추가하기
            firepit.append(cheese.pop(0))
            firepit_order.append(order.pop(0))
        if firepit: # 화로에서 돌려주기
            melt = firepit.pop(0)
            melt = (melt)//2 # 녹았는지 확인
            real_order = firepit_order.pop(0)
            if melt: # 덜 녹았네
                firepit.append(melt)
                firepit_order.append(real_order)
            else: # 녹았네
                count_list.append(real_order) # 피자 나왔습니다. 배열 추가
    if firepit_order:
        return firepit_order.pop() # 한개 남은 피자의 번호를 뽑음
    else: return order.pop() # 0의 연속일 경우, M-1 꺼내고, 화덕에 피자를 넣지 않음

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 화로의 크기, 피자의 개수
    cheese = list(map(int, input().split())) # M개의 피자의 치즈 두께
    order = [i+1 for i in range(M)] # 1 ~ M 번째 피자 순서 번호
    firepit = [] # 화로 내 에서 치즈 확인
    firepit_order = [] # 화로 내 에서 피자 순번
    for i in range(N): # 초기 화덕 세팅
        firepit.append(cheese.pop(i))
        firepit_order.append(order.pop(i))
    count_list = [] # 치즈가 녹은 피자를 확인
    print(f'#{tc} {pizza_time()}')

