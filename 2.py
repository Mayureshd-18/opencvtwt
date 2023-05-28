import random
import cv2

img = cv2.imread('assets/cat.jpg',-1)

print(img.shape)
# Prints 3 values height,width,channels
# height - height of image(no. of rows)
# width - no. of columns
# channels - No. of colors used to represent a pixel in the image (BGR)

for i in range(200,301):
    for j in range(img.shape[1]):
        # print(img[i][j])
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

crop = img[100:200, 180:380]
img[200:300, 180:380] = crop
# cv2.imshow("Cropped", crop)


cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

