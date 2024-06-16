### rasterio
# !pip install rasterio
import rasterio

### data loading
# !pip install numpy
import numpy as np
import pandas as pd

### learning
# !pip install tensorflow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from keras.models import Model
from tensorflow.keras.layers import Input, Activation, Conv2D, MaxPooling2D, concatenate, BatchNormalization, LSTM, UpSampling2D, Conv2DTranspose, Reshape, Dense, TimeDistributed
from keras.callbacks import EarlyStopping
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score

### visualization
from tensorflow.keras.utils import plot_model
from matplotlib import pylab
import matplotlib.pyplot as plt

### evaluation
import time
#from sklearn.metrics import precision_score, recall_score, confusion_matrix, Binarizer

## Pytorch loading configuration with cuda
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(torch.cuda.is_available())
## True = GPU, False = CPU

# Fire Spread Image Load # Gunwi
# min - max Scaler
def MinMaxScaler(map, row, col) :
  scaled = []

  for i in map :
    up = i - np.min(map)
    down = np.max(map) - np.min(map)
    scaled.append(up/down)

  scaled_map = np.concatenate(scaled[0:row]).reshape(row, col)
  return scaled_map

# Function to read TIF file and convert to NumPy array
def tif_to_array(file_path):
    with rasterio.open(file_path) as src:
        array = src.read()
        array = MinMaxScaler(array[0,...], array.shape[1], array.shape[2])
    return array



'''
Model Layer
kernels_size = 5
input_row = 300
input_col = 300
input_chan = 5
number_of_filters1 = 4
number_of_filters2 = 8
unit = 4
'''

kernels_size = 5
input_row = 300
input_col = 300
input_chan = 5
number_of_filters1 = 4
number_of_filters2 = 8
unit = 4

with tf.device('/device:GPU:0'):
  Input = Input(shape=(input_row, input_col, input_chan))
  ULSTM = Conv2D(filters=number_of_filters1, kernel_size=kernels_size, padding='same')(Input) # conv kernel ---> x1 --> x1*w1
  ULSTM = BatchNormalization()(ULSTM)
  ULSTM = Activation('relu')(ULSTM)
  ULSTM = MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same')(ULSTM)
  ULSTM = Conv2D(filters=number_of_filters2, kernel_size=kernels_size, padding='same')(ULSTM)
  ULSTM = BatchNormalization()(ULSTM)
  ULSTM = Activation('relu')(ULSTM)
  ULSTM = MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same')(ULSTM)
  ULSTM = Reshape(target_shape = (75*75, number_of_filters2))(ULSTM)
  ULSTM = LSTM(units=4, activation='tanh', return_sequences=True, input_shape=(None, 1444, 32))(ULSTM)
  ULSTM = TimeDistributed(Dense(1))(ULSTM)
  ULSTM = Reshape(target_shape = (75, 75, 1))(ULSTM)
  ULSTM = UpSampling2D(size=(2, 2))(ULSTM)
  ULSTM = Conv2DTranspose(filters=number_of_filters2, kernel_size=kernels_size, padding='same')(ULSTM)
  ULSTM = BatchNormalization()(ULSTM)
  ULSTM = Activation('relu')(ULSTM)
  ULSTM = UpSampling2D(size=(2, 2))(ULSTM)
  ULSTM = Conv2DTranspose(filters=number_of_filters1, kernel_size=kernels_size, padding='same')(ULSTM)
  ULSTM = BatchNormalization()(ULSTM)
  ULSTM = Activation('relu')(ULSTM)
  ULSTM = Conv2D(1, kernel_size=kernels_size, padding='same', activation = 'sigmoid')(ULSTM)
  Output = TimeDistributed(Dense(1))(ULSTM)

  ULSTM_Model = Model(inputs=Input, outputs = Output)
  ULSTM_Model.compile(loss='mse', optimizer='adam', metrics=['accuracy', 'mse'])

ULSTM_Model.summary()

# Model Train
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor = 'val_loss', min_delta = 0.01, patience = 30, mode = 'auto')

