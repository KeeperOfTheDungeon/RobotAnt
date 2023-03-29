import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk

from RoboView.Gui.InternalWindow.InternalWindow import InternalWindow

#root = Tk()
#frame = Frame(root,borderwidth=2)
#frame.config(highlightbackground = "red", highlightcolor= "red", bg = "GREY") 
#frame.place(height=500, width = 500)
#frame.pack()
#frame1 = Frame(root, height = 100, width = 200, bg = "RED", borderwidth=2)
#frame.place(height=1000, width = 1000, x=10, y=10)


root = ctk.CTk()


entry = ctk.CTkEntry(master=root,
                               placeholder_text="CTkEntry",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#window = InternalWindow(root, 100,100,300,300)
#window2 = InternalWindow(root, 100,100,200,200)

#window.set_min_dimension(100,100)
#window2.set_min_dimension(200,200)

#window.rename("Window 1")
#window2.rename("Window 2")



root.mainloop()

