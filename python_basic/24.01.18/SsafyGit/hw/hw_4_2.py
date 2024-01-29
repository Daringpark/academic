
sum_book = 0

list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '난중일기',
    '수성지',
    '백호집',
    '홍길동전',
    '만복자서포기',
]

for i in rental_list :
    # print(f'{i}')
    sum_book += 1
    if (i not in list_of_book) == True :
        print(f'{i} 은/는 보유하고 있지 않습니다.')
        break
    elif sum_book == len(rental_list) :
        print(f'모든 도서가 대여 가능한 상태입니다.')