
'''
3
1
10
100
'''



T = int(input())
for tc in range(1, T+1):
    radius = int(input())
    cnt = 0
    for x in range(-radius, radius+1):
        for y in range(-radius, radius + 1):
            if x ** 2 + y ** 2 <= radius ** 2:
                cnt += 1
    print(f'#{tc} {cnt}')