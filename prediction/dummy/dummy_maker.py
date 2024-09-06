import numpy as np
import pandas as pd

# Daily Dummy를 받는다고 가정...
# np.random.normal -> loc, scale, size => centre, standard deviation, size = (int, tuple, etc...)
data = {
    'date' : pd.date_range(start='2023-01-01', periods=545, freq='D'),
    'user_id': 1,
    'sex' : 1,
    'age' : 25,
    'weight' : np.random.normal(75, 1.41414, 545),
    'height' : 176,
    'BMI' : 0, # 초기 설정값
    'fat' : 18,
    'muscle' : 19,
    'consumed_cal' : np.random.normal(150, 9, 545),
    'intake_cal' : 2700
}
df = pd.DataFrame(data)
df['BMI'] = round(df['weight'] / ((df['height']/100) ** 2), 2)

print(df)
