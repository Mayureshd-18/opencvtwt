import cv2
import mediapipe as mp
import time

class HandDetector():

    def __init__(self,mode=False,maxHands = 2,model_complexity=1, detectionConf=0.5, trackConf=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = 1
        self.detectionConf=detectionConf
        self.trackConf=trackConf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.model_complexity,self.detectionConf,self.trackConf)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, frame,draw = True):

        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        # print(results.multi_hand_landmarks)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handLms,self.mpHands.HAND_CONNECTIONS,
                                          self.mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2 ),
                                          self.mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2))

                # for id, lm in enumerate(handLms.landmark):
                #     h, w, c = frame.shape
                #     cx, cy = int(lm.x*w), int(lm.y*h)
                #
                #
                #     print(id, cx, cy)

        return frame




def main():
    cap = cv2.VideoCapture(0)

    detector = HandDetector()

    while True:
        ret, frame = cap.read()
        

        detector.findHands(frame)
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord('q'):
            break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()