
numbers = list(map(int, input().split()))
a_cnt = 0
d_cnt = 0
for i in range(7):
    if numbers[i] == numbers[i+1]-1:
        a_cnt += 1
    elif numbers[i] == numbers[i+1]+1:
        d_cnt += 1
    else:
        print('mixed')
        break
if a_cnt == 7:
    print('ascending')
elif d_cnt == 7:
    print('descending')
