############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def compare_pw(user):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    pass_length = 0
    for letter in user['password'] :
        pass_length += 1
    if 8 <= pass_length < 32 and user['password'] == user['password_confirm'] :
        return True
    else :
        return False
    # 패스워드의 길이만 확인 + 패스워드와 컨펌키가 같은지 확인

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'user_id': 'leessafy24',
    'password': 'q1w2e3r4',
    'password_confirm': 'q1w2e3r4',
    'email': 'goodjob24@mail.com',
}
print(compare_pw(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(compare_pw(user_data2))  # False
#####################################################
