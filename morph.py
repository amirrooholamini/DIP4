import cv2
import numpy as np

chavoshi = cv2.imread('resources/chavoshi.jpg', cv2.IMREAD_GRAYSCALE)
yeganeh = cv2.imread('resources/yeganeh.jpg', cv2.IMREAD_GRAYSCALE)

chavoshi = chavoshi.astype(np.float32)
yeganeh = yeganeh.astype(np.float32)

factors = [0, 0.3, 0.6, 0.9, 1]
results = []
for factor in factors:
    result = chavoshi*factor + yeganeh*(1-factor)
    result = result.astype(np.uint8)
    padded_result = np.pad(result, 4, mode='constant', constant_values=255)
    results.append(padded_result)

concatenated_results = np.concatenate(results, axis=1)

cv2.imwrite("results/morph.jpg",concatenated_results)