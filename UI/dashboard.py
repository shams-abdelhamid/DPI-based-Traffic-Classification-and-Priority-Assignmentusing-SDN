from cProfile import label
import tkinter
from tkinter import Button, Canvas, Image, PhotoImage

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
canvas.create_text((screen_width/2), 90, text="Dashboard", fill = "black", font = ("Times New Roman", 30))

#Devices connected
canvas.create_text(349, 150, text="Devices Connected", fill = "black", font = ("Times New Roman", 17))

#Images
img = PhotoImage(file = "images/iphonepicc.png")
canvas.create_image(280, 230, image = img)
canvas.create_image(350, 230, image = img)
canvas.create_image(420, 230, image = img)

canvas.create_text(280, 300, text="Iphone 1", fill = "black", font = ("Times New Roman", 12))
canvas.create_text(350, 300, text="Iphone 2", fill = "black", font = ("Times New Roman", 12))
canvas.create_text(420, 300, text="Iphone 3", fill = "black", font = ("Times New Roman", 12))

#Add devices button
addDevices = Button(window, text = "Add Device", bg = "#74CCE0", 
fg = "white", font = ("Times New Roman", 18), width = 10, height = 1)
addDevices.place(relx = 0.6, rely = 0.3)

#Speedometer
canvas.create_text(352, 400, text="Speedometer", fill = "black", font = ("Times New Roman", 17))

#Internet speed button
internetSpeed = Button(window, text = "Internet Speed", bg = "#74CCE0", 
fg = "white", font = ("Times New Roman", 18), width = 12, height = 1)
internetSpeed.place(relx = 0.2, rely = 0.61)

#Automatic optimization button
autoOpti = Button(window, text = "Automatic Optimization", bg = "#74CCE0", 
fg = "white", font = ("Times New Roman", 18), width = 18, height = 1)
autoOpti.place(relx = 0.49, rely = 0.75)




canvas.pack()
window.mainloop()