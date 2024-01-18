def dustforecast(dust) :
    if dust > 150 :
        print('매우 나쁨')
    elif dust > 80 :
        print('나쁨')
    elif dust > 30 :
        print('보통')
    elif dust < 0 : 
        print('0보다 작을 순 없습니다.')
    else :
        print('좋음')
    
print('오늘의 미세먼지 농도를 입력해주세요')
dust = int(input())

#이하 조건이 겹칠 경우, and 연산자를 사용하지 않아도 좋다.
dustforecast(dust)