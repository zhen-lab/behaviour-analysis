import cv2
import glob
import os

def file_name_str_to_int(f_path):
    f_name = os.path.basename(f_path)
    str_key, _ = os.path.splitext(f_name)
    return int(str_key)

path = './data/jpeg-30s/'
img_extension = "*.jpg"
frames_per_second = 10

img_files = sorted(glob.glob(path + img_extension))
img_files.sort(key=file_name_str_to_int)

images = [cv2.imread(file) for file in img_files]
width, height, _ = images[0].shape

video = cv2.VideoWriter(path + 'test.avi', cv2.VideoWriter_fourcc(*'XVID'), frames_per_second, (height, width))

for img in images:
    video.write(img)

video.release()
