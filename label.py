import json

import cv2

files = [
    'input/OnDesk/ScreenShot26.png',
    'input/OnWall/ScreenShot12.png',
    'input/Round/ScreenShot20.png',
]


def save_results():
    with open('labels.json', 'w', encoding='utf-8') as f:
        json.dump(file_to_rectangles, f, ensure_ascii=False, indent=4)


def record_and_show_next_image_stop_when_last():
    global current_file_index, rectangles, files

    file = files[current_file_index]
    file_to_rectangles[file] = rectangles

    if current_file_index == (len(files) - 1):
        return

    rectangles = []
    current_file_index += 1

    return


# State
rectangles = []
drawing = False

current_file_index = 0

file_to_rectangles = {}


# State updater
def draw_rectangle(event, x, y, flags, params):
    global rectangles, drawing

    if drawing and event == cv2.EVENT_LBUTTONDOWN:
        drawing = False

        return

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        rectangles.append((x, y, x, y))

    if not drawing:
        return

    if event == cv2.EVENT_MOUSEMOVE:
        last = len(rectangles) - 1
        rectangles[last] = (rectangles[last][0], rectangles[last][1], x, y)


cv2.namedWindow('image')

cv2.setMouseCallback('image', draw_rectangle)
# Render
while True:
    file = files[current_file_index]
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (0, 0), fx=0.8, fy=0.8)

    for draw in rectangles:
        cv2.rectangle(image, (draw[0], draw[1]), (draw[2], draw[3]), (255, 0, 0), thickness=2)

    cv2.imshow('image', image)

    key = cv2.waitKey(17)

    if key == 100:
        record_and_show_next_image_stop_when_last()

    if key == 115:
        save_results()

    if key == 27:
        break
