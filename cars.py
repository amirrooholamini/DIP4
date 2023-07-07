import cv2
import numpy as np

cap = cv2.VideoCapture('resources/cars.mp4')

frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=10)
frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
cv2.imshow('frame', medianFrame)
cv2.waitKey(0)