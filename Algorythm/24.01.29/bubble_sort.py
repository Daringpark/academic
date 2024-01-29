
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

def Bubble_Sort_Higher(lst, N) :
    for i in range(N-1, 0, -1) : # 끝에서부터 1까지 -1 단위로
        for j in range(0, i) : # 0부터 N-2 까지의 j
            if lst[j] < lst[j+1] : # j+1 = N-1까지 고정 가능
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(Bubble_Sort_Higher(lst_1, 5))