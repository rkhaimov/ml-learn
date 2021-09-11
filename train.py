import os

import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

on_desk = os.listdir('input/OnDesk')
on_wall = os.listdir('input/OnWall')
round_t = os.listdir('input/Round')


def read(file: str):
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    return np.hstack(image)


def read_and_shift(file: str):
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    transformation = np.float32([
        [1, 0, 1],
        [0, 1, 1]
    ])

    shifted = cv2.warpAffine(image, transformation, (image.shape[1], image.shape[0]))

    return np.hstack(shifted)


on_desk_X = np.concatenate([
    np.array(
        list(map(lambda img_path: read(f'input/OnDesk/{img_path}'), on_desk))),
    np.array(
        list(map(lambda img_path: read_and_shift(f'input/OnDesk/{img_path}'), on_desk)))
])

on_wall_X = np.concatenate([
    np.array(
        list(map(lambda img_path: read(f'input/OnWall/{img_path}'), on_wall))),
    np.array(
        list(map(lambda img_path: read_and_shift(f'input/OnWall/{img_path}'), on_wall)))
])

round_X = np.concatenate([
    np.array(
        list(map(lambda img_path: read(f'input/Round/{img_path}'), round_t))),
    np.array(
        list(map(lambda img_path: read_and_shift(f'input/Round/{img_path}'), round_t)))
])

X = np.vstack([on_desk_X, on_wall_X, round_X])

on_desk_y = np.full((len(on_desk) * 2), 0)
on_wall_y = np.full((len(on_wall) * 2), 1)
round_y = np.full((len(round_t)) * 2, 2)

y = np.hstack([on_desk_y, on_wall_y, round_y])

groups = {}
for index, kind in enumerate(y):
    if kind not in groups:
        groups[kind] = [index]
        continue

    if len(groups[kind]) == 1:
        continue

    groups[kind].append(index)

train_idx = np.hstack(np.array([groups[kind] for kind in groups]).reshape(1, -1))
in_test = np.full(y.shape, False)
in_test[train_idx] = True

X_test = X[in_test]
y_test = y[in_test]

X_train = X[np.logical_not(in_test)]
y_train = y[np.logical_not(in_test)]

clf = RandomForestClassifier(max_depth=2, max_leaf_nodes=3, n_estimators=14, random_state=42, n_jobs=6)

clf.fit(X_train, y_train)

joblib.dump(clf, 'clf.joblib')

