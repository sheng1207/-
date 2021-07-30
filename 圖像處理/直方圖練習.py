import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("./images/test6.jpg")
img1 = cv.imread("./images/test6.jpg", 0)
color = ("B", "G", "R")
histr = cv.calcHist([img], [0], None, [256], [0, 256])

plt.plot(histr)
plt.xlim([0, 256])
plt.show()