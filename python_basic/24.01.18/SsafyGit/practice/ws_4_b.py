

food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

for i in range(len(food_list)) :
    if food_list[i]['이름'] != '토마토' and food_list[i]['이름'] != '자장면' :
        food_name = food_list[i]['이름']
        food_class = food_list[i]['종류']
        print(f'{food_name} 은/는 {food_class} (이)다.')
    elif food_list[i]['이름'] == '토마토' :
        food_list[i]['종류'] = '과일'
        food_name = food_list[i]['이름']
        food_class = food_list[i]['종류']   
        print(f'{food_name} 은/는 {food_class} (이)다.')
    else : 
        food_name = food_list[i]['이름']
        food_class = food_list[i]['종류']
        print(f'{food_name}엔 고추가루지')
        print(f'{food_name} 은/는 {food_class} (이)다.')

print(food_list)


