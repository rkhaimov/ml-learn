import json

import cv2
import joblib
import numpy as np
from joblib import load
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputRegressor

import image_to_string


def parse_sections(original):
    with open('labels.json') as f:
        labels = json.load(f)

    cls: RandomForestClassifier = joblib.load('clf.joblib')
    image = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)

    x = np.hstack(image)
    type = __as_type(cls.predict([x])[0])
    sections = labels[type]

    original = cv2.resize(original, (0, 0), fx=0.8, fy=0.8)
    options_0 = original[sections[0][3]:sections[0][1], sections[0][2]:sections[0][0]]
    options_1 = original[sections[1][3]:sections[1][1], sections[1][2]:sections[1][0]]
    answers = original[sections[2][3]:sections[2][1], sections[2][2]:sections[2][0]]

    # original = cv2.rectangle(original, sections[0][:2], sections[0][2:], (255, 0, 0))
    #
    # cv2.imshow('options_0', original)
    #
    # cv2.waitKey(0)

    return (image_to_string.image_to_string(options_0) + image_to_string.image_to_string(options_1),
            image_to_string.image_to_string(answers))


def __as_type(enum):
    return ['OnDesk', 'OnWall', 'Round'][enum]
