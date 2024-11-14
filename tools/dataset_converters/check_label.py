import argparse
from PIL import Image
import os
import sys


def main(args):
    folder_path = args.folder_path
    # 遍历文件夹下的所有文件
    for filename in os.listdir(folder_path):
        # 拼接文件路径
        image_path = os.path.join(folder_path, filename)
        
        # 检查文件是否为图片文件
        if image_path.endswith('.png') or image_path.endswith('.tif'):
        # 打开图片文件
            with Image.open(image_path) as img:
                # 将图片转换为适合的模式，例如 'RGB'
                
                img = img.convert('RGB')
                # 加载图片数据
                # img = img.convert('L')
                pixels = list(img.getdata())
            max_pixel_value = max(pixels)
            unique_pixel_values = set(pixels)
            print(f"file name: {filename}")
            print(f"all class value: {unique_pixel_values}")
            
            # 设置范围值
            if args.dataset == 'loveda':
                max_val = (8, 8, 8)
                min_val = (0, 0, 0)
            elif args.dataset == 'potsdam':
                max_val = (7, 7, 7)
                min_val = (0, 0, 0)
            elif args.dataset == 'vaihingen':
                max_val = (7, 7, 7)
                min_val = (0, 0, 0)
            elif args.dataset == 'casid':
                max_val = (6, 6, 6)
                min_val = (-1, -1, -1)
            elif args.dataset == 'potsdam_res':
                max_val = (6, 6, 6)
                min_val = (0, 0, 0)
            elif args.dataset == 'rescue':
                max_val = (6, 6, 6)
                min_val = (0, 0, 0)
            elif args.dataset == 'road':
                max_val = (2, 2, 2)
                min_val = (-1, -1, -1)
            elif args.dataset == 'building':
                max_val = (2, 2, 2)
                min_val = (-1, -1, -1)

            for pixel in unique_pixel_values:
                if not (min_val < pixel < max_val):
                    print(f"error class value: {pixel}")
                    print(f"correct value should be: {min_val} to {max_val}")
                    sys.exit(1)

    print("Check labels done! All labels are correct!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder_path', type=str, default='')
    parser.add_argument('--dataset', type=str, default='') # loveda, 
    args = parser.parse_args()
    main(args)