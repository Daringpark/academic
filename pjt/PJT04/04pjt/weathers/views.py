from django.shortcuts import render, HttpResponse
from io import BytesIO
import base64
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from copy import deepcopy

# 테이블 불러오기
def load():
    table = pd.read_csv('static/austin_weather.csv')
    return table

# Create your views here.
def index(request):
    return render(request, 'weathers/index.html')

def problem1(request):
    table = load()
    df = table
    context = {
        'df' : df
    }
    return render(request, 'weathers/problem1.html', context)

# 이미지화 시키기
# buffer = BytesIO()
# plt.savefig(buffer, format = 'png')
# img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('/n', '')
# context = { 'image' : f'data:image/png;base64, {img_base64}', }

# 일별 다중 그래프
def problem2(request):
    # Init
    # Temperature field 전처리
    table = load()
    table['TempHighF'] = table['TempHighF'].astype(int)
    table['TempAvgF'] = table['TempAvgF'].astype(int)
    table['TempLowF'] = table['TempLowF'].astype(int)
    df = table
    plt.clf()

    # Date field 전처리
    df['Date'] = pd.to_datetime(df['Date'])
    Date = df['Date']

    # Graph Format
    plt.figure(figsize=(12,8))
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    
    # Y axis Define
    TempHigh = df['TempHighF']
    TempAvg = df['TempAvgF']
    TempLow = df['TempLowF']

    # Plot with label
    plt.plot(Date, TempHigh, label = 'TempHighF')
    plt.plot(Date, TempAvg, label = 'TempAvgF')
    plt.plot(Date, TempLow, label = 'TempLowF')
    plt.legend(loc = 'lower center')
    # plt.show()

    # plt to html
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    context = { 'image' : f'data:image/png;base64, {img_base64}', }    
    return render(request, 'weathers/problem2.html', context)

def problem3(request):

    table = load()
    df = table
    # Temperature field 전처리
    table['TempHighF'] = table['TempHighF'].astype(int)
    table['TempAvgF'] = table['TempAvgF'].astype(int)
    table['TempLowF'] = table['TempLowF'].astype(int)
    # Date field 전처리
    df['Date'] = pd.to_datetime(df['Date'])
    Date = df['Date']

    y1 = df.groupby(df['Date'].dt.to_period('M'))['TempHighF'].mean()
    y2 = df.groupby(df['Date'].dt.to_period('M'))['TempAvgF'].mean()
    y3 = df.groupby(df['Date'].dt.to_period('M'))['TempLowF'].mean()

    # 그래프 초기화
    plt.clf()
    
    # graph format
    plt.figure(figsize=(12,8))
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')

    # x = table.groupby(table['Date'].dt.to_period('M'))
    # # Plot with label
    y1.plot(label = 'TempHighF')
    y2.plot(label = 'TempAvgF')
    y3.plot(label = 'TempLowF')
    plt.axis('auto')
    plt.legend(loc = 'lower right')

    # plt to html
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    context = { 'image' : f'data:image/png;base64, {img_base64}', }    
    return render(request, 'weathers/problem3.html', context)

def problem4(request):
    table = load()
    df = table
    # 0. 사전에 event가 없는 경우, 바꿔주기
    df = df.replace(to_replace={'Events':' '}, value='No Events')
    # 1. event 쪼개기
    event_explode = df['Events'].str.split(' , ').explode()
    # 2. Events : value
    event_count = event_explode.value_counts()

    # 그래프 초기화
    plt.clf()

    # print(event_count)
    # graph format
    plt.figure(figsize=(10,6))
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')

    x = list(event_count.keys())
    y = event_count.to_list()
    
    # plt.hist(x, bins = 16, weights= y, align = 'left')
    plt.bar(x, y, align='center')


    # plt to html
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    context = { 'image' : f'data:image/png;base64, {img_base64}', }    
    return render(request, 'weathers/problem4.html', context)