import cv2
import glob

path = './data/jpeg-30s/'
img_extension = "*.jpg"
fps = 10

img_files = glob.glob(path + img_extension)

images = [cv2.imread(file) for file in img_files]

video_width, video_height, _ = images[0].shape

video = cv2.VideoWriter(
  path + "test.avi",
  cv2.VideoWriter_fourcc(*"XVID"),
  # -1,
  fps,
  (video_height, video_width))

for image in images:
  video.write(image)

video.release()


































# def sort_file_by_name_num(f_path):
#     f_name = f_path.split('/')[-1]
#     key = f_name.split('.')[0]
#     return int(key)


# img_files.sort(key=sort_file_by_name_num)
