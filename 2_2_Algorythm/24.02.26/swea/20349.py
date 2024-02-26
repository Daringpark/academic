
# 국민셔플
#
def shuffle(lst, t):
    new_deck = lst
    bottom_up = int(N * 0.37)
    result_deck = [0] * N
    for _ in range(t):
        if result_deck[0]:
            new_deck = result_deck
        new_deck = new_deck[-bottom_up:] + new_deck[:-bottom_up]
        if N%2: # 홀수라면 마지막 값을 고려해야함.
            A = 0
            B = N // 2 + 1
            for i in range(N//2):
                result_deck[2*i] = new_deck[A+i]
                result_deck[2*i+1] = new_deck[B+i]
            result_deck[-1] = (new_deck[N//2])
        else:
            A = 0
            B = N // 2
            for i in range(N//2):
                result_deck[2*i] = new_deck[A+i]
                result_deck[2*i+1] = new_deck[B+i]
    return result_deck
    # two-pointer 사용이 깔끔하지 않음 <<

Test_case = int(input())
for tc in range(1, Test_case+1):
    N , T = map(int, input().split())
    deck = list(range(1, N+1))
    res = ' '.join(map(str, shuffle(deck, T)))
    print(f'#{tc} {res}')