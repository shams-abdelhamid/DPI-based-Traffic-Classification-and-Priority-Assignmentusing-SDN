import tkinter
from tkinter import Canvas


window = tkinter.Tk()
window.state('zoomed')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
canvas =  Canvas(window, width=screen_width, height=screen_height)

canvas.create_rectangle(0, 0, screen_width, screen_height, outline = "#6BD5B9", fill="#6BD5B9")
canvas.create_text((screen_width/2, screen_height/2), text="Portia", fill = "white", font = ("Times New Roman", 100))

#TITLE
window.title("Portia")

canvas.pack()
window.mainloop()