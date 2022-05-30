import tkinter
from tkinter import NW, TOP, Button, Canvas, Image, PhotoImage

#Window & Canvas
window = tkinter.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
canvas =  Canvas(window, width=screen_width, height=screen_height)

#Title
window.title("Portia")
window.state('zoomed')
#Menu Bar
canvas.create_rectangle(0, 0, screen_width, 50, outline = "#5EABBD", fill="#5EABBD")
canvas.create_text(90, 30, text="Portia", fill = "white", font = ("Times New Roman", 32))

canvas.create_rectangle(0, 50, 200, screen_height - 50, outline = "#74CCE0", fill="#74CCE0")

dashboard_btn = tkinter.Button(canvas, text = 'Dashboard', bg = "#74CCE0", fg = "white",
font = ("Times New Roman", 18), width = 10, height = 1, borderwidth=0)
dashboard_btn.place(x = 20, y =100)

timeframe_btn = tkinter.Button(canvas, text = 'Timeframe', bg = "#74CCE0", fg = "white",
font = ("Times New Roman", 18), width = 10, height = 1, borderwidth=0)
timeframe_btn.place(x = 20, y =140)

devices_btn = tkinter.Button(canvas, text = 'Devices', bg = "#74CCE0", fg = "white",
font = ("Times New Roman", 18), width = 10, height = 1, borderwidth=0)
devices_btn.place(x = 20, y =180)

protocols_btn = tkinter.Button(canvas, text = 'Custom Protocols', bg = "#74CCE0", fg = "white",
font = ("Times New Roman", 18), width = 13, height = 1, borderwidth=0)
protocols_btn.place(x = 20, y =220)

contactus_btn = tkinter.Button(canvas, text = 'Contact Us', bg = "#74CCE0", fg = "white",
font = ("Times New Roman", 18), width = 10, height = 1, borderwidth=0)
contactus_btn.place(x = 20, y =600)

#Dashboard
canvas.create_text((screen_width/2)+40, 90, text="Contact Us", fill = "black", font = ("Times New Roman", 30))

#Submit button
submit = Button(window, text = "Submit", bg = "#74CCE0", 
fg = "white", font = ("Times New Roman", 18), width = 10, height = 1)
submit.place(relx = 0.49, rely = 0.75)

name = tkinter.Entry(window) 
canvas.create_window(((screen_width - 180)/4)+230, 200, window=name, width = 250, height = 25)
name.insert(0, "Name")

email = tkinter.Entry(window) 
canvas.create_window(((screen_width - 180)/2)+330, 200, window=email, width = 250, height = 25)
email.insert(0, "Email")

message = tkinter.Entry (window) 
canvas.create_window((screen_width/2)+40, 400, window=message, width = 500, height = 250)
message.insert(1, "Message")


canvas.pack()
window.mainloop()