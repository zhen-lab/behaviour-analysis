import numpy as np
from math import sqrt
from skimage import io as sk_io
from skimage import feature
from skimage.color import rgb2gray
import cv2
import matplotlib.pyplot as plt
import tifffile

puncta_img = tifffile.imread('./data/puncta/subtracted.tif')
# puncta_img = sk_io.imread('./data/puncta/subtracted.jpg')

puncta_img_gray = puncta_img

blobs_log = feature.blob_log(puncta_img_gray, max_sigma=30, num_sigma=10, threshold=.05)

# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

fig, ax = plt.subplots(1)
ax.set_title('puncta')
ax.imshow(puncta_img_gray, cmap=plt.cm.binary, aspect='auto')

for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r, color='blue', linewidth=2, fill=False)
    ax.add_patch(c)

plt.show()