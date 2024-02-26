'''
3
6
A B C D E F
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
'''

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     deck = input().split()
#     new_deck = []
#     if N%2: # 홀수의 경우
#         stack1 = deck[:N//2+1] # 길이가 여기가 1 길음
#         stack2 = deck[N//2+1:]
#         for i in range(N//2):
#             new_deck.append(stack1[i])
#             new_deck.append(stack2[i])
#         new_deck.append(stack1[-1])
#     else: # 짝수의 경우
#         stack1 = deck[:N//2] # 길이가 같음
#         stack2 = deck[N//2:]
#         for i in range(N//2):
#             new_deck.append(stack1[i])
#             new_deck.append(stack2[i])
#     res = ' '.join(new_deck)
#     print(f'#{tc} {res}')

### 이건 Two-Pointer로 풀이하는게 더 쉽다!
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    deck = input().split()
    new_deck = []
    if N%2: # 홀수의 경우, 끝자리 하나가 필요로 하니까
        A = 0
        B = N//2 + 1
        res = ''
        for i in range(N//2):
            res += deck[A+i] + ' '
            res += deck[B+i] + ' '
        res += deck[N//2]
    else:
        A = 0
        B = N//2
        res = ''
        for i in range(N//2):
            res += deck[A+i] + ' '
            res += deck[B+i] + ' '
    print(f'#{tc} {res}')