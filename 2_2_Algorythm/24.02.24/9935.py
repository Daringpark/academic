

# import sys
# input = sys.stdin.readline
# from collections import deque

import sys
input = sys.stdin.readline

letter = input().rstrip()  # 개행 문자 제거
bomb = input().rstrip()    # 개행 문자 제거
result = []

for char in letter:
    result.append(char)
    
    # 패턴과 비교하여 일치할 경우 패턴 길이만큼 결과 리스트에서 제거
    if len(result) >= len(bomb) and ''.join(result[-len(bomb):]) == bomb:
        del result[-len(bomb):]

# 결과 출력
if result:
    print(''.join(result))
else:
    print('FRULA')

