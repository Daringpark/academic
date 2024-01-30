Data = [1,4,5,6,7,8,5,6,1,2,0]
K = max(Data) + 1 # 9
N = len(Data) # 11

## 나의 풀이

# sorting for reading
# for i in range(N) :
#     for j in range(i+1, N) :
#         if Data[i] > Data [j] :
#             Data[i], Data[j] = Data[j], Data[i]
# print(Data)

# counting
cnt_list = [0] * N
for number in Data:
    cnt_list[number] += 1
print(cnt_list)

# count stacking의 시간 복잡도 O(n)
new_cnt_list = [0] * len(cnt_list) # 새로운 리스트 변수에 넣어주고자 함.
new_cnt_list[0] = cnt_list[0]
for idx in range(1, len(new_cnt_list)):
    new_cnt_list[idx] += cnt_list[idx] + new_cnt_list[idx-1]
print(new_cnt_list)

## count stacking의 시간 복잡도는 동일하게 진행 O(n*1)
new_cnt_list = [0] * len(cnt_list) # 새로운 리스트 변수에 넣어주고자 함.
for idx in range(len(new_cnt_list)):
    if idx >= 1:
        new_cnt_list[idx] += cnt_list[idx] + new_cnt_list[idx-1]
    else :
        new_cnt_list[idx] = cnt_list[idx]
print(new_cnt_list)

# temp 안전 정렬의 경우
temp = [0] * len(new_cnt_list)
for idx in range(len(temp)-1, -1, -1): # range를 사용안하고, 튜플로 저장하였었음;;
    new_cnt_list[Data[idx]] -= 1 # counting amount -1한 위치가 마지막 위치
    temp[new_cnt_list[Data[idx]]] = Data[idx]
    # print(temp) # [1,4,5,6,7,8,5,6,1,2,0] 뒤에서부터 (0,2,1,6,5,8,7,6,5,4,1 순으로)
print(temp) # 0, 1, 1, 2, 4, 5, 5, 6, 6, 7, 8
