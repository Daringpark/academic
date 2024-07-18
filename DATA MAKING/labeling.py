import glob
import json
import os

# 디렉토리 설정
directory_path = f'./2.Ano/'
os.makedirs(f'{directory_path}/output', exist_ok = True)

# 현재 진행된 file count
file_count = 0 

# 내가 원하는 객체의 포지션과 BBOX 정규화
def json_to_txt(path):
    global file_count

    # json 파일을 열어서 data에 저장하기
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    content = ''
    # Pothole labeling
    for annotation in data['annotations']:
        # annotation -> 0 1 2 : norm, overload, pothole
        if annotation['category_id'] == 8:
            new_x = str(round(float(annotation['bbox'][0])/1280, 7))
            new_w = str(round(float(annotation['bbox'][1])/720, 7))
            new_y = str(round(float(annotation['bbox'][2])/1280, 7))
            new_h = str(round(float(annotation['bbox'][3])/720, 7))
            temp = f'2 {new_x} {new_y} {new_w} {new_h}' + '\n'
            content += temp

    file_name = data['images']['file_name'][:-4] + '.txt'
    # json -> txt 파일화
    # file_name.txt -> 2 0.xxx 0.xxx 0.xxx 0.xxx
    with open(directory_path + 'output/' + file_name, 'w', encoding='utf-8') as f:
        f.write(content)
    file_count += 1

# 디렉토리 내 모든 JSON 파일 검색
json_files = glob.glob(directory_path + '*.json')

# 각 JSON 파일에서 file path별 json file과 img file 옮기기
for file_path in json_files:
    json_to_txt(file_path)

print(f'총 {file_count}의 json을 txt 변환하였습니다.')





