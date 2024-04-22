
# 1713 후보 추천하기


# 사진 틀은 20 이하
N = int(input())
# 구성을 


# 전체 학생의 투표 횟수 << 1000번 이하
Number = int(input())

# length가 Number인 리스트, 학생 번호는 1~ 100까지 있다.
vote = list(map(int, input().split()))

# 직접 돌면 될 것 같은데?
for k in range(Number):

    # 틀에 걸릴 녀석 번호
    n = vote[k]