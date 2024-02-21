
# # 달팽이는 오르고 싶다 2869번 // 수식 만들기
# A, B, H = map(int, input().split())

# res = (H-A)//(A-B)

# if (H-A)%(A-B) == 0 :
#     print(res + 1)
# else :
#     print(res + 2)

# # 펠린드롬 확인, 속도 40ms
# word = input()
# back_word = word[::-1]

# if word == back_word :
#     print(1)
# else :
#     print(0)

# # 기하학 백준 3009번 : 네번째 점
# num_list = []
# for i in range(3) :
#     num_list.extend([input().split()])
# # print(num_list)
# x_list = []
# y_list = []
# for i in range(len(num_list)) :
#     x_list.append(num_list[i][0])
#     y_list.append(num_list[i][1])
# x_list.sort(); y_list.sort()
# x_list = list(map(int, x_list))
# y_list = list(map(int, y_list))

# if x_list.count(x_list[0]) == 1 :
#     X = x_list[0]
# else :
#     if x_list[1] == max(x_list) :
#         X = x_list[0]
#     X = x_list[2]

# if y_list.count(y_list[0]) == 1 :
#     Y = y_list[0]
# else :
#     if y_list[1] == max(y_list) :
#         Y = y_list[0]
#     Y = y_list[2]
# print(X, Y)
# # 40ms 속도

### 숏 코딩
# x, y = [], []
# for i in range(3):
#     a, b = map(int, input().split())
#     x.append(a)
#     y.append(b)
# print(min(x, key=x.count), min(y, key=y.count))
# # # 40ms, dictionary sort
