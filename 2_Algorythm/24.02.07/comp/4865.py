T = int(input())

for tc in range(1, T+1):
    letter = set(input())
    original = list(input())
    cnt_dict = {}
    for l in letter:
        cnt_dict.setdefault(l, 0)
    for l in original:
        try:cnt_dict[l] += 1
        except: pass
    print(f'#{tc} {max(cnt_dict.values())}')