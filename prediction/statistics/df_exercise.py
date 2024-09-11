import numpy as np
import pandas as pd

# dataset maker define
total_count = 0
def generate_data(row_data, N, active_flag):
    global total_count

    result_data = []

    # 현재 성별별 총 인구 분포가 달라져여야 하는데, 적용되지 않음
    male_population = row_data[row_data['sex']==1]['percent'].sum()
    female_population = row_data[row_data['sex']==2]['percent'].sum()


    # 이중 For문을 돌면서 성별 분류별 데이터 생성
    for _, row in row_data.iterrows():
        age_group = row['age']
        sex_group = row['sex']

        if sex_group == 1:
            population_ratio = row['percent'] / male_population
        else:
            population_ratio = row['percent'] / female_population

        # 조건: 40대까지는 더 반영하고, 50대 이상은 덜 반영
        if age_group in ['40-49', '30-39', '20-29']:
            population_ratio *= 1.2  # 40대까지 가중치 추가
        elif age_group in ['50-59', '60-69', '70+']:
            population_ratio *= 0.7  # 50대 이상은 가중치 감소

        count_for_group = int(N * population_ratio + 0.5)

        total_count += count_for_group

        # 데이터 생성 라인
        for _ in range(count_for_group):
            if active_flag:
                # 운동을 잘하는 사람 데이터
                consumed_cal = 150 + np.random.normal(150, 9)
                intake_cal = np.random.choice([1500, 1800, 2400, 3000, 3300], p=[0.2, 0.25, 0.4, 0.1, 0.05])
            else:
                # 운동을 잘 안하는 사람 데이터
                consumed_cal = 70 + np.random.normal(20, 4)  # 운동량 적음
                intake_cal = np.random.choice([2000, 2300, 2700, 3200, 3500], p=[0.1, 0.2, 0.3, 0.3, 0.1])  # 섭취량 더 많음

            user_data = {
                'age': age_group,
                'sex': np.random.choice([1, 2]),
                'consumed_cal' : consumed_cal,
                'intake_cal': intake_cal,
                'BMI': 0,  # Placeholder for future calculation
                'fat': np.random.normal(18, 2),  # Fat percentage with some variation
                'muscle': np.random.normal(19, 2),  # Muscle percentage with some variation
                'BMR': 0  # Placeholder for future calculation
            }
            result_data.append(user_data)
    
    return pd.DataFrame(result_data)

file_path = './국민 건강 통계/exercise_total.csv'
data = pd.read_csv(file_path)
# n = 52000 => 약 20만명 데이터를 생성 :: 200,612명의 개인 생체정보 데이터
# n = 52000

# 샘플 데이터 생성
n = 100

# 데이터를 각각 출력하여 데이터 병합
active_result, inactive_result = generate_data(data, n, True), generate_data(data, n, False)
result = pd.concat([active_result, inactive_result])
result = result.sort_values(by=['age', 'sex'])

print(f'{total_count}개의 개인 DB가 만들어졌습니다!')

result.to_csv('output.csv', index=False)