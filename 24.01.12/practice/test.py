# print('Hello Python')
# ################################################
# print((11+12+13)/3)
# print((12+13+14)/3)
# print((13+14+15)/3)
# ################################################
# #위 결과와 비슷하게 만들고 싶습니다.
# #추가적으로 값에 따라서 다른 물고기 종류가 나오게 설정하였습니다.
# ###연산 규칙 반복하기 (하)
# a = 11
# for i in range(3) :
#     A = []
#     A.append(a)
#     A.append(a+1)
#     A.append(a+2)
#     a +=1
#     ans = sum(A) // 3
#     if ans == 12 :
#         print("JELLYFISH")
#     elif ans == 14 :
#         print("TROUT")
#     else :
#         print("GOLDFISH", ans)
# ################################################
# ###관계 연산자 이해하기
# dust = 100 > 200 and 200 >= 100 #F and T = F
# print(dust)

# con = 100 > 200 or 200 >= 100 #F or T = T
# print(con)


# ###################################################
# ###리스트 내부에서 특정 조건의 순서 숫자를 뽑아내기
# dust = [58, 48, 64, 55, 78, 74, 69, 36]
# n = len(dust)

# for i in range(n) :
#     if i % 2 == 0 :
#         print(dust[i])
# #range(init_order, end_order, step)
# ###################################################
# ###딕셔너리 이해하기
# dust = {'A' : 32, 'B' : 24, 'C' : 27, 'D' : 3}
# print(dust['A'])

# print(dust.get('A')) #

# dust['A'] = dust['A'] + 20 #딕셔너리 키값에 바로 저장하는 것
# print(dust['A'])

# print(dust['A'] + 20) #그냥 값을 더해주는 것을 print
# print(dust)
# ##################################################
# ##입력값을 받아서 두 수를 비교하는 프로그램을 만들어보자.
# print("이건 입력하신 두 자연수의 크기를 판단하는 프로그램입니다.")
# print("100이하의 두 자연수를 기입해주세요.")
# input1, input2 = map(int, input().split())

# if (input1 and input2) >= 0 and (input1 and input2) <= 100 :
#     if input1 > input2 :
#         print("앞의 수가 더 큽니다.")
#     elif input1 < input2 :
#         print("뒤의 수가 더 큽니다.")
#     else : 
#         print("두 수는 같은 수입니다.")
# else :
#     print("수를 잘못 기입하셨습니다.")
# ##################################################
# ##입력값을 받아서 숫자를 늘려주는 반복문을 돌려보자.
# number = int(input())

# while number < 25 :
#     number += 1
#     print(number)
# ##################################################
# ##리스트에 있는 값을 while문을 통해서 출력해보자.
# lst = [3,5,5,4,8,6]
# i = 0
# while i < len(lst) :
#     print("#%d %d" %(i, lst[i]))
#     i += 1 
# ##################################################
# ##위에서 진행했던 반복문 돌리기도 while문을 통해서 돌릴 수 있어요.
# a = 11
# while a < 16 :
#     A = []
#     A.append(a)
#     A.append(a+1)
#     A.append(a+2)
#     a +=1
#     ans = sum(A) // 3
#     if ans <= 12 :
#         print("GOLDFISH", ans)
#     elif ans < 15 :
#         print("JELLYFISH", ans)
#     else :
#         print('TROUT', ans)
# ##################################################

# lst = [4, 5, 6, 8, -5, -7, 3]
# idx = 0

# while lst[idx] > 0 :
#     print("#%d %d" %(idx, lst[idx]))
#     idx += 1
# print("#stop before# #%d %d" %(idx, lst[idx+ 1]))

###################################################

numbers = [1,4,2,7,6,8]










###################################################
# numbers 리스트 내에 있는 최대값, 최소값과 위치를 출력하기
# numbers = [-15,8,9,10,-43,61,45,12]
# maxV = 0
# maxP = 0
# pos = 0

# for number in numbers :
#     if maxV <= number:
#         maxV = number
#         maxP = pos
#     pos = pos + 1

# print('최대값은', maxV, '위치는', maxP,'입니다.')

# minV = 10000
# minP = 0
# pos = 0

# for number in numbers :
#     if minV >= number :
#         minV = number
#         minP = pos
#     pos = pos + 1
# print('최소값은', minV, '위치는', minP,'입니다.')


###################################################
numbers = [48, 49, 50, 51, 52]
n = len(numbers)

result = 0

for i in  range(n) :
    result = result + numbers[i]
print('모든 원소의 총 합은',result,'입니다.')


###################################################
result_even = 0
result_odd = 0

for i in range(n) :
    if i % 2 != 1 :
        result_even = result_even + numbers[i]
    else :
        result_odd = result_odd + numbers[i]
print('리스트 내 짝수의 총 합은',result_even,'입니다.')
print('리스트 내 짝수의 총 합은',result_odd,'입니다.')