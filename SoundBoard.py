from tkinter import *
from PIL import ImageTk, Image
import sounddevice as sd
import soundfile as sf
import keyboard
import os

for i in sd.query_devices():
    if i["name"] == "CABLE Input (VB-Audio Virtual C":
        device = i["index"]
        break

def play():
    data, fs = sf.read("sounds/"+sounds[currentSelected]+".mp3")
    sd.play(data, fs, device=device)
    sd.play(data, fs)

def left():
    global img, currentSelected
    currentSelected -= 1
    if currentSelected < 0:
        currentSelected = len(sounds) - 1
    img = ImageTk.PhotoImage(Image.open("icons/"+sounds[currentSelected]+".png")) 
    label.configure(image=img)

def right():
    global img, currentSelected
    currentSelected += 1
    if currentSelected == len(sounds):
        currentSelected = 0
    img = ImageTk.PhotoImage(Image.open("icons/"+sounds[currentSelected]+".png")) 
    label.configure(image=img)

keyboard.add_hotkey("`", play)
keyboard.add_hotkey("left", left)
keyboard.add_hotkey("right", right)

sounds = []
for file in os.listdir("sounds"):
    if file != ".gitkeep":
        sounds.append(file[:-4])
currentSelected = 0

root = Tk()
root.geometry("50x50")
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-transparentcolor", "white")

img = ImageTk.PhotoImage(Image.open("icons/"+sounds[0]+".png")) # Load the first image
label = Label(root, bg="white", text="a", image=img)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()