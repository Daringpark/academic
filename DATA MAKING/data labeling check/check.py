import os
import cv2
import matplotlib.pyplot as plt

def process_annotations(annotation_dir, image_dir):
    annotation_files = [f for f in os.listdir(annotation_dir) if f.endswith('.txt')]
    
    for file in annotation_files:
        with open(os.path.join(annotation_dir, file), 'r') as f:
            lines = f.readlines()
        
        image_name = os.path.splitext(file)[0] + '.png'
        image_path = os.path.join(image_dir, image_name)
        
        # Check if image file exists
        if not os.path.exists(image_path):
            print(f"Image file '{image_name}' does not exist in '{image_dir}'. Skipping...")
            continue
        
        img = cv2.imread(image_path)
        
        if img is None:
            print(f"Failed to load image '{image_name}'")
            continue
        
        height, width, _ = img.shape
        
        for line in lines:
            label = list(map(float, line.strip().split(' '))) 
            class_id = int(label[0])
            x = float(label[1]) * width
            y = float(label[2]) * height
            w = float(label[3]) * width
            h = float(label[4]) * height
            
            x1 = int(x)
            y1 = int(y)
            x2 = int(x + w)
            y2 = int(y + h)
            
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, f'Class: {class_id}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        print(image_name, label[1], label[2], label[3], label[4])


        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img_rgb)
        plt.axis('off')
        plt.title(f'Annotated Image: {image_name}')
        plt.show()

# 실행
annotation_dir = './test_annotation/'  # annotation 파일이 있는 디렉토리
image_dir = './test_image/'  # annotation 파일에 해당하는 이미지가 있는 디렉토리

process_annotations(annotation_dir, image_dir)