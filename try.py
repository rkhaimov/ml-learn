import cv2
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier


def read(file: str):
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    return np.hstack(image)


cls: RandomForestClassifier = joblib.load('clf.joblib')

x = read('input/Round/F4power3.png')

predict = cls.predict([x])

map_label_to_read = ['OnDesk', 'OnWall', 'Round']

print(list(map(lambda p: map_label_to_read[p], predict)))
print(cls.predict_proba([x]))
