from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm


# Create your views here.
def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    form = KeywordForm()
    context = {
        'keywords' : keywords,
        'form' : form
    }
    return render(request, 'trends/keyword.html', context)

def kw_delete(request, key_pk):
    if request.method == "POST":
        keyword = Keyword.objects.get(pk = key_pk)
        keyword.delete()
    return redirect('trends:keyword')

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def get_url(keyword, year):
    url = f'https://www.google.com/search?q={keyword}&tbs=qdr:{year}'
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.select_one('#result-stats')
    return result.text

# Keyword 테이블에 저장된 키워드들을 활용하여 크롬 검색 결과 페이지 크롤링을 수행합니다.
# 페이지의 정보 중 "검색 결과 개수"를 추출하여 Trend 테이블에 저장하게 합니다.
# search_period column은 'all' 로 저장합니다.
# 저장시 이미 저장되어 있는 키워드면, 새로 생성하지 않고, 검색 결과 개수만 변경합니다.
def crawling(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        for y in [0, 'y']:
            temp = get_url(keyword.name, y)
            print(temp)
            counts = ''
            counts = 1
            counts = int(counts)
            if y:
                if Trend.objects.filter(name = keyword, search_period = 'all').exists():
                    trend = Trend.objects.get(name = keyword, search_period = 'all')
                    trend.result = counts
                    trend.save()
                else:
                    Trend.objects.create(name = keyword, result = counts, search_period = 'all')
            else:
                if Trend.objects.filter(name = keyword, search_period = 'year').exists():
                    trend = Trend.objects.get(name = keyword, search_period = 'year')
                    trend.result = counts
                    trend.save()
                else:
                    Trend.objects.create(name = keyword, result = counts, search_period = 'year')

    # 크롤링 개수, 검색일자
    Trends = Trend.objects.all()
    context = {
        'Trends' : Trends
    }
    return render(request, 'trends/crawling.html', context)

import matplotlib.pyplot as plt
from io import BytesIO
import base64

def histo(request):
    trends = Trend.objects.filter(search_period = 'all')
    # x 값과 y 값 초기화
    x_values = [trend.name.name for trend in trends]
    y_values = [trend.result for trend in trends]

    # 그래프 초기화
    plt.clf()

    # 히스토그램 그리기
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Trend Analysis')
    plt.grid(True)
    plt.bar(x_values, y_values)

    # plt to html img
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    context = { 'image' : f'data:image/png;base64, {img_base64}', }
    return render(request, 'trends/crawling_histogram.html', context)

def advanced(request):
    trends = Trend.objects.filter(search_period = 'year')
    # x 값과 y 값 초기화
    x_values = [trend.name.name for trend in trends]
    y_values = [trend.result for trend in trends]

    # 그래프 초기화
    plt.clf()

    # 히스토그램 그리기
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Trend Analysis')
    plt.grid(True)
    plt.bar(x_values, y_values)

    # plt to html img
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    context = { 'image' : f'data:image/png;base64, {img_base64}', }
    return render(request, 'trends/crawling_advanced.html', context)