import cv2
import numpy as np


def nothing(*args):
    pass


ondesk = cv2.imread('input/OnDesk/0.jpg', cv2.IMREAD_GRAYSCALE)
onwall = cv2.imread('input/OnWall/3.jpg', cv2.IMREAD_GRAYSCALE)
round = cv2.imread('input/Round/7.jpg', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('image')
cv2.createTrackbar('p_0', 'image', -1, 255, nothing)
cv2.createTrackbar('p_1', 'image', 1, 255, nothing)

# Render

while True:
    image = ondesk

    M = np.float32([
        [1, 0, 1],
        [0, 1, 1]
    ])

    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    cv2.imshow('image', shifted)

    key = cv2.waitKey(17)

    if key == 27:
        break
