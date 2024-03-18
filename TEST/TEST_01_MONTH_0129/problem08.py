############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def find_solo(number_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    new_set = sorted(set(number_list))
    over_dict = {}
    for number in new_set : # initial dictionary setting
        over_dict[number] = 0
    for number in number_list : # For value 2 count
        over_dict[number] += 1
    
    for number in over_dict.keys() : # 출력 for문
        if over_dict[number] == 1 :
            return number
    # 앞선 문제와 같이 지금 생각나는건 set화 시켜서 리스트 업하는게 떠오름
    # 3가지 for문을 이용함 (시간 복잡도 ++)



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
number_list1 = [64, 27, 71, 27, 64]
print(find_solo(number_list1))  # 71
number_list2 = [4, 14, 60, 14, 49, 49, 78, 60, 78]
print(find_solo(number_list2))  # 4
#####################################################
