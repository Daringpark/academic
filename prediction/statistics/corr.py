
import numpy as np
import pandas as pd

# csv를 불러와
csv_dir = './dummy/inputs/'
df_list = []

for csv_file in os.listdir(csv_dir):
    if csv_file.endswith('.csv'):
        df = pd.read_csv(os.path.join(csv_dir, csv_file))
        df_list.append(df)

df_combined = pd.concat(df_list, axis=0)



# print(df.head(6))
