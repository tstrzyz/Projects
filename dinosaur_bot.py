from PIL import Image, ImageGrab, ImageOps
import sys
import pyautogui
import numpy as np
import time 
class Cordinates():
    dinosaur = (245,400)
    btn = (479,398)
    gamespeedmultiplier = 0
def RestartGame():
    pyautogui.click(Cordinates.btn)      
     
def PressSpace():    
    pyautogui.keyDown("space")
    time.sleep(0.15)
    pyautogui.keyUp("space")
          
def imageGrab():
    box = (Cordinates.dinosaur[0]+(60+Cordinates.gamespeedmultiplier),Cordinates.dinosaur[1],Cordinates.dinosaur[0]+(150+Cordinates.gamespeedmultiplier),Cordinates.dinosaur[1]+30)
    image = ImageGrab.grab(box)             
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())           
    a = sum((sum(a)))           
    Cordinates.gamespeedmultiplier += 0.11  
    
    return(a)
                                 
                   
def main(): 
    pyautogui.keyDown("space")                                          
    RestartGame()             
    while True:            
        imageGrab()         
        if (imageGrab() !=2947):
            pyautogui.keyUp("down")
            PressSpace()
            time.sleep(0.015) 
    sys.exit()                                                                     

main()
