from tkinter import *
import datetime
from PIL import Image

import keras
from keras import Sequential
from keras.datasets import mnist
import os
from keras import layers
from keras import backend as k
import json
from keras.losses import categorical_crossentropy
import cv2 
from keras.models import model_from_json
from keras.optimizers import Adadelta
import numpy as np


b1 = "up"
xold, yold = None, None

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

def main():
    root = Tk()
    root.title("Canvas Draw")
    drawing_area = Canvas(root,width=400,height=400)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    button4=Button(root,fg="green",text="Save",command=lambda:getter(drawing_area))
    button4.pack(side=RIGHT)
    button4=Button(root,fg="green",text="Clear",command=lambda:delete(drawing_area))
    button4.pack(side=LEFT)
    def delete(widget):
        widget.delete("all")

    def getter(widget):
        import numpy as np
        now = datetime.datetime.now()
        fileName = str(now)
        drawing_area.postscript(file=fileName+ '.eps') 
        # use PIL to convert to PNG 
        img = Image.open(fileName + '.eps') 
        cv_image = np.array(img)
        cv2.imshow('a', cv_image)
        cv_image = cv2.resize(cv_image, (28, 28), interpolation=cv2.INTER_LINEAR)
        cv_image = rgb2gray(cv_image)
        cv_image = cv_image.astype('float32')
        cv_image /= 255
        cv_image = np.reshape(cv_image, (1, 28, 28, 1))
        #cv_image = cv_image[np.newaxis]
        probs = loaded_model.predict(cv_image)
        prediction = probs.argmax(axis=1)
        print(prediction)



        
    root.mainloop()
def b1down(event):
    global b1
    b1 = "down"
def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,width=5,smooth=TRUE)
        xold = event.x
        yold = event.y


json_file = open('model_digit.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model_digit.h5")
loaded_model.compile(loss=categorical_crossentropy, optimizer=Adadelta(),metrics=['accuracy'])


if __name__ == "__main__":
    main()