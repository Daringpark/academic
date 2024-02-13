N = 4
arr = [1,2,3,4]
# result = 16개의 부분 집합
one_hot = [0]*N
def subset(k):
    if k == N:
        # print(one_hot)
        result = []
        for i in range(N):
            if one_hot[i]:
                result.append(arr[i])
        print(result)
        return

    for i in range(2):
        one_hot[k] = i
        subset(k+1)

subset(0)




N = 10
arr = [1,2,3,4,5,6,7,8,9,10]
# result = 16개의 부분 집합

one_hot = [0]*N
def subset(k, subsum):
    if subsum > 10:
        return

    if k == N: # depth까지 bottom-up
        if subsum == 10:
            print(result, subsum)
            return

    # width
    for i in range(2):
        one_hot[k] = i
        if i == 0:
            subset(k+1, subsum)
        else:
            subset(k+1, subsum + arr[k])

subset(0)