from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
import time


#643 697 - restartbtn
#292 705 - dino

class DinoBot:
    def __init__(self, replaybtn, dino):
        self.replaybtn = replaybtn
        self.dino = dino

    def restartgame(self):
        pyautogui.click(self.replaybtn)

    def jump(self):
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')

    def grabImage(self):
        box = (self.dino[0] + 35, self.dino[1], self.dino[0] + 75, self.dino[1] + 30)
        image = ImageGrab.grab(box)
        grayimage = ImageOps.grayscale(image)
        a = array(grayimage.getcolors())
        return a.sum()

    def start(self):
        self.restartgame()
        while True:
            print(self.grabImage()) #1477 white




def main():
    bot = DinoBot((643, 697), (292, 705))
    bot.start()

if __name__ == "__main__":
    main()