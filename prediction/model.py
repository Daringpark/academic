# 패키지 불러오기
import os
import numpy as np
import pandas as pd
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, GRU, Dense 
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# csv를 불러와
csv_dir = './dummy/inputs/'
df_list = []

for csv_file in os.listdir(csv_dir):
    if csv_file.endswith('.csv'):
        df = pd.read_csv(os.path.join(csv_dir, csv_file))
        df_list.append(df)

df_combined = pd.concat(df_list, axis=0)

# 주요 features 설정
features = ['sex', 'age', 'BMI', 'weight', 'consumed_cal'] # 체중, 체중 연산 변경치 (기초 대사 + 활동 대사 > 섭취 칼로리 = 체중 증가)
# 성별, 나이, BMI, 체중, fat, muscle
df_features = df[features].values

# 타임스텝 설정, 앞선 타임스텝을 가지고, 90일까지의 예측을 진행할 예정...
timesteps = 7
forecast_steps = 90

# 시계열 데이터를 timesteps로 자르고, 다중 스텝 예측을 위해 여러 값을 y로 설정
def create_multi_step_sequences(data, time_steps, forecast_steps):
    X, y = [], []
    for i in range(len(data) - time_steps - forecast_steps):
        X.append(data[i:i + time_steps])
        y.append(data[i + time_steps:i + time_steps + forecast_steps, 0])  # 여기서는 weight(체중)를 예측

    return np.array(X), np.array(y)

# 입력 데이터(X)와 출력 데이터(y) 생성
X, y = create_multi_step_sequences(df_features, timesteps, forecast_steps)

# X의 shape: (샘플 수, timesteps, features), y의 shape: (샘플 수, forecast_steps)
print("X shape:", X.shape)  # 예: (455, 7, 2)
print("y shape:", y.shape)  # 예: (455, 90)

# 모델 순차 정의
model = Sequential() # 모델 순차적 정의
model.add(Input(shape=(X.shape[1], X.shape[2])))
# GRU 레이어를 어느정도를 쓸건가?
model.add(GRU(units=128, return_sequences=False)) # 모델 GRU 레이어 통과
model.add(Dense(units=forecast_steps)) # 모델 Dense 레이어 통과 이후, 1차원으로 90개 출력 데이터

# 모델 컴파일 - GPT : 회귀 모델은 Mean Sqaure??
model.compile(optimizer='adam', loss='mse')

# checkpoint = restore best model
checkpoint = ModelCheckpoint("./models/modelv1.weights.h5", monitor='val_loss', save_best_only=True, verbose=1, save_weights_only=True)

# EarlyStopping 콜백 설정: 10번 연속 성능이 개선되지 않으면 학습 중지
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# 모델 학습 | 7 : 3 (user 12000; 8400: 3600)
history = model.fit(X, y, epochs=500, batch_size=32, validation_split=0.3, callbacks=[early_stopping, checkpoint])

# 학습 결과 출력
print("모델 학습 완료!")

# val_loss와 train_loss 시각화
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.title('Train and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')

# x축과 y축의 범위를 조정하여 변화를 더 자세히 관찰
plt.xlim([0, 50])  # 예: 처음 50 에포크에 초점을 맞추기 위해 x축 제한
plt.ylim([0, 0.1])  # y축의 값을 0과 0.1 사이로 제한하여 작은 변화에 집중

plt.legend()
plt.show()


