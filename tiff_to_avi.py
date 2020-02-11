import cv2
import glob

def sorted_tiff(f_path):
    tiff_name = f_path.split('/')[-1]
    key = tiff_name.split('.')[0]
    return int(key)

tiff_files = glob.glob("./data/*.tiff")
tiff_files.sort(key=sorted_tiff)

images = []

for file in tiff_files:
    img = cv2.imread(file)
    # cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    images.append(img)

width, height, _ = images[0].shape

video = cv2.VideoWriter("./data/test.avi", cv2.VideoWriter_fourcc(*'XVID'), 26, (height, width))

for img in images:
    video.write(img)

video.release()