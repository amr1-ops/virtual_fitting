import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector
from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Dressing Room")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text = "Select T-Shirt")
        self.labelFrame.grid(column = 1, row = 1, padx = 300, pady = 200)

        self.button_3()
        self.button_4()
        self.button_5()
        self.button_6()

    def button_3(self):
        self.button = ttk.Button(self.labelFrame, text = "gray",command = lambda: ShirtSizes("gray.png"))
        self.button.grid(column = 1, row = 1)
    def button_4(self):
        self.button = ttk.Button(self.labelFrame, text = "pantalon",command = lambda: PantalonSizes("pantalon.png"))
        self.button.grid(column = 2, row =1)
    def button_5(self):
        self.button = ttk.Button(self.labelFrame, text = "mentgreen",command = lambda: ShirtSizes("mentgreen.png"))
        self.button.grid(column = 1, row = 2)
    def button_6(self):
        self.button = ttk.Button(self.labelFrame, text = "babyblue",command = lambda: ShirtSizes("babyblue.png"))
        self.button.grid(column = 2, row = 2)
        
        
cap = cv2.VideoCapture(0)
detector = PoseDetector()


fixedRatio = 450/200 # widthOfShirt/widthOfPoint11to12

def ShirtSizes(ShirtName):
    # imgctr = 0
    while True:
        success, img = cap.read()
        img = detector.findPose(img, draw=False)
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
        
        shirtFolderPath = "data"
        if lmList:
            lm11 = lmList[11][1:3]
            lm12 = lmList[12][1:3]
            lm9 = lmList[9][1:3]
            imgShirt = cv2.imread(os.path.join(shirtFolderPath, ShirtName), cv2.IMREAD_UNCHANGED)
            try:
                vw = int(lm12[0]-60)
                img = cvzone.overlayPNG(img, imgShirt, (vw, lm9[1]+25))
        
            except:
                pass
    
            
        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Image', 800,600)
        cv2.imshow("Image", img)
        
        key = cv2.waitKey(1)
        if key == 27:
            break

def PantalonSizes(PantalonName):
    while True:
        success, img = cap.read()
        img = detector.findPose(img, draw=False)
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
        shirtFolderPath = "assets"
        if lmList:
            lm24 = lmList[24][1:3]
            lm28 = lmList[28][1:3]
            imgShirt = cv2.imread(os.path.join(shirtFolderPath, PantalonName), cv2.IMREAD_UNCHANGED)
            heightOfPantalon = int((lm28[1]-lm24[1]))
            imgShirt = cv2.resize(imgShirt, (imgShirt.shape[1], heightOfPantalon))
    
            try:
                vw = int(lm24[0]-110)
                img = cvzone.overlayPNG(img, imgShirt, (vw, lm24[1]))
    
            except:
                pass
            #########################################
        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Image', 800,600)
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == 27:
            break

##############################################

def main():
    root = Root()
    root.mainloop()
    
    cap.release()
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main() 
