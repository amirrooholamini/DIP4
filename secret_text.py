import cv2

source = cv2.imread('resources/a.png', cv2.IMREAD_GRAYSCALE)
key = cv2.imread('resources/b.png', cv2.IMREAD_GRAYSCALE)

source = 255 - source

key[key == 255] = 1

result = source * key
result = 255 - result

cv2.imwrite("results/secret_text.jpg",result)