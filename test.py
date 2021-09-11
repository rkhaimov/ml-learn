import cv2
import numpy as np
from PIL import ImageGrab

import parse_words
from parse_options import parse_sections


def intersection(left, right):
    result = []

    for index in range(len(left)):
        if left[index] == right[index]:
            result.append(left[index])

    return result


letters = 5
image = ImageGrab.grabclipboard()
image = np.array(image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image = cv2.imread('input/OnWall/ScreenShot36.png')

raw_options, raw_answers = parse_sections(image)

options = parse_words.parse_words(raw_options, letters)
answers = parse_words.parse_words(raw_answers, letters)
numbers = parse_words.parse_numbers(raw_answers)

tips = {}

for index in range(len(answers)):
    tips[answers[len(answers) - 1 - index]] = numbers[len(numbers) - 1 - index]

solutions = []

print(tips)

for option in options:
    matches = all(map(lambda tip: len(intersection(option, tip)) == tips[tip], tips))

    if matches:
        solutions.append(option)

print(solutions)
