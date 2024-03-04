


T = int(input())
for tc in range(1, T+1):
    Matrix = [input() for _ in range(5)]
    length_list = [len(Matrix[i]) for i in range(5)]
    max_length = max(length_list)
    res = ''
    for i in range(max_length): # 각 col
        for row in range(5):
            if i < length_list[row]:
                res += Matrix[row][i]
    print(f'#{tc} {res}')

'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''