
Data = [1,4,5,6,7,8,5,6,1,2,0]
N = len(Data)
cnt_list = [0] * N

# sorting for reading
# for i in range(N) :
#     for j in range(i+1, N) :
#         if Data[i] > Data [j] :
#             Data[i], Data[j] = Data[j], Data[i]
# print(Data)

# counting
for number in Data:
    cnt_list[number] += 1
print(cnt_list)

# count stacking
new_cnt_list = [0] * len(cnt_list) # 새로운 리스트 변수에 넣어주고자 함. # 복잡도 증가 원인
new_cnt_list[0] = cnt_list[0]
for idx in range(1, len(new_cnt_list)):
    new_cnt_list[idx] += cnt_list[idx] + new_cnt_list[idx-1]
print(new_cnt_list)

temp = [0] * len(new_cnt_list)
# temp ????
for idx in (len(temp)-1, -1, -1):
    new_cnt_list[Data[idx]] -= 1
    temp[new_cnt_list[Data[idx]]] = Data[idx]
print(temp) # 0, 1, 1, 2, 4, 5, 5, 6, 6, 7, 8


## 시간 복잡도를 높인 경우, 조건문으로 인해서
if idx >= 1:
    new_cnt_list[idx] += cnt_list[idx] + new_cnt_list[idx-1]
else :
    new_cnt_list[idx] = cnt_list[idx]