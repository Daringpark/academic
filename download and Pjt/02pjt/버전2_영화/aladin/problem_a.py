import requests
from pprint import pprint
print = pprint
import json


ttbkey = 'ttbshoostar06111532001'
query_type = 'Title'
MaxResults = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101

URL = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query=aladdin&QueryType={query_type}&{MaxResults}&start={start}&SearchTarget={search_target}&output={output}s&Version={version}'

response = requests.get(URL).json()
print(response)


# def author_works():
#     # 여기에 코드를 작성합니다.
    

#     pass


# # 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     print(author_works())
