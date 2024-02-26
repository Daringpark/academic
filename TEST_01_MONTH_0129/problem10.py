############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_position_safe(N, M, current):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    ## boundary 경계는 N+1이랑 -1
    pos = list(current) # tuple은 수정 불가 타입이니 list 형변환
    if M == 0 :
        pos[0] -= 1
    elif M == 1 :
        pos[0] += 1
    elif M == 2 :
        pos[1] -= 1
    elif M ==3 :
        pos[1] += 1
    
    if (0 <= pos[0] <= N and 0 <= pos[1] <= N) :
        return True
    else :
        return False
    # 특정 조건(바운더리 안)을 만족했을 때, True 

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False
#####################################################
