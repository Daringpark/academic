
# # f-string 이해하기
# print(f'다음은 이형기 시인의 \"낙화\"의 한 구절이다.\n- 1연\n	가야할 때 언제인가를\n	분명히 알고 가는 이의\n	뒷모습은 얼마나 아름다운가.\n\n나는 이 시를 보며 \'나는 내가 가야할 때가 언제일까?\' 를 생각해 보았다.')

# # type 변환 (명시적 형변환)
# book = '1'
# total = 10
# guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
# book = int(book)
# print(guide)
# print(book * total)

# changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
# rental = 3.0
# rental = int(rental)
# print(changes)
# print(total - rental)

# # type 변환 (중복제거, 명시적 형변환)
# list_A = ['사과', '배', '사과', '포도', '감', '수박', '사과', '포도']
# print(list_A)

# list_A = set(list_A) #set()형변환을 이용하여, 중복된 값을 제거해준다. set()은 집합 변수
# print(list_A, type(list_A))

# list_A = list(list_A) #set()으로 되어있는 list()형변환을 이용하여 다시 list 형태로 바꿔준다.
# print(list_A, type(list_A))

# # 리스트 활용하기

# zero_list = [0]
# print(zero_list)
# many_zero_list = [0]*250000
# print(len(many_zero_list))
# numbers = list(range(1,11))
# print(numbers)
# print(numbers[3:])

# # 숫자형 변수 = 0이 아닌 숫자에는 n(True)으로 본다.
# # 문자형 변수 = ''(공백)이 아니면, 문자가 있다고(True)로 본다.
# # 리스트형 변수 = []는 0이고, 차있는 리스트는 True로 본다.

# # f-string 활용; 책 한 권당 print문을 한 번씩만 사용한다. 
# author_1 = '권필'
# author_2 = '허균'
# book_1 = '주생전'
# book_2 = '홍길동전'

# print(f'{book_1}의 작가는 {author_1}이고,\n{author_2}은 {book_2}를 집필하였다.')

# # dictionary append하는 방식

# t = {'a' : 5, 'b' : 12, 'c' : 20}

# print('몇 개의 실험군을 추가하실 껀가요?')
# n = int(input())

# for j in range(n) :
#     print('a, b, c 중에서 하나를 골라, count를 늘려주세요.')
#     i = str(input())
#     if i == 'a' :
#         t['a'] += 1
#     elif i == 'b' :
#         t['b'] += 1
#     elif i == 'c' :
#         t['c'] += 1
#     else : 
#         print('다른 형태의 실험군입니다. count를 건너뜁니다.')
#     print(t)

# # slicing을 이용하여, 문자열 만들기; 새로운 변수 저장
    
# alpha = 'good'
# beta = 'se'
# ans = alpha[:3] + beta

# print(ans)
# title = '딕셔너리 활용하기'
# # 아래에 코드를 작성하시오.
# data = {'과목' : 'Python', '구분' : '실습', '단계' : 2, '문제번호' : 3251, '이름' : None, '일차' : 22}
# print(data)
# data['단계'] = str(data['단계'])+'단계'
# data['이름'] = title
# data['일차'] = data['일차']-20
# print(data)




# books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
# authors = ['작자 미상', '허균', '박지원', '이항복', '임제']


# print(f'{authors[1]} : {books[-2]}\n{authors[-2]} : {books[1]}\n{authors[0]} : {books[2]}\n{authors[2]} : {books[0]}\n{authors[-1]} : {books[-1]}')

# data = [{'has_more': False,
#   'next_cursor': None,
#   'object': 'list',
#   'page_or_database': {},
#   'request_id': 'a5163fff-758f-45ea-b6fb',
#   'results': [{'archived': False,
#                'cover': None,
#                'created_by': {'object': 'user'},
#                'created_time': '2023-06-15T04:29:00.000Z',
#                'icon': None,
#                'last_edited_by': {'object': 'user'},
#                'last_edited_time': '2023-12-12T09:19:00.000Z',
#                'object': 'page',
#                'parent': {'type': 'database_id'},
#                'properties': {'setNum': {'id': '%7DK%40%5C',
#                                          'number': 1,
#                                          'type': 'number'},
#                               '과목': {'id': 'YuIE',
#                                      'multi_select': [{'color': 'default',
#                                                        'name': 'Python'}],
#                                      'type': 'multi_select'},
#                               '구분': {'id': '%40%3EmR',
#                                      'select': {'color': 'purple',
#                                                 'name': '실습'},
#                                      'type': 'select'},
#                               '단계': {'id': 'T%7B%7BP',
#                                      'select': {'color': 'default',
#                                                 'name': '3'},
#                                      'type': 'select'},
#                               '문제번호': {'id': 'uEBt',
#                                        'number': 1431,
#                                        'type': 'number'},
#                               '제목': {'id': 'title',
#                                      'title': [{'annotations': {'bold': False,
#                                                                 'code': False,
#                                                                 'color': 'default',
#                                                                 'italic': False,
#                                                                 'strikethrough': False,
#                                                                 'underline': False},
#                                                 'href': None,
#                                                 'plain_text': '복잡한 자료구조',
#                                                 'text': {'content': '복잡한 자료구조',
#                                                          'link': None},
#                                                 'type': 'text'}],
#                                      'type': 'title'},
#                               '일차': {'id': 'nWnH',
#                                      'number': '2',
#                                      'type': 'number'},
#                               '커리큘럼': {'id': 'T%3AR_',
#                                        'multi_select': [{'color': 'default',
#                                                          'name': 'fundamentals-of-python'}],
#                                        'type': 'multi_select'}},
#                'public_url': None
#             }],
#   'type': 'page_or_database'}]

# # 아래에 코드를 작성하시오.

# first_data = dict()

# first_data['제목'] = data[0]['results'][0]['properties']['제목']['title'][0]['plain_text']
# first_data['일차'] = int(data[0]['results'][0]['properties']['일차']['number'])
# first_data['단계'] = data[0]['results'][0]['properties']['단계']['select']['name'] +'단계'
# first_data['과목'] = data[0]['results'][0]['properties']['과목']['multi_select'][0]['name']

# print(first_data)

# information = dict()
# authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
# books = [
#     ['장화홍련전', '가락국 신화', '온달 설화'],
#     ['금오신화', '이생규장전', '만복자서포기'],
#     ['수성지', '백호집', '원생몽유록'],
#     ['홍길동전', '장생전', '도문대작'],
#     ['옥루몽', '옥련몽'],
# ]

# information[authors[0]] = books[1]
# information[authors[1]] = books[-2]
# information[authors[2]] = books[-1]
# information[authors[3]] = books[0]
# information[authors[-2]] = books[2]

# print(information)

''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''
catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

#backup_catalog = [x[:] for x in catalog] #깊은 복사
# backup_catalog = catalog[:] #얕은 복사
# catalog[3] = ['성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀']

backup_catalog = catalog[:]
backup_catalog[3] = tuple(catalog[3])
catalog[3][0] = '성공을 향한 한 걸음'
catalog[3][1] = '내 삶의 변화'
catalog[3][2] = '목표 달성의 비밀'
backup_catalog[3] = list(backup_catalog[3])

print('catalog와 backup_catalog를 비교한 결과')
# 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오.
print(backup_catalog == catalog)

print('backup_catalog : ')
print(backup_catalog)
print()

print('catalog : ')
print(catalog)

