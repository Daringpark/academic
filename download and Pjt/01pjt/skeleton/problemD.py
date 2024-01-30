import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.

def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
  api_key = '44d2341d5bf00098167d20245dc95c84'

  whole_list = []
  # 요구사항에 맞도록 이곳의 코드를 수정합니다.
  url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  back_url = {'auth' : api_key, 'topFinGrpNo' : '020000', 'pageNo' : 1}
  result = requests.get(url, params = back_url).json()
  result_A = result.get('result').get('baseList')
  result_B = result.get('result').get('optionList')

  for products in result_A :
    product_dictionary = {}
    information_list = []
    for options in result_B :
      if products['fin_prdt_cd'] == options['fin_prdt_cd'] :
        product_infomation = {}
        product_infomation['저축 금리'] = options['intr_rate']
        product_infomation['저축 기간'] = options['save_trm']
        product_infomation['저축금리유형'] = options['intr_rate_type']
        product_infomation['저축금리유형명'] = options['intr_rate_type_nm']
        product_infomation['최고 우대금리'] = options['intr_rate2']      

        information_list.append(product_infomation)
        product_dictionary['금리정보'] = information_list
    product_dictionary['금융상품명'] = products['fin_prdt_nm']
    product_dictionary['금융회사명'] = products['kor_co_nm']
    whole_list.append(product_dictionary)
  
  result = whole_list
  return result

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
