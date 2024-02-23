
Original = 'Hello, Mr.King. Welcome to South Korea.'
text = 'Korea'

# Brute-force algo
# For문으로 구성
for i in range(len(Original) - len(text)): # 두 번의 for문 (N*M - M**2)
    for j in range(len(text)):
        if Original[i+j] != text[j]:
            break
    else:
        print('Bruteforce',i, Original[i:i+j+1])
        break
else: # for문을 중간에 멈추지 않았을 때, else문 
    print(-1)

# KMP algo(O(M+N))
# N = len(Original)
# M = len(text)
# lps = [0] * (M+1)

# j = 0 # 일치한 개수를 셈
# lps[0] = -1
# for i in range(1, M):
#     lps[i] = j
#     if text[i] == Original[j]:
#         j += 1
#     else :
#         j = 0
# lps[M] = j
#############
N = len(Original)
M = len(text)
lps = [0] * (M+1)
i = 0
j = 0
lps[0] = -1
while i < N and j <= M: # O(N)
    if j == -1 or Original[i] == text[j]:
        i += 1
        j += 1
    else :
        j = lps[j]
    if j == M:
        j = lps[j] # 값을 변환
        print('KMP',i-M, Original[i-M:i])

# 보이어 무어 알고리즘
def make(p):
    M = len(p)
    jump = [len(p)] * (ord('z') + 1)
    for idx in range(M):
        c = p[idx]
        jump[ord(c)] = M-1-idx # range(M-1,-1,-1)
    return jump

def find(p, t):
    # 길이 가져오기
    N = len(t)
    M = len(p)
    # 포지션 잡기
    ti = 0
    pi = M-1 # 뒤쪽 부터 보기
    while ti+pi<N and pi >= 0:
        if t[ti+pi] == p[pi]: # 뒤에서 앞으로 순차적으로 서칭 # -1에 도달하면 글자 밖(전체 서칭)
            pi -= 1
        else:
            pos = ord(t[ti+pi]) # 아스키코드로 호핑 지점 불러오기
            ti += make(p)[pos] # 얼마나 뛸지 ti +=
            pi = M-1 # 뒤 쪽부터 보겠다고 초기화
    if pi == -1:
        return f'pos="{ti}", word="{t[ti:ti + M]}"'
    else :
        return f'"Cannot find word!"'

t = 'a pattern matching algorythm'
p = 'rythm'
# jump의 list화 123개의 jump 위치
make(p)
print(find(p,t))

p = 'matcc'
make(p)
print(find(p, t))
# CR LF (carrige return : 다음 줄로, line feed: 라인 위쪽으로)
#a
#b
# 61 0D 0A 62 (a CR LF b)