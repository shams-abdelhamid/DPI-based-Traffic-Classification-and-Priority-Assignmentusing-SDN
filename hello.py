import tkinter
from tkinter import BOTH, VERTICAL, Canvas, PanedWindow

window = tkinter.Tk()


#canvas.create_rectangle(30, 10, 120, 80,
  #  outline="#fb0", fill="#fb0")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
#Grey rectangle
canvas =  Canvas(window, width=screen_width, height=screen_height)
#canvas.pack()
canvas.create_rectangle(0, 0, 170, screen_height, outline = "grey", fill="grey")

#TITLE
window.title("Title")
title = tkinter.Label(window, text = "Title",  font=("Times New Roman", 25))

title.place(relx = 0.037, rely = 0.01, anchor = 'nw')
title.config(bg="grey")

page1 = tkinter.Label(window, text = " Page 1",  font=("Times New Roman", 14))
page1.place(relx = 0.01, rely = 0.08, anchor = 'nw')
page1.config(bg="grey")

page2 = tkinter.Label(window, text = " Page 2",  font=("Times New Roman", 14))
page2.place(relx = 0.01, rely = 0.12, anchor = 'nw')
page2.config(bg="grey")

page3 = tkinter.Label(window, text = " Page 3",  font=("Times New Roman", 14))
page3.place(relx = 0.01, rely = 0.16, anchor = 'nw')
page3.config(bg="grey")

page4 = tkinter.Label(window, text = " Page 4",  font=("Times New Roman", 14))
page4.place(relx = 0.01, rely = 0.2, anchor = 'nw')
page4.config(bg="grey")

def pageClick( event ):
    canvas.create_rectangle(170, 0, screen_width, screen_height, outline = "yellow", fill="yellow")
    canvas.pack()    
       
page1.bind( "<Button>", pageClick )
#p1 = PanedWindow()
#p1.pack(fill=BOTH, expand=1)

#left = tkinter.Label(p1, text="Left Panel")
#p1.add(left)

#p2 = PanedWindow(p1, orient=VERTICAL)
#p1.add(p2)

#top = tkinter.Label(p2, text="Top Panel")
#p2.add(top)

#bottom = tkinter.Label(p2, text="Bottom Panel")
#p2.add(bottom)


canvas.pack()
window.mainloop()