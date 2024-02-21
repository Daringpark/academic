
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

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

sum_book = 0
missing_book = []


for i in rental_book :
    sum_book += 1
    if (i in list_of_book) == False :
        sum_book -= 1
        print(f'{i} 을/를 보충하여야 합니다.')
        missing_book = [i for i in rental_book if (i in list_of_book) != True]
    elif sum_book == len(rental_book) :
        print(f'모든 도서가 대여 가능한 상태입니다.')
