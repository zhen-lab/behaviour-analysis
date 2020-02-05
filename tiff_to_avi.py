import cv2
import glob


def sorted_tiff(f_path):
    tiff_name = f_path.split('/')[-1]
    key = tiff_name.split('.')[0]
    return int(key)

tiff_files = glob.glob("./temp10/*.tiff")
tiff_files.sort(key=sorted_tiff)

images = [cv2.imread(file) for file in tiff_files]
width, height, layers = images[0].shape

video = cv2.VideoWriter("test.avi", cv2.VideoWriter_fourcc(*'XVID'), 26, (width, height))

for img in images:
    video.write(img)

video.release()