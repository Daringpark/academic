import sys
sys.stdin = open("score.txt")

T = int(input())
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T+1):
    N, K = map(int, input().split()) # N은 학생 수, K는 확인하고자 하는 학생 번째
    students = []
    for _ in range(N):
        mid, final, report = map(int, input().split())
        students.append(mid*0.35 + final*0.45 + report*0.2)
    sorted_students = list(reversed(sorted(students)))
    school = dict()
    new_N = N//10 # 동일하게 들어갈 수 있는 한도
    pos = 0
    for i in range(10):
        for j in range(new_N):
            school[sorted_students[pos+j]] = score[i]
        pos += new_N
        if pos == N:
            break
    print(f'#{tc} {school[students[K-1]]}')






