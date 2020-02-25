import numpy as np
from math import sqrt
from skimage import io as sk_io
from skimage import feature
from skimage.color import rgb2gray
import cv2
import matplotlib.pyplot as plt
import tifffile

puncta_img = tifffile.imread('./data/puncta/subtracted.tif')

# a puncta is a row of tuples containing (x, y, sigma)
# where x, y is the pixel position in the image
# where sigma is proprotional to the punctums radius
puncta = feature.blob_log(puncta_img, max_sigma=5, overlap=0.9, threshold=.05)

# Compute radii of each punctum
# radius = sqrt(2) * sigma
puncta[:, 2] = puncta[:, 2] * sqrt(2)

# show the puncta image
fig, ax = plt.subplots(1)
ax.set_title('puncta')
ax.imshow(np.invert(puncta_img), cmap=plt.cm.binary, aspect='auto')

# show where each recognized punctum is on the image
for punctum in puncta:
    y, x, r = punctum
    punctum_marker = plt.Circle((x, y), r, color='blue', linewidth=2, fill=False)
    ax.add_patch(punctum_marker)

plt.show()