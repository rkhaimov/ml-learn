import cv2
import numpy as np

# State
drawings = []
drawing = False


# State updater
def draw_rectangle(event, x, y, flags, params):
    global drawings, drawing

    if drawing and event == cv2.EVENT_LBUTTONDOWN:
        drawing = False

        return

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        drawings.append((x, y, x, y))

    if not drawing:
        return

    if event == cv2.EVENT_MOUSEMOVE:
        last = len(drawings) - 1
        drawings[last] = (drawings[last][0], drawings[last][1], x, y)


cv2.namedWindow('image')

cv2.setMouseCallback('image', draw_rectangle)
original = np.zeros((512, 512), np.uint8)

# Render
while True:
    copy = np.copy(original)

    for draw in drawings:
        cv2.rectangle(copy, (draw[0], draw[1]), (draw[2], draw[3]), (255, 0, 0), thickness=2)

    cv2.imshow('image', copy)

    key = cv2.waitKey(16)

    if key == 27:
        break
