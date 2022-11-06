import cv2 as c
import pyautogui as p
import numpy as np
rs = p.size()
fn = input("Please Enter any file name and Path: ")
fps = 15.0
fourcc = c.VideoWriter_fourcc(*"XVID")
output = c.VideoWriter(fn,fourcc,fps,rs)
c.namedWindow("LIve_Recording",c.WINDOW_NORMAL)
c.resizeWindow("LIve_Recording",(600,400))
while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f,c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow('res',f)
    if c.waitKey(1) == ord("q"):
        break
output.releae() 
c.destroyAllWindows() 