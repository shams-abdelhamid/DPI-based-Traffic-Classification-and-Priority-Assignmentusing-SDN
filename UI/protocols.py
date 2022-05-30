import tkinter
from tkinter import Button, Canvas, ttk

#Window & Canvas
def retrieve():
    print(protocols.get())
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


#Protocols
canvas.create_text((screen_width/2), 90, text="Protocols", fill = "black", font = ("Times New Roman", 30))

#Protocols combobox
protocols = ttk.Combobox(window, width = 40)
protocols['values'] = ('Ethernet', 'TCP', 'UDP', 'Ipv4', 'Ipv6', 'SMTP')
protocols.place(relx = 0.3, rely =0.31)
#protocols.current(0)

#Add protocol button
addProtocol = Button(window, text = "Add Protocol", bg = "#74CCE0", 
fg = "white", font = ("Times New Roman", 18), width = 10, height = 1,command=retrieve)
addProtocol.place(relx = 0.5, rely = 0.3)



canvas.pack()
window.mainloop()