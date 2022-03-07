import tkinter
from tkinter import Button, Canvas, ttk

#Window & Canvas
window = tkinter.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
canvas =  Canvas(window, width=screen_width, height=screen_height)

#Title
window.title("Portia")

#Menu Bar
canvas.create_rectangle(0, 0, screen_width, 50, outline = "#5EABBD", fill="#5EABBD")
canvas.create_text(90, 30, text="Portia", fill = "white", font = ("Times New Roman", 32))

canvas.create_rectangle(0, 50, 180, screen_height - 50, outline = "#74CCE0", fill="#74CCE0")

canvas.create_text(90, 100, text="Dashboard", fill = "white", font = ("Times New Roman", 18))
canvas.create_text(90, 150, text="Timeframe", fill = "white", font = ("Times New Roman", 18))
canvas.create_text(90, 200, text="Devices", fill = "white", font = ("Times New Roman", 18))
canvas.create_text(90, 250, text="Custom", fill = "white", font = ("Times New Roman", 18))

#Protocols
canvas.create_text((screen_width/2), 90, text="Protocols", fill = "black", font = ("Times New Roman", 30))

#Protocols combobox
protocols = ttk.Combobox(window, width = 40)
protocols['values'] = ('Ethernet', 'TCP', 'UDP', 'Ipv4', 'Ipv6', 'SMTP')
protocols.place(relx = 0.3, rely =0.31)
#protocols.current(0)

#Add protocol button
addProtocol = Button(window, text = "Add Protocol", bg = "#74CCE0", 
fg = "white", font = ("Times New Roman", 18), width = 10, height = 1)
addProtocol.place(relx = 0.5, rely = 0.3)



canvas.pack()
window.mainloop()