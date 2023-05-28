import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# The 0 inside is for specifying the number of webcams. 0 would access the forst, 1 would second, etc...

while True :
    ret, frame = cap.read()
    # ret tells if read is working or not (bool)
    # print(ret)
    width = int(cap.get(3))
    height = int(cap.get(4))


    print(height, width)

    image = np.zeros(frame.shape, np.uint8)

    smaller_frame = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)
    image[:height // 4, :width // 4] = smaller_frame
    image[:height // 4, width//4:width // 2] = smaller_frame
    image[:height // 4, width//2: (width*3) // 4] = smaller_frame
    image[:height // 4, (width*3) // 4:] = smaller_frame

    image[height//4:height // 2, :width // 4] = smaller_frame
    image[height//4:height // 2, width//4:width // 2] = smaller_frame
    image[height//4:height // 2, width//2: (width*3) // 4] = smaller_frame
    image[height//4:height // 2, (width*3) // 4:] = smaller_frame

    image[height // 2:(height*3)//4, :width // 4] = smaller_frame
    image[height // 2:(height*3)//4 , width//4:width // 2] = smaller_frame
    image[height // 2:(height*3)//4, width//2: (width*3) // 4] = smaller_frame
    image[height // 2:(height*3)//4, (width*3) // 4:] = smaller_frame

    image[(height*3)//4:, :width // 4] = smaller_frame
    image[(height*3)//4:, width//4:width // 2] = smaller_frame
    image[(height*3)//4:, width//2: (width*3) // 4] = smaller_frame
    image[(height*3)//4:, (width*3) // 4:] = smaller_frame


    # image[:height // 4, :width // 4] = smaller_frame
    # image[:height // 4, :width // 4] = smaller_frame
    # image[:height // 4, :width // 4] = smaller_frame
    # image[:height // 4, :width // 4] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
# releases the webcam so that other applications can use it.
cv2.destroyAllWindows()