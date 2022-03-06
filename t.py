import tkinter
from tkinter import BOTH, VERTICAL, Canvas, PanedWindow


window = tkinter.Tk()


#canvas.create_rectangle(30, 10, 120, 80,
  #  outline="#fb0", fill="#fb0")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
#Grey rectangle
canvas =  Canvas(window, width=screen_width, height=screen_height)

#p1 = PanedWindow(width = 170, height = screen_height, bg= 'grey')
#p1.pack(fill=Y, expand=1)

p1 = PanedWindow(width = 170, height= screen_height, bg="grey")
p1.pack(fill=BOTH, expand=False)

title = tkinter.Label(p1, text="Title", font=("Times New Roman", 25))

title.place(relx = 0.037, rely = 0.01, anchor = 'nw')
p1.add(title)

p2 = PanedWindow(p1, orient=VERTICAL)
p1.add(p2)


#p2 = PanedWindow()
#p1.pack()
canvas.pack()
window.mainloop()
