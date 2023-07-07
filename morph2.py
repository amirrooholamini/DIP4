import cv2
import numpy as np

animal = cv2.imread('resources/animal.jpg', cv2.IMREAD_GRAYSCALE)
me = cv2.imread('resources/me.jpg', cv2.IMREAD_GRAYSCALE)

animal = animal.astype(np.float32)
me = me.astype(np.float32)

R,C = animal.shape
top = animal[:R//2,:]*0.5 + me[:R//2,:]*0.5
top = top.astype(np.uint8)

bottom = animal[R//2:,:]
for r in range(R//2,R):
    factor = r/R
    bottom[r - (R//2)] = animal[r,:]*factor + me[r,:]*(1-factor)

bottom = bottom.astype(np.uint8)

concatenated_results = np.concatenate([top,bottom], axis=0)

cv2.imwrite("results/morph2.jpg",concatenated_results)