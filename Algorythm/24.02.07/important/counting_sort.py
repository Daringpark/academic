arr = [1,2,3,4,5,4,5,4,5,1,3,67,100] # K = 100인 경우

counting_sort = [0] * (max(arr) + 1) # 해당 숫자까지의 인덱싱을 만들어주고

for num in arr: # count_list에 ++
    counting_sort[num] += 1

for i in range(1,len(counting_sort)): # 누적 합으로 계산
    counting_sort[i] += counting_sort[i-1]

result_list = [0]* len(arr) # arr의 길이 만큼
for num in arr:
    i = counting_sort[num]
    result_list[i -1] = num
    counting_sort[num] -= 1

print(result_list)