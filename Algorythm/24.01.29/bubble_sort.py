
def Bubble_Sort(lst, N) :
    for i in range(N-1, 0, -1) : # 끝에서부터 1까지 -1 단위로
        for j in range(0, i) : # 0부터 N-2 까지의 j
            if lst[j] > lst[j+1] : # j+1 = N-1까지 고정 가능
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst_1 = [55,7,78,12,42]
lst_2 = [7,99,76,8,20,7]
print(Bubble_Sort(lst_1, 5))
print(Bubble_Sort(lst_2, 6))

def Sort_Higher(lst, N) :
    for i in range(N) : # 0 ~ N까지의 숫자를 비교할 것이다.
        for j in range(i + 1, N) :  # 1 ~ N까지의 숫자를 비교할 것이다.
            if lst[i] > lst[j] : # 앞에 수가 크면, 바꿔준다. (큰 수를 뒤로 미룬다.)
                lst[i], lst[j] = lst[j], lst[i]
    return lst # 오름차순이 되는거

def Sort_Lower(lst, N) :
    for i in range(N) : # 0 ~ N까지의 숫자를 비교할 것이다.
        for j in range(i + 1, N) :  # 1 ~ N까지의 숫자를 비교할 것이다.
            if lst[i] < lst[j] : # 앞에 수가 작으면, 바꿔준다. (작은 수를 뒤로 미룬다.)
                lst[i], lst[j] = lst[j], lst[i]
    return lst # 내림차순이 되는거

print(Sort_Higher(lst_1, 5))
print(Sort_Lower(lst_1, 5))