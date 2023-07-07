import cv2
import numpy as np
import os

results = []

for i in range(1,5):
    paths = os.listdir(os.path.join("resources","black hole", str(i)))
    result = None
    for path in paths:
        img = cv2.imread(os.path.join("resources","black hole", str(i), path))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img.astype(np.float32)
        if result is None:
            result = img
        else:
            result += img

    result /= len(paths)
    result = result.astype(np.uint8)
    results.append(result)

concatenated_horizontal_1 = np.concatenate((results[0], results[1]), axis=1)
concatenated_horizontal_2 = np.concatenate((results[2], results[3]), axis=1)
final_image = np.concatenate((concatenated_horizontal_1, concatenated_horizontal_2), axis=0)

cv2.imwrite("results/black_hole.jpg",final_image)

