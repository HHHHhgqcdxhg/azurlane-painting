# Authors: Robert Layton <robertlayton@gmail.com>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Mathieu Blondel <mathieu@mblondel.org>
#
# License: BSD 3 clause
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time
import cv2


def make(imgPath, n_colors=8):
    if isinstance(imgPath,str):
        if not imgPath[-3:] == "png":
            rawImage = cv2.imread(imgPath)
        else:
            rawImage = cv2.imread(imgPath, -1)
    else:
        rawImage = imgPath

    rawImage = np.array(rawImage, dtype=np.float64) / 255
    w, h, d = tuple(rawImage.shape)
    assert d == 3
    image_array = np.reshape(rawImage, (w * h, d))
    image_array_sample = shuffle(image_array, random_state=0)[:1000]
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)
    labels = kmeans.predict(image_array)
    outImg = recreate_image(kmeans.cluster_centers_, labels, w, h)
    return outImg


def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image


if __name__ == '__main__':
    n_colors = 3
    outImg = make("testimg/ysxb.jpg", n_colors)
    outImg *= 255
    outImg = np.array(outImg,dtype='uint8')
    cv2.imshow(f"{n_colors}colors", outImg)
    cv2.waitKey(0)
# plt.figure(2)
# plt.clf()
# plt.axis('off')
# plt.title(f'Quantized image ({n_colors} colors, K-Means)')
