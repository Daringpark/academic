



N = int(input())
Numbers = list(map(int, input().split())) # 숫자들을 배열로 저장한다.
Memo_1 = [1] * N # 길이가 1인 것이 시작점, 왼쪽으로 보기
Memo_2 = [1] * N # 길이가 1인 것이 시작점, 오른쪽으로 보기

for i in range(1, N):
    if Numbers[i] >= Numbers[i-1]:
        Memo_1[i] = max(Memo_1[i], Memo_1[i-1]+1)
    if Numbers[i] <= Numbers[i-1]:
        Memo_2[i] = max(Memo_2[i], Memo_2[i-1]+1)
print(max(max(Memo_1), max(Memo_2)))