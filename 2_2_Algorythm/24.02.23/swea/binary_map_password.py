import sys
sys.stdin = open("binary.txt")

mapping_dict = {'0001101' : 0,
                '0011001' : 1,
                '0010011' : 2,
                '0111101' : 3,
                '0100011' : 4,
                '0110001' : 5,
                '0101111' : 6,
                '0111011' : 7,
                '0110111' : 8,
                '0001011' : 9}
def make_code():
    keylist = list(mapping_dict.keys())
    # 8자 뽑아내는 것을 어떻게 해야하나?
    # 완전 탐색 기법으로 80 - 56? 이후에 7자씩 끊어본다?
    # 하지만, 시작 지점은 잡아야 함.
    # 한 행에 주어지게 되어 있다. 이때 7개로 쪼개서 볼 때 8개 값이 나오는가? 그럼 출력하게금
    for row in range(N):
        for number in keylist:
            if number in matrix[row]:
                for i in range(M-56): # col에서 어디까지 확인할지
                    res = ''
                    for j in range(i, M, 7): # 시작 지점 잡기
                        if matrix[row][j:j+7] in keylist:
                            res += str(mapping_dict[matrix[row][j:j+7]])
                    if len(res) == 8:
                        return res
    return 0

def codetonumber(code):
    if code:
        number = 3 * (int(code[0]) + int(code[2]) + int(code[4]) + int(code[6])) + int(code[1]) + int(code[3]) + int(code[5]) + int(code[7])
    if number%10:
        return 0
    else:
        res = 0
        for i in range(8):
            res += int(code[i])
        return res

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)] # 2차원 array str
    print(f'#{tc} {codetonumber(make_code())}')

