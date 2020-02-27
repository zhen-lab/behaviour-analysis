import cv2
import glob
import os

path = './data/jpeg-30s/'
img_extension = "*.jpg"
fps = 10
video_file_name = path + "test.avi"


img_files = glob.glob(path + img_extension)



images = [cv2.imread(file) for file in img_files]



video_height, video_width, _ = images[0].shape



video = cv2.VideoWriter(
  video_file_name,
  cv2.VideoWriter_fourcc(*"XVID"),
  fps,
  (video_width, video_height))

for image in images:
  video.write(image)

video.release()


































# def file_name_str_to_int(f_path):
#     f_name = os.path.basename(f_path)

#     str_key, _ = os.path.splitext(f_name)

#     return int(str_key)


# img_files.sort(key=file_name_str_to_int)
