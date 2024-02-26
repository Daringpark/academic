

# import sys
# input = sys.stdin.readline
# from collections import deque

import sys
input = sys.stdin.readline

letter = input().rstrip()  # 개행 문자 제거
bomb = input().rstrip()    # 개행 문자 제거
result = []

for char in letter: # letter list에 있는 char 한 글자를 계속 받아오면서 체크
    result.append(char)
    # 패턴과 비교하여 일치할 경우 패턴 길이만큼 결과 리스트에서 제거
    if len(result) >= len(bomb) and ''.join(result[-len(bomb):]) == bomb: # 길이가 같고, 그 뒤에 제거할 글씨만큼 뒤에 있는 것
        del result[-len(bomb):]

# 결과 출력
if result:
    print(''.join(result))
else:
    print('FRULA')

