
# a = int(input())

# for i in range(a) :
#     print('*')

# b = int(input())

# for j in range(b) :
#     print('*' * (j+1))

# c = int(input())

# for k in range(0, c, 4) :
#     print()


# startnumber = 2
# sumV = 0

# for l in range(startnumber, 1001, 2) :
#     if l % 2 == 0 :
#         sumV += l
# print(sumV)

# numbers = [2,3,4,5,8,-18,-3,0,10,12,9,7]
# # for idx in range(len(numbers)):
# #     print("#%d %d" % (idx, numbers[idx]))

# pos = 0
# maxP = 0
# maxV = -1000
# for idx in range(len(numbers)) :
#     if  maxV < numbers[idx] :
#         maxV = numbers[idx]
#         maxP = idx
# print("#%d %d" % (maxP, maxV))

A = [1,2,3]
x = list(map(str, A))
print(A, x, type(A), type(x))
