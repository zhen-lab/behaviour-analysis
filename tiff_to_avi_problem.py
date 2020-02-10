import cv2
import glob
tiff_files = glob.glob("./data/*.tiff")

frames_per_second = 10
images = [cv2.imread(file) for file in tiff_files]
video_width, video_height, _ = images[0].shape
print(video_width, video_height)

video = cv2.VideoWriter(
  "./data/test.avi",
  cv2.VideoWriter_fourcc(*"XVID"),
  # -1,
  frames_per_second,
  (video_width, video_height),
  True
)

for image in images:
  video.write(image)

video.release()