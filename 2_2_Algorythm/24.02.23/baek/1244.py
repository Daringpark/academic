def toggle(no):
    switch[no] = (switch[no]+1) % 2 # 스위치 조작을 0,1을 나머지로
# if switch[no] == 1:
#     switch[no] = 0
# else:
#     switch[no] = 1
def m_do(no):
    for idx in range(no, N+1, no): # 뛰어주는 거리도, 결국 스위치 시작 지점부터 뛰어준다.
        toggle(idx)
def f_do(no):
    toggle(no) # 첫번째 스위치를 조작해주고
    s = no-1 # 왼쪽, 오른쪽 스위치를 조작하기 위한 인덱스를 만들어준다.
    e = no+1
    while s>=1 and e<=N and switch[s] == switch[e]: # 왼쪽이 0번째로 가거나 오른쪽이 제일 마지막 범위를 벗어나거나, 스위치가 같지 않을 때까지
            toggle(s) # 왼쪽, 오른쪽의 스위치를 조작해준다.
            toggle(e)
            s -= 1 # 왼쪽은 앞으로 움직이고
            e += 1 # 오른쪽은 뒤로 움직여준다.
N = int(input()) # 스위치 개수
switch = [0] + list(map(int, input().split())) # index를 쉽게 가져가려고 0번째를 추가
NUM = int(input()) # 액션의 갯수
for _ in range(NUM):
    sex, no = map(int, input().split()) # 성별과 조작할 스위치 넘버를 받는다.
    if sex == 1: # 성별에 따라서 다른 함수를 사용할 수 있게 조건문 입력
        m_do(no)
    else:
        f_do(no)
# 스위치를 조작하고 나서, 1부터 N까지의 스위치를 20개를 기준으로 출력한다.
for idx in range(1, N+1, 20):
    print(*switch[idx:idx+20])