def train(t_x_list, t_y_list, epochs=200, Batchsize=32):
    start = time.time()

    for i in range(len(t_x_list)):
        hist = ULSTM_Model.fit(t_x_list[i], t_y_list[i], batch_size=Batchsize, epochs=epochs, validation_data=(val_x, val_y), callbacks = [early_stopping])

    end = time.time()
    how_long = end - start

    print(how_long // 3600, ' hours', (how_long % 3600) // 60, ' miniutes')

    # acc와 loss 그래프 그리기
    fig, ax = plt.subplots(2, 1)

    ax[0].plot(hist.history['accuracy'], label='train_acc')
    ax[0].plot(hist.history['val_accuracy'], label='val_acc')
    ax[0].set_ylabel('accuracy')
    ax[0].legend()

    ax[1].plot(hist.history['loss'], label='train_loss')
    ax[1].plot(hist.history['val_loss'], label='val_loss')
    ax[1].set_ylabel('loss')
    ax[1].legend()

    plt.show()

if __name__ == "__main__":
    # time step 3, 4, 5, 6
#    t_x_list = [train_x_25,train_x_26,train_x_27,train_x_28,train_x_29,train_x_30,train_x_31,train_x_32,train_x_33,train_x_34,train_x_35,train_x_36,train_x_37,train_x_38,train_x_39,train_x_40,train_x_41,train_x_42,train_x_43,train_x_44,train_x_46,train_x_47,train_x_48,train_x_49,train_x_50,train_x_51,train_x_52,train_x_53,train_x_54,train_x_55,train_x_56,train_x_57,train_x_58,train_x_59,train_x_60,train_x_61,train_x_62,train_x_63,train_x_64,train_x_65,train_x_66,train_x_67,train_x_68,train_x_69,train_x_70,train_x_71,train_x_72,train_x_73,train_x_74,train_x_75,train_x_76,train_x_77,train_x_78,train_x_79,train_x_80,train_x_81,train_x_82,train_x_83,train_x_84,train_x_85,train_x_86,train_x_87,train_x_88,train_x_89,train_x_90,train_x_91,train_x_92,train_x_93,train_x_94,train_x_95,train_x_96,train_x_97,train_x_98,train_x_99,train_x_100,train_x_101,train_x_102,train_x_103,train_x_104,train_x_105]
#    t_y_list = [train_y_25,train_y_26,train_y_27,train_y_28,train_y_29,train_y_30,train_y_31,train_y_32,train_y_33,train_y_34,train_y_35,train_y_36,train_y_37,train_y_38,train_y_39,train_y_40,train_y_41,train_y_42,train_y_43,train_y_44,train_y_46,train_y_47,train_y_48,train_y_49,train_y_50,train_y_51,train_y_52,train_y_53,train_y_54,train_y_55,train_y_56,train_y_57,train_y_58,train_y_59,train_y_60,train_y_61,train_y_62,train_y_63,train_y_64,train_y_65,train_y_66,train_y_67,train_y_68,train_y_69,train_y_70,train_y_71,train_y_72,train_y_73,train_y_74,train_y_75,train_y_76,train_y_77,train_y_78,train_y_79,train_y_80,train_y_81,train_y_82,train_y_83,train_y_84,train_y_85,train_y_86,train_y_87,train_y_88,train_y_89,train_y_90,train_y_91,train_y_92,train_y_93,train_y_94,train_y_95,train_y_96,train_y_97,train_y_98,train_y_99,train_y_100,train_y_101,train_y_102,train_y_103,train_y_104,train_y_105]

    # time step 1, 2, 3, 4, 5, 6  # validation data x
    t_x_list = [train_x_1,train_x_2,train_x_3,train_x_4,train_x_5,train_x_6,train_x_7,train_x_8,train_x_9,train_x_10,train_x_11,train_x_12,train_x_13,train_x_14,train_x_15,train_x_16,train_x_17,train_x_18,train_x_19,train_x_20,train_x_21,train_x_22,train_x_25,train_x_26,train_x_27,train_x_28,train_x_29,train_x_30,train_x_31,train_x_32,train_x_33,train_x_34,train_x_35,train_x_36,train_x_37,train_x_38,train_x_39,train_x_40,train_x_42,train_x_43,train_x_44,train_x_46,train_x_47,train_x_48,train_x_49,train_x_50,train_x_51,train_x_52,train_x_53,train_x_54,train_x_55,train_x_56,train_x_57,train_x_58,train_x_59,train_x_60,train_x_61,train_x_62,train_x_63,train_x_64,train_x_65,train_x_66,train_x_67,train_x_68,train_x_69,train_x_70,train_x_71,train_x_72,train_x_73,train_x_74,train_x_75,train_x_76,train_x_77,train_x_78,train_x_79,train_x_80,train_x_81,train_x_82,train_x_83,train_x_84,train_x_85,train_x_86,train_x_87,train_x_88,train_x_89,train_x_90,train_x_91,train_x_92,train_x_93,train_x_94,train_x_95,train_x_96,train_x_97,train_x_98,train_x_99,train_x_100,train_x_101,train_x_102,train_x_103,train_x_104,train_x_105,train_x_106,train_x_107,train_x_108,train_x_109,train_x_110,train_x_111,train_x_112,train_x_113,train_x_114,train_x_115,train_x_116,train_x_117,train_x_118,train_x_119,train_x_120,train_x_121,train_x_122,train_x_123,train_x_124,train_x_125,train_x_126,train_x_127,train_x_128,train_x_129,train_x_130,train_x_131,train_x_136,train_x_137,train_x_138,train_x_139,train_x_140,train_x_141,train_x_142,train_x_143,train_x_144,train_x_145,train_x_146,train_x_147,train_x_148,train_x_149,train_x_150,train_x_151,train_x_152,train_x_153,train_x_154,train_x_155,train_x_156,train_x_157,train_x_158,train_x_159]
    t_y_list = [train_y_1,train_y_2,train_y_3,train_y_4,train_y_5,train_y_6,train_y_7,train_y_8,train_y_9,train_y_10,train_y_11,train_y_12,train_y_13,train_y_14,train_y_15,train_y_16,train_y_17,train_y_18,train_y_19,train_y_20,train_y_21,train_y_22,train_y_25,train_y_26,train_y_27,train_y_28,train_y_29,train_y_30,train_y_31,train_y_32,train_y_33,train_y_34,train_y_35,train_y_36,train_y_37,train_y_38,train_y_39,train_y_40,train_y_42,train_y_43,train_y_44,train_y_46,train_y_47,train_y_48,train_y_49,train_y_50,train_y_51,train_y_52,train_y_53,train_y_54,train_y_55,train_y_56,train_y_57,train_y_58,train_y_59,train_y_60,train_y_61,train_y_62,train_y_63,train_y_64,train_y_65,train_y_66,train_y_67,train_y_68,train_y_69,train_y_70,train_y_71,train_y_72,train_y_73,train_y_74,train_y_75,train_y_76,train_y_77,train_y_78,train_y_79,train_y_80,train_y_81,train_y_82,train_y_83,train_y_84,train_y_85,train_y_86,train_y_87,train_y_88,train_y_89,train_y_90,train_y_91,train_y_92,train_y_93,train_y_94,train_y_95,train_y_96,train_y_97,train_y_98,train_y_99,train_y_100,train_y_101,train_y_102,train_y_103,train_y_104,train_y_105,train_y_106,train_y_107,train_y_108,train_y_109,train_y_110,train_y_111,train_y_112,train_y_113,train_y_114,train_y_115,train_y_116,train_y_117,train_y_118,train_y_119,train_y_120,train_y_121,train_y_122,train_y_123,train_y_124,train_y_125,train_y_126,train_y_127,train_y_128,train_y_129,train_y_130,train_y_131,train_y_136,train_y_137,train_y_138,train_y_139,train_y_140,train_y_141,train_y_142,train_y_143,train_y_144,train_y_145,train_y_146,train_y_147,train_y_148,train_y_149,train_y_150,train_y_151,train_y_152,train_y_153,train_y_154,train_y_155,train_y_156,train_y_157,train_y_158,train_y_159]

    train(t_x_list, t_y_list)











pred=ULSTM_Model(val_x)
real=val_y
#pred2=ULSTM_Model(test_x)
pred.shape, real.shape

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

pred = ULSTM_Model(val_x)
real = val_y
arr = pred
arr = sigmoid(arr)  # Apply sigmoid function to arr
condition = arr > 0.7

result = np.where(condition, arr, 0)
print(result)


tf.experimental.numpy.experimental_enable_numpy_behavior()

#numpy reshape
pred = result.reshape(4, -1)
real = real.reshape(4, -1)

# Confusion Matrix 계산을 위한 dytpe 변경
binary_pred = tf.cast(pred >= 0.5, dtype = tf.int32).numpy()
conf_matrix = confusion_matrix(real.flatten(), binary_pred.flatten())

# Accuracy 및 F1-score 계산
accuracy = accuracy_score(real.flatten(), binary_pred.flatten())
f1 = f1_score(real.flatten(), binary_pred.flatten())

# Confusion Matrix 시각화
plt.imshow(conf_matrix, cmap='Blues', interpolation='nearest')
plt.title('Confusion Matrix\nAccuracy: {:.2f}, F1-score: {:.2f}'.format(accuracy, f1))
# TP, FP, FN, TN 텍스트 추가
plt.text(0, 0, f'TP: {conf_matrix[1, 1]}', ha='center', va='center', fontsize=6, fontweight='bold', color='black')
plt.text(0, 1, f'FP: {conf_matrix[0, 1]}', ha='center', va='center', fontsize=6, fontweight='bold', color='black')
plt.text(1, 0, f'FN: {conf_matrix[1, 0]}', ha='center', va='center', fontsize=6, fontweight='bold', color='black')
plt.text(1, 1, f'TN: {conf_matrix[0, 0]}', ha='center', va='center', fontsize=6, fontweight='bold', color='black')

plt.colorbar()

plt.show()