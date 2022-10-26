
from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk 
from tkinter import ttk
import time
import tkinter as tk
splash_screen_root = Tk()

width_of_window = 427
height_of_window = 250
screen_width = splash_screen_root.winfo_screenwidth()
screen_height = splash_screen_root.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
splash_screen_root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))



#splash_screen_root.geometry("400x250")
splash_screen_root.title("Network Anomoly Detection")

splash_screen_root.overrideredirect(1)  

width = 500
height = 400

image = Image.open("C:\\Users\\moode\\Desktop\\Picture\\AICYBER.png")
im = image.resize((500,350),Image.ANTIALIAS)
img = ImageTk.PhotoImage(im)
ttk.Label(image=img).grid()


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='lime green')
pb=Progressbar(splash_screen_root,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='indeterminate',)
pb.place(x=-10,y=235)


def PrograssBar(): 

    r=0
    for i in range(100):
        pb['value']=r
        splash_screen_root.update_idletasks()
        time.sleep(0.03)
        r=r+1



def main():

	PrograssBar()
	splash_screen_root.destroy()

	Mainroot = Tk()
	Mainroot.title("Network Anomoly Detection")

	Mainroot.geometry("900x500")


splash_screen_root.after(2000,main)

mainloop()

