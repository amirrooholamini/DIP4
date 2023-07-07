import cv2

room_background = cv2.imread("resources/room_background.jpg")
room_foreground = cv2.imread("resources/room_foreground.jpg")
room_mask = cv2.imread("resources/room_mask.jpg")

top_mask = room_mask.copy()
top_mask[top_mask >= 128] = 255
top_mask[top_mask < 128] = 0

top_mask[top_mask==0] = 1
top_mask[top_mask==255] = 0

top = room_background * top_mask

bottom_mask = 1 - top_mask
bottom = room_foreground * bottom_mask

result = top + bottom

cv2.imwrite("results/virtual_decoration.jpg", result)