import cv2
import glob

def sorted_tiff(f_path):
    tiff_name = f_path.split('/')[-1]
    key = tiff_name.split('.')[0]
    return int(key)

# path = './data/'

path = './data/8bit-tiff-30s/'
frames_per_second = 10

tiff_files = glob.glob(path + '*.tiff')
tiff_files.sort(key=sorted_tiff)

images = [cv2.imread(file) for file in tiff_files]
width, height, _ = images[0].shape

video = cv2.VideoWriter(path + 'test.avi', cv2.VideoWriter_fourcc(*'XVID'), frames_per_second, (height, width))

for img in images:
    video.write(img)

video.release()
