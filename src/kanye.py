from getQuote import Quote
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time

root = Tk()
root.geometry("800x500")


def gif():
    global image
    image = Image.open("src/assets/kanye.gif")
    label = Label(root)
    label.place(x=100, y=100)

    for img in ImageSequence.Iterator(image):
        img = img.resize((300,300))
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        time.sleep(0.1)
        root.update()
    root.after(0, gif)

T = Label(root, wraplength=200)
T.place(x=500, y=100)


def gen():
    res = Quote.getData()
    T.config(text=res)


Button(root, text=" Good Morning Kanye! ", command=gen).place(x=500, y=275)
gif()

root.mainloop()



