from tkinter import *
from PIL import ImageTk, Image
import os

sounds = []
for file in os.listdir("sounds"):
    if file != ".gitkeep":
        sounds.append(file[:-4])

root = Tk()
root.geometry("50x50")
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-transparentcolor", "white")

img = ImageTk.PhotoImage(Image.open("icons/"+sounds[0]+".png"))
label = Label(root, bg="white", text="a", image=img)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()