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
import time
import c8


def make(imgPath, n_colors=8):
    # import time
    # t0 = time.perf_counter()
    if isinstance(imgPath,str):
        if not imgPath[-3:] == "png":
            rawImage = cv2.imread(imgPath)
        else:
            rawImage = cv2.imread(imgPath, -1)
    else:
        rawImage = imgPath

    rawImage = np.array(rawImage, dtype=np.float64) / 255
    w, h, d = rawImage.shape
    assert d == 3
    image_array = np.reshape(rawImage, (w * h, d))
    image_array_sample = shuffle(image_array, random_state=0)[:1000]
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)
    labels = kmeans.predict(image_array)
    codeBook = kmeans.cluster_centers_

    # 在codebook中将颜色转为8色
    codeBook,codeBookFollow = handdleCodeBook(codeBook)

    outImgFollow = recreate_image2(codeBook, labels, w, h,codeBookFollow)
    return outImgFollow


def handdleCodeBook(codeBook):
    codeBook *= 255
    codeBook=codeBook.astype(int)
    codeBookFollow = np.zeros(codeBook.__len__())
    for i,c in enumerate(codeBook):
        newColor,follow = c8.to8color(c[0],c[1],c[2])
        codeBook[i,:] = newColor
        codeBookFollow[i] = follow
    return codeBook,codeBookFollow

def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i,j,:] = codebook[labels[label_idx]]
            label_idx += 1
    return image

def recreate_image2(codebook, labels, w, h,codeBookFollow):
    # print(codeBookFollow)
    # codebook.dtype = "uint8"
    # mapLabels = lambda label:codebook[label]
    mapLabelsFollow = lambda label:codeBookFollow[label]
    # m = list(map(mapLabels , labels))
    # m = np.apply_along_axis(mapLabels, 0, labels)
    mFollow = np.apply_along_axis(mapLabelsFollow, 0, labels)
    # m = list(map(lambda label:operator.itemgetter(label)(codebook) , labels))
    # m = np.fromfunction(lambda label:codebook[label] , labels)
    # d = codebook.shape[1]
    # m = m.reshape((w,h,d))
    mFollow = mFollow.astype(int).reshape((w,h))
    # mFollow = mFollow

    return mFollow


if __name__ == '__main__':

    t0 = time.perf_counter()
    n_colors = 16
    outImg,outImgFollow = make("testimg/1.jpg", n_colors)
    # outImg *= 255
    outImg = np.array(outImg,dtype='uint8')
    t1 = time.perf_counter()
    print(t1 - t0)
    cv2.imshow(f"{n_colors}colors", outImg)
    print(outImgFollow)
    cv2.waitKey(0)
    # def my_func(a):
    #     print(a)
    #     return (a[0] + a[-1]) * 0.5
    #
    # b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    #
    # res = np.apply_along_axis(my_func, 1, b)
    # print(res)
# plt.figure(2)
# plt.clf()
# plt.axis('off')
# plt.title(f'Quantized image ({n_colors} colors, K-Means)')
