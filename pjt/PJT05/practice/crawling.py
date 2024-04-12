




import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/tag/love/'

# url을 통해서 html의 내용을 받을 수 있다.
response = requests.get(url)
html_text = response.text
# print(html_text)

# 하지만, 우리는 quote한 내용이 필요한 것이다.
# body > div > div (class = quote) > span (text)

soup = BeautifulSoup(html_text, 'html.parser')
# print(type(soup))

# 그럼 탐색해보자.
main = soup.find('body') # body 태그의 요소를 가져올 수 있다. (1개)
# print(main)

span_tag = soup.find_all('span') # list 반환된다.
# print(span_tag)
# for i in range(20):
#     if not i%2:
#         print(span_tag[i])

# css selector를 사용해서 class에 해당하는 것을 탐색한다.
spans = soup.select('.text')
# print(spans)

for text in spans:
    quote = text.text
    print(f'인용글 : {quote}')


