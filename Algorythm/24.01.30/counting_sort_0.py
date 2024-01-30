Data = [1,4,5,6,7,8,5,6,1,2,0]
K = max(Data) + 1 # 9
N = len(Data) # 11

# cnt_list를 만들어 줌.(최대 값을 기준으로)
cnt_list = [0] * K
for number in Data:
    cnt_list[number] += 1
print(cnt_list)

# count stacking 강사님, 시간 복잡도 O(K), 새로운 
for idx in range(1, K):
    cnt_list[idx] = cnt_list[idx] + cnt_list[idx-1]
print(cnt_list)

