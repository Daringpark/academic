import glob
import json
import shutil
import os

# 데이터를 읽을 식별자 확인
identification_key = 'MainRoad_H02'

# 돌리기 전에 key값을 확인해주세요.
# JSON 파일들이 있는 디렉토리
directory_path = f'./raw/{identification_key}/annotation/'
img_path = f'./raw/{identification_key}/image/'

# Json 에서 찾을 pothole
desired_value = "Pothole on road"
file_count = 0
count = 0

print(os.getcwd())
os.mkdir(f'{directory_path}/2.Ano')
os.mkdir(f'{img_path}/1.Images')

def find_value_in_json_file(file_path):
    global count

    # json 파일을 열어 data에 저장하기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # for 문을 통해서 flag = True일 때 아래 결과물을 옮기는 식
    for annotation in data['annotations']:
        flag = False
        if annotation['category_id'] == 8:
            count += 1
            flag = True
            img_file_name = data['images']['file_name']
            break

    # 결과 출력
    if flag:
        print(img_file_name)
        json_file_name = img_file_name[:-4]+'_BBOX.json'
        print(json_file_name)

        # Json 파일 이동 경로 설정
        src_json_file = f'{directory_path}/{json_file_name}'
        dst_json_dir = f'{directory_path}/2.Ano/'

        # Img 파일 이동 경로 설정
        src__img_file = f'{img_path}/{img_file_name}'
        dst_img_dir = f'{img_path}/1.Images/'
        
        try:
            shutil.move(src_json_file, dst_json_dir)
            shutil.move(src__img_file, dst_img_dir)
        except:
            print(f'{img_file_name} is already in. {count}')

# 디렉토리 내 모든 JSON 파일 검색
json_files = glob.glob(directory_path + '*.json')

# 각 JSON 파일에서 file path별 json file과 img file 옮기기
for file_path in json_files:
    file_count += 1
    find_value_in_json_file(file_path)

print('Total : ', file_count, 'is checked.')
print('Total : ', count, 'is moved.')