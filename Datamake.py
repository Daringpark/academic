### rasterio
# !pip install rasterio
import rasterio

import numpy as np
import pandas as pd

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

# 시간별로 path 설정 # 마지막 화선은 DF에 없음 # slope, aspect 없는 ver
file_path = pd.DataFrame({"t0" : ["US_0304_1100.tif", "US_wd_t0.tif", "US_ws_t0.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t1" : ["US_0304_1410.tif", "US_wd_t1.tif", "US_ws_t1.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t2" : ["US_0304_2130.tif", "US_wd_t2.tif", "US_ws_t2.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t3" : ["US_0305_0540.tif", "US_wd_t3.tif", "US_ws_t3.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t4" : ["US_0305_1500.tif", "US_wd_t5.tif", "US_ws_t5.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t5" : ["US_0306_0700.tif", "US_wd_t6.tif", "US_ws_t6.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t6" : ["US_0306_1100.tif", "US_wd_t7.tif", "US_ws_t7.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t7" : ["US_0306_1700.tif", "US_wd_t8.tif", "US_ws_t8.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t8" : ["US_0307_0900.tif", "US_wd_t9.tif", "US_ws_t9.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t9" : ["US_0307_1300.tif", "US_wd_t10.tif", "US_ws_t10.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t10" : ["US_0307_1600.tif", "US_wd_t11.tif", "US_ws_t11.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t11" : ["US_0308_0800.tif", "US_wd_t12.tif", "US_ws_t12.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t12" : ["US_0308_1700.tif", "US_wd_t13.tif", "US_ws_t13.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t13" : ["US_0309_0900.tif", "US_wd_t14.tif", "US_ws_t14.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t14" : ["US_0309_1700.tif","US_wd_t15.tif", "US_ws_t15.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t15" : ["US_0311_0900.tif", "US_wd_t15.tif", "US_ws_t15.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t16" : ["US_0311_1700.tif", "US_wd_t16.tif", "US_ws_t16.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t17" : ["US_0312_0900.tif", "US_wd_t17.tif", "US_ws_t17.tif", "US_DEM.tif", "US_NDVI.tif"],
                          "t18" : ["US_0312_1700.tif", "US_wd_t18.tif", "US_ws_t18.tif", "US_DEM.tif", "US_NDVI.tif"]})

file_path

# Iterate through each column in the DataFrame and read TIF files
# Assuming your DataFrame is named file_path
data_arrays = {}

for col in file_path.columns:
    time_step_arrays = []

    for file_name in file_path[col]:
        file_path_full = "/content/drive/MyDrive/23-2_Capstone_team1/data/US/" + file_name  # Replace with your actual directory path
        array = tif_to_array(file_path_full)
        time_step_arrays.append(array)

    # Stack arrays along the fourth axis
    stacked_arrays = np.stack(time_step_arrays, axis=2)

    # Store the stacked arrays in a dictionary
    data_arrays[col] = stacked_arrays

# Access the arrays for a specific time step, for example, t0
t0_arrays_us = data_arrays["t0"]
t1_arrays_us = data_arrays["t1"]
t2_arrays_us = data_arrays["t2"]
t3_arrays_us = data_arrays["t3"]
t4_arrays_us = data_arrays["t4"]
t5_arrays_us = data_arrays["t5"]
t6_arrays_us = data_arrays["t6"]
t7_arrays_us = data_arrays["t7"]
t8_arrays_us = data_arrays["t8"]
t9_arrays_us = data_arrays["t9"]
t10_arrays_us = data_arrays["t10"]
t11_arrays_us = data_arrays["t11"]
t12_arrays_us = data_arrays["t12"]
t13_arrays_us = data_arrays["t13"]
t14_arrays_us = data_arrays["t14"]
t15_arrays_us = data_arrays["t15"]
t16_arrays_us = data_arrays["t16"]
t17_arrays_us = data_arrays["t17"]
t18_arrays_us = data_arrays["t18"]

US_t1_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0304_1410.tif")
US_t1_fire = US_t1_fire.read()[0,...]
US_t1_fire = MinMaxScaler(US_t1_fire, US_t1_fire.shape[0], US_t1_fire.shape[1])

US_t2_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0304_2130.tif")
US_t2_fire = US_t2_fire.read()[0,...]
US_t2_fire = MinMaxScaler(US_t2_fire, US_t2_fire.shape[0], US_t2_fire.shape[1])

US_t3_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0305_0540.tif")
US_t3_fire = US_t3_fire.read()[0,...]
US_t3_fire = MinMaxScaler(US_t3_fire, US_t3_fire.shape[0], US_t3_fire.shape[1])

US_t4_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0305_1500.tif")
US_t4_fire = US_t4_fire.read()[0,...]
US_t4_fire = MinMaxScaler(US_t4_fire, US_t4_fire.shape[0], US_t4_fire.shape[1])

US_t5_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0306_0700.tif")
US_t5_fire = US_t5_fire.read()[0,...]
US_t5_fire = MinMaxScaler(US_t5_fire, US_t5_fire.shape[0], US_t5_fire.shape[1])

US_t6_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0306_1100.tif")
US_t6_fire = US_t6_fire.read()[0,...]
US_t6_fire = MinMaxScaler(US_t6_fire, US_t6_fire.shape[0], US_t6_fire.shape[1])

US_t7_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0306_1700.tif")
US_t7_fire = US_t7_fire.read()[0,...]
US_t7_fire = MinMaxScaler(US_t7_fire, US_t7_fire.shape[0], US_t7_fire.shape[1])

US_t8_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0307_0900.tif")
US_t8_fire = US_t8_fire.read()[0,...]
US_t8_fire = MinMaxScaler(US_t8_fire, US_t8_fire.shape[0], US_t8_fire.shape[1])

US_t9_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0307_1300.tif")
US_t9_fire = US_t9_fire.read()[0,...]
US_t9_fire = MinMaxScaler(US_t9_fire, US_t9_fire.shape[0], US_t9_fire.shape[1])

US_t10_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0307_1600.tif")
US_t10_fire = US_t10_fire.read()[0,...]
US_t10_fire = MinMaxScaler(US_t10_fire, US_t10_fire.shape[0], US_t10_fire.shape[1])

US_t11_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0308_0800.tif")
US_t11_fire = US_t11_fire.read()[0,...]
US_t11_fire = MinMaxScaler(US_t11_fire, US_t11_fire.shape[0], US_t11_fire.shape[1])

US_t12_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0308_1700.tif")
US_t12_fire = US_t12_fire.read()[0,...]
US_t12_fire = MinMaxScaler(US_t12_fire, US_t12_fire.shape[0], US_t12_fire.shape[1])

US_t13_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0309_0900.tif")
US_t13_fire = US_t13_fire.read()[0,...]
US_t13_fire = MinMaxScaler(US_t13_fire, US_t13_fire.shape[0], US_t13_fire.shape[1])

US_t14_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0309_1700.tif")
US_t14_fire = US_t14_fire.read()[0,...]
US_t14_fire = MinMaxScaler(US_t14_fire, US_t14_fire.shape[0], US_t14_fire.shape[1])

US_t15_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0311_0900.tif")
US_t15_fire = US_t15_fire.read()[0,...]
US_t15_fire = MinMaxScaler(US_t15_fire, US_t15_fire.shape[0], US_t15_fire.shape[1])

US_t16_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0311_1700.tif")
US_t16_fire = US_t16_fire.read()[0,...]
US_t16_fire = MinMaxScaler(US_t16_fire, US_t16_fire.shape[0], US_t16_fire.shape[1])

US_t17_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0312_0900.tif")
US_t17_fire = US_t17_fire.read()[0,...]
US_t17_fire = MinMaxScaler(US_t17_fire, US_t17_fire.shape[0], US_t17_fire.shape[1])

US_t18_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0312_1700.tif")
US_t18_fire = US_t18_fire.read()[0,...]
US_t18_fire = MinMaxScaler(US_t18_fire, US_t18_fire.shape[0], US_t18_fire.shape[1])

US_t19_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/US/US_0313_0900.tif")
US_t19_fire = US_t19_fire.read()[0,...]
US_t19_fire = MinMaxScaler(US_t19_fire, US_t19_fire.shape[0], US_t19_fire.shape[1])

train_x_us = np.stack((t0_arrays_us, t1_arrays_us, t2_arrays_us, t3_arrays_us, t4_arrays_us, t5_arrays_us, t6_arrays_us, t7_arrays_us, t8_arrays_us, t9_arrays_us, t10_arrays_us, t11_arrays_us, t12_arrays_us, t13_arrays_us, t14_arrays_us, t15_arrays_us, t16_arrays_us, t17_arrays_us, t18_arrays_us), axis=0)
train_y_us = np.stack((US_t1_fire, US_t2_fire, US_t3_fire, US_t4_fire, US_t5_fire, US_t6_fire, US_t7_fire, US_t8_fire, US_t9_fire, US_t10_fire, US_t11_fire, US_t12_fire, US_t13_fire, US_t14_fire, US_t15_fire, US_t16_fire, US_t17_fire, US_t18_fire, US_t19_fire), axis=0)

# 밀양 산불 데이터
# 시간별로 path 설정 # 마지막 화선은 DF에 없음  # slope, aspect 없는 ver
file_path = pd.DataFrame({"t0" : ["MY_0531_1000.tif", "MY_wd_t0.tif", "MY_ws_t0.tif", "MY_DEM.tif", "MY_NDVI.tif"],
                          "t1" : ["MY_0531_1430.tif", "MY_wd_t1.tif", "MY_ws_t1.tif", "MY_DEM.tif", "MY_NDVI.tif"],
                          "t2" : ["MY_0601_0730.tif", "MY_wd_t2.tif", "MY_ws_t2.tif", "MY_DEM.tif", "MY_NDVI.tif"],
                          "t3" : ["MY_0601_1400.tif", "MY_wd_t3.tif", "MY_ws_t3.tif", "MY_DEM.tif", "MY_NDVI.tif"],
                          "t4" : ["MY_0601_1700.tif", "MY_wd_t4.tif", "MY_ws_t4.tif", "MY_DEM.tif", "MY_NDVI.tif"],
                          "t5" : ["MY_0601_2000.tif", "MY_wd_t5.tif", "MY_ws_t5.tif", "MY_DEM.tif", "MY_NDVI.tif"],
                          "t6" : ["MY_0602_1100.tif", "MY_wd_t6.tif", "MY_ws_t6.tif", "MY_DEM.tif", "MY_NDVI.tif"]})

file_path

# Iterate through each column in the DataFrame and read TIF files
# Assuming your DataFrame is named file_path
data_arrays = {}

for col in file_path.columns:
    time_step_arrays = []

    for file_name in file_path[col]:
        file_path_full = "/content/drive/MyDrive/23-2_Capstone_team1/data/MY/" + file_name  # Replace with your actual directory path
        array = tif_to_array(file_path_full)
        time_step_arrays.append(array)

    # Stack arrays along the fourth axis
    stacked_arrays = np.stack(time_step_arrays, axis=2)

    # Store the stacked arrays in a dictionary
    data_arrays[col] = stacked_arrays

# Access the arrays for a specific time step, for example, t0
t0_arrays_my = data_arrays["t0"]
t1_arrays_my = data_arrays["t1"]
t2_arrays_my = data_arrays["t2"]
t3_arrays_my = data_arrays["t3"]
t4_arrays_my = data_arrays["t4"]
t5_arrays_my = data_arrays["t5"]
t6_arrays_my = data_arrays["t6"]

MY_t1_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/MY/MY_0531_1430.tif")
MY_t1_fire = MY_t1_fire.read()[0,...]
MY_t1_fire = MinMaxScaler(MY_t1_fire, MY_t1_fire.shape[0], MY_t1_fire.shape[1])
MY_t2_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/MY/MY_0601_0730.tif")
MY_t2_fire = MY_t2_fire.read()[0,...]
MY_t2_fire = MinMaxScaler(MY_t2_fire, MY_t2_fire.shape[0], MY_t2_fire.shape[1])
MY_t3_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/MY/MY_0601_1400.tif")
MY_t3_fire = MY_t3_fire.read()[0,...]
MY_t3_fire = MinMaxScaler(MY_t3_fire, MY_t3_fire.shape[0], MY_t3_fire.shape[1])
MY_t4_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/MY/MY_0601_1700.tif")
MY_t4_fire = MY_t4_fire.read()[0,...]
MY_t4_fire = MinMaxScaler(MY_t4_fire, MY_t4_fire.shape[0], MY_t4_fire.shape[1])
MY_t5_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/MY/MY_0601_2000.tif")
MY_t5_fire = MY_t5_fire.read()[0,...]
MY_t5_fire = MinMaxScaler(MY_t5_fire, MY_t5_fire.shape[0], MY_t5_fire.shape[1])
MY_t6_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/MY/MY_0602_1100.tif")
MY_t6_fire = MY_t6_fire.read()[0,...]
MY_t6_fire = MinMaxScaler(MY_t6_fire, MY_t6_fire.shape[0], MY_t6_fire.shape[1])
MY_t7_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/MY/MY_0602_1700.tif")
MY_t7_fire = MY_t7_fire.read()[0,...]
MY_t7_fire = MinMaxScaler(MY_t7_fire, MY_t7_fire.shape[0], MY_t7_fire.shape[1])

train_x_my = np.stack((t0_arrays_my, t1_arrays_my, t2_arrays_my, t3_arrays_my, t4_arrays_my, t5_arrays_my, t6_arrays_my), axis=0)
train_y_my = np.stack((MY_t1_fire, MY_t2_fire, MY_t3_fire, MY_t4_fire, MY_t5_fire, MY_t6_fire, MY_t7_fire), axis=0)

# 군위 산불 데이터
# 시간별로 path 설정 # 마지막 화선은 DF에 없음  # slope, aspect 없는 ver
file_path = pd.DataFrame({"t0" : ["GW_0410_1330.tif", "GW_wd_t0.tif", "GW_ws_t0.tif", "GW_DEM.tif", "GW_NDVI.tif"],
                          "t1" : ["GW_0410_1500.tif", "GW_wd_t1.tif", "GW_ws_t1.tif", "GW_DEM.tif", "GW_NDVI.tif"],
                          "t2" : ["GW_0411_1200.tif", "GW_wd_t2.tif", "GW_ws_t2.tif", "GW_DEM.tif", "GW_NDVI.tif"],
                          "t3" : ["GW_0411_1550.tif", "GW_wd_t3.tif", "GW_ws_t3.tif", "GW_DEM.tif", "GW_NDVI.tif"]})

file_path

# Iterate through each column in the DataFrame and read TIF files
# Assuming your DataFrame is named file_path
data_arrays = {}

for col in file_path.columns:
    time_step_arrays = []

    for file_name in file_path[col]:
        file_path_full = "/content/drive/MyDrive/23-2_Capstone_team1/data/GW/" + file_name  # Replace with your actual directory path
        array = tif_to_array(file_path_full)
        time_step_arrays.append(array)

    # Stack arrays along the fourth axis
    stacked_arrays = np.stack(time_step_arrays, axis=2)

    # Store the stacked arrays in a dictionary
    data_arrays[col] = stacked_arrays

# Access the arrays for a specific time step, for example, t0
t0_arrays_gw = data_arrays["t0"]
t1_arrays_gw = data_arrays["t1"]
t2_arrays_gw = data_arrays["t2"]
t3_arrays_gw = data_arrays["t3"]

GW_t1_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/GW/GW_0410_1500.tif")
GW_t1_fire = GW_t1_fire.read()[0,...]
GW_t1_fire = MinMaxScaler(GW_t1_fire, GW_t1_fire.shape[0], GW_t1_fire.shape[1])
GW_t2_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/GW/GW_0411_1200.tif")
GW_t2_fire = GW_t2_fire.read()[0,...]
GW_t2_fire = MinMaxScaler(GW_t2_fire, GW_t2_fire.shape[0], GW_t2_fire.shape[1])
GW_t3_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/GW/GW_0411_1550.tif")
GW_t3_fire = GW_t3_fire.read()[0,...]
GW_t3_fire = MinMaxScaler(GW_t3_fire, GW_t3_fire.shape[0], GW_t3_fire.shape[1])
GW_t4_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/GW/GW_0412_1410.tif")
GW_t4_fire = GW_t4_fire.read()[0,...]
GW_t4_fire = MinMaxScaler(GW_t4_fire, GW_t4_fire.shape[0], GW_t4_fire.shape[1])

train_x_gw = np.stack((t0_arrays_gw, t1_arrays_gw, t2_arrays_gw, t3_arrays_gw), axis=0)
train_y_gw = np.stack((GW_t1_fire, GW_t2_fire, GW_t3_fire, GW_t4_fire), axis=0)
train_x_gw.shape, train_y_gw.shape

# 강릉 산불 데이터

# 시간별로 path 설정 # 마지막 화선은 DF에 없음  # slope, aspect 없는 ver
file_path = pd.DataFrame({"t0" : ["GN_0411_1000.tif", "GN_wd_t0.tif", "GN_ws_t0.tif", "GN_DEM.tif", "GN_NDVI.tif"],
                          "t1" : ["GN_0411_1130.tif", "GN_wd_t1.tif", "GN_ws_t1.tif", "GN_DEM.tif", "GN_NDVI.tif"],
                          "t2" : ["GN_0411_1230.tif", "GN_wd_t2.tif", "GN_ws_t2.tif", "GN_DEM.tif", "GN_NDVI.tif"],
                          "t3" : ["GN_0411_1330.tif", "GN_wd_t3.tif", "GN_ws_t3.tif", "GN_DEM.tif", "GN_NDVI.tif"],
                          "t4" : ["GN_0411_1530.tif", "GN_wd_t4.tif", "GN_ws_t4.tif", "GN_DEM.tif",  "GN_NDVI.tif"],
                          "t5" : ["GN_0411_1630.tif", "GN_wd_t4.tif", "GN_ws_t4.tif", "GN_DEM.tif",  "GN_NDVI.tif"]})
file_path

# Iterate through each column in the DataFrame and read TIF files
# Assuming your DataFrame is named file_path
data_arrays = {}

for col in file_path.columns:
    time_step_arrays = []

    for file_name in file_path[col]:
        file_path_full = "/content/drive/MyDrive/23-2_Capstone_team1/data/GN/" + file_name  # Replace with your actual directory path
        array = tif_to_array(file_path_full)
        time_step_arrays.append(array)

    # Stack arrays along the fourth axis
    stacked_arrays = np.stack(time_step_arrays, axis=2)

    # Store the stacked arrays in a dictionary
    data_arrays[col] = stacked_arrays

# Access the arrays for a specific time step, for example, t0
t0_arrays_gn = data_arrays["t0"]
t1_arrays_gn = data_arrays["t1"]
t2_arrays_gn = data_arrays["t2"]
t3_arrays_gn = data_arrays["t3"]
t4_arrays_gn = data_arrays["t4"]
t5_arrays_gn = data_arrays["t5"]

GN_t1_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/GN/GN_0411_1130.tif")
GN_t1_fire = GN_t1_fire.read()[0,...]
GN_t1_fire = MinMaxScaler(GN_t1_fire, GN_t1_fire.shape[0], GN_t1_fire.shape[1])

GN_t2_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/GN/GN_0411_1230.tif")
GN_t2_fire = GN_t2_fire.read()[0,...]
GN_t2_fire = MinMaxScaler(GN_t2_fire, GN_t2_fire.shape[0], GN_t2_fire.shape[1])

GN_t3_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/GN/GN_0411_1330.tif")
GN_t3_fire = GN_t3_fire.read()[0,...]
GN_t3_fire = MinMaxScaler(GN_t3_fire, GN_t3_fire.shape[0], GN_t3_fire.shape[1])

GN_t4_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/GN/GN_0411_1530.tif")
GN_t4_fire = GN_t4_fire.read()[0,...]
GN_t4_fire = MinMaxScaler(GN_t4_fire, GN_t4_fire.shape[0], GN_t4_fire.shape[1])

GN_t5_fire = rasterio.open("/content/drive/MyDrive/23-2_Capstone_team1/data/GN/GN_0411_1630.tif")
GN_t5_fire = GN_t5_fire.read()[0,...]
GN_t5_fire = MinMaxScaler(GN_t5_fire, GN_t5_fire.shape[0], GN_t5_fire.shape[1])

train_x_gn = np.stack((t0_arrays_gn, t1_arrays_gn, t2_arrays_gn, t3_arrays_gn, t4_arrays_gn, t5_arrays_gn), axis=0)
train_y_gn = np.stack((GN_t1_fire, GN_t2_fire, GN_t3_fire, GN_t4_fire, GN_t5_fire), axis=0)