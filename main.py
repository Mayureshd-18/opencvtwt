import cv2

img = cv2.imread('assets/cat.jpg',-1)
# -1, cv2.IMREAD_COLOR: Loads a color image. Any transparency of the image will not be considered
# 0, cv2.IMREAD_GRAYSCALE : Loads an image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED : Loads an image as such including alpha channel ( Includes transparency)

# cv2.resize(img, (100,100))

small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)


cv2.imshow("Image",small)
cv2.waitKey(1000)
cv2.destroyAllWindows()

