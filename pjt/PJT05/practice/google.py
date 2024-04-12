import requests
from bs4 import BeautifulSoup
from selenium import webdriver


url = f'https://www.google.com/search?q=%EC%82%AC%EA%B3%BC&oq=%EC%82%AC%EA%B3%BC&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDIzMjhqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8'
# search?q=keyword&oq=keyword&...

def get_url(keyword):
    url = f'https://www.google.com/search?q={keyword}'

    # 동적 페이지를 가져오기엔 별로다!
    # response = requests.get(url)
    # print(response.text)

    # 동적 내용이 채워진다.
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아온다.
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    result = soup.select_one('#result-stats')
    # div > class
    titles = soup.select('div.g')
    titles_result = ''
    for title in titles:
        title = title.select_one('.LC20lb.MBeuO.DKV0Md')
        if title:
            titles_result += f'\n'
            titles_result += f'{title.text}'
            print(title.text)

    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(result.text)
        file.write(titles_result)

get_url('사과')