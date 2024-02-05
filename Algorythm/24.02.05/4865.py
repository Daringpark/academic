import sys
sys.stdin = open('input_4865.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    letter_dict = {}

    str1 = set(map(str, input()))
    str2 = list(map(str, input()))

    for letter in str1: # 문자별 순회 할 때 O(K)
        for i in range(len(str2)):
            if letter == str2[i]:
                try : letter_dict[letter] += 1
                except KeyError : letter_dict[letter] = 1

    print(f'#{tc} {max(letter_dict.values())}')
