############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def get_final_position(N, matrix, move_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    pos = []
    for i in range(N) : # 좌표 계산
        if 1 in matrix[i] :
            pos.append(i)
            pos.append(matrix[i].index(1))
    # 초기 position을 list로 계산, 저장해준다.
    
    # 초기 position을 받아서 move_list의 order에 맞게 움직이기 시작 
    for order in move_list :
        if order == 0 :
            pos[0] -= 1
        elif order == 1 :
            pos[0] += 1
        elif order == 2 :
            pos[1] -= 1
        elif order == 3 :
            pos[1] += 1
        # 바운더리를 벗어나게 된다면 바로 None값으로 처리
        if not (0 <= pos[0] <= N and 0 <= pos[1] <= N) :
            return None
    return pos # 끝까지 바운더리 내에 있었다면, 성공적으로 position 출력
# 2차원 list 풀이

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
N = 3
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
] 
moves1 = [1, 1, 3]
print(get_final_position(N, matrix, moves1)) # [2, 1]

moves2 = [1, 2, 3, 3]
print(get_final_position(N, matrix, moves2)) # None
#####################################################
