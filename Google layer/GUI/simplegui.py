#simple GUI

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title ("Simple GUI")
root.geometry("500x400")

#kick of the event loop
root.mainloop()

#button
button = Button(root, activeforeground="F1F1F1", photo="buttonimg.png"))
button.pack(side="top")
#button.grid(column=250, row=200)