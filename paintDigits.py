from tkinter import *
import datetime
from PIL import Image
b1 = "up"
xold, yold = None, None

def main():
    root = Tk()
    root.title("Canvas Draw")
    drawing_area = Canvas(root,width=600,height=600)
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
        now = datetime.datetime.now()
        fileName = str(now)
        drawing_area.postscript(file=fileName+ '.eps') 
        # use PIL to convert to PNG 
        img = Image.open(fileName + '.eps') 
        img.save(fileName + '.png', 'png')
        cv_image = np.array(img)
        cv_image.resize([28,28])
        cv_image.reshape([1,28,28])
        

        
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
            event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE)
        xold = event.x
        yold = event.y
if __name__ == "__main__":
    main()