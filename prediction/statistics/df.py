
import numpy as np
import pandas as pd

path_file = './2023_korean_health.csv'
row_data = pd.read_csv(path_file, encoding = "cp949", index_col='user_id')
print(row_data.columns)

data = row_data[:, ]




# print(df.head(6))
