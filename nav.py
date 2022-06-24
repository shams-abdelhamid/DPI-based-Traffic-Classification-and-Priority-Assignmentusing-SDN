from logging import root
from tkinter import *
from tkinter import ttk
import tkinter as tk

from psutil import net_io_counters

import tk_tools
from tkinter import PhotoImage

from tk_tools.images import rotary_gauge_volt, rotary_scale, rotary_gauge_bar
last_upload, last_download, upload_speed, down_speed = 0, 0, 0, 0


imagelist = {
  'menu': ['menu.png', None],
  'close': ['close.png', None],
}

def get(name):
  if name in imagelist:
    if imagelist[name][1] is None:
      print('loading image:', name)
      imagelist[name][1] = PhotoImage(file=imagelist[name][0])
    return imagelist[name][1]
  return None

color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
btnState = False
current_page = None
class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		#Setup Menu
		#Setup Frame
		# top Navigation bar:

		
		self.geometry('900x620')
		container = tk.Frame(self)

		global topFrame, homeLabel, navRoot
		topFrame = tk.Frame(self, bg=color["orange"])
		topFrame.pack(side="top", fill=tk.X)

		# Header label text:
		homeLabel = tk.Label(topFrame, text="PE", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
		homeLabel.pack(side="right")


		# Navbar button:
		navbarBtn = tk.Button(topFrame, image=get('menu'), bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
		navbarBtn.place(x=10, y=10)

		# setting Navbar frame:
		navRoot = tk.Frame(self, bg="gray17", height=1000, width=300)
		navRoot.place(x=-300, y=0)
		tk.Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

		# set y-coordinate of Navbar widgets:
		y = 80
		# option in the navbar:
		options = ["Profile", "Settings", "Help", "About", "Feedback"]
		# Navbar Option Buttons:
		tk.Button(navRoot, text="Start Page", font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0,command=lambda:self.show_frame(StartPage)).place(x=25, y=80)
		tk.Button(navRoot, text="Bandwidth", font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0,command=lambda:self.show_frame(PageTwo)).place(x=25, y=y+80)
		# Navbar Close Button:
		closeBtn = tk.Button(navRoot, image=get('close'), bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
		closeBtn.place(x=250, y=10)
		
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo):
			frame = F(container, self)
			self.frames[F] = frame
			frame.config(bg="gray17")
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)	
		
	def show_frame(self, context):
		frame = self.frames[context]
		frame.tkraise()

def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

class StartPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		global current_page
		if current_page is not None:
			current_page.pack_forget()

		label = Label(self, text="Start Page")
		label.pack(padx=10, pady=10)
		current_page = label
		label = Label(self,text='welcome to portia').pack()
		label = Label(self,text='Choost Time').pack()
		time = ttk.Combobox(self)
		time['values'] = ('1', '2', '3', '4', '5')
		time.pack()
		label = Label(self,text='Choose Host').pack()
		host = ttk.Combobox(self)
		host.pack()
		label = Label(self,text='Set Priority').pack()
		priority = Entry(self)
		priority.pack()
		button = Button(self,text='Test',fg='white',bg='blue').pack()
		success = Label(self,text='Success')
		success.pack_forget()

		page_one = Button(self, text="Page One", command=lambda:controller.show_frame(PageOne))
		page_one.pack()
		page_two = Button(self, text="Page Two", command=lambda:controller.show_frame(PageTwo))
		page_two.pack()

class PageOne(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		controller.show_frame(StartPage)
		label = Label(self, text="Page One")
		label.pack(padx=10, pady=10)
		
		start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
		start_page.pack()
		page_two = Button(self, text="Page Two", command=lambda:controller.show_frame(PageTwo))
		page_two.pack()

class PageTwo(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		frame2 = self
		label = Label(self, text="Page Two")
		label.pack(padx=10, pady=10)
		# Variables for use in the size() function.
		KB = float(1024)
		MB = float(KB ** 2) # 1,048,576
		GB = float(KB ** 3) # 1,073,741,824
		TB = float(KB ** 4) # 1,099,511,627,776
		def size(B):
			"""Credits: https://stackoverflow.com/a/31631711 (Improved version of it.)"""
			
			B = float(B)
			if B < KB: return f"{B} Bytes"
			elif KB <= B < MB: return f"{B/KB:.2f} KB"
			elif MB <= B < GB: return f"{B/MB:.2f} MB"
			elif GB <= B < TB: return f"{B/GB:.2f} GB"
			elif TB <= B: return f"{B/TB:.2f} TB"

		## Constants
		REFRESH_DELAY = 1500 # Window update delay in ms.

		## Variables


		## Initializing

		label_total_upload_header = Label(self, text = "Total Upload:", font = "Quicksand 12 bold")
		label_total_upload_header.pack()
		label_total_upload = Label(self, text = "Calculating...", font = "Quicksand 12")
		label_total_upload.pack()

		label_total_download_header = Label(self, text = "Total Download:", font = "Quicksand 12 bold")
		label_total_download_header.pack()
		label_total_download = Label(self, text = "Calculating...", font = "Quicksand 12")
		label_total_download.pack()

		label_total_usage_header = Label(self, text = "Total Usage:", font = "Quicksand 12 bold")
		label_total_usage_header.pack()
		label_total_usage = Label(self, text = "Calculating...\n", font = "Quicksand 12")
		label_total_usage.pack()

		label_upload_header = Label(self, text = "Upload:", font = "Quicksand 12 bold")
		label_upload_header.pack()
		label_upload = Label(self, text = "Calculating...", font = "Quicksand 12")
		label_upload.pack()

		label_download_header = Label(self, text = "Download:", font = "Quicksand 12 bold")
		label_download_header.pack()
		label_download = Label(self, text = "Calculating...", font = "Quicksand 12")
		label_download.pack()

		attribution = Label(self, text = "\n~ WaterrMalann ~", font = "Quicksand 11 italic")
		attribution.pack()
		p1 = tk_tools.RotaryScale(self, max_value=100, size=100, unit=' KB',img_data=rotary_gauge_bar)
		p1.pack()

		p2 = tk_tools.RotaryScale(self, max_value=100,
                              size=100,
                              needle_thickness=3,
                              needle_color='black',
                              img_data=rotary_gauge_volt)

		p2.pack()
		# Updating Labels
		def update():
			global last_upload, last_download, upload_speed, down_speed
			counter = net_io_counters()

			upload = counter.bytes_sent
			download = counter.bytes_recv
			total = upload + download

			if last_upload > 0:
				if upload < last_upload:
					upload_speed = 0
				else:
					upload_speed = upload - last_upload

			if last_download > 0:
				if download < last_download:
					down_speed = 0
				else:
					down_speed = download - last_download

			last_upload = upload
			last_download = download
			
			label_total_upload["text"] = f"{size(upload)} ({upload} Bytes)"
			label_total_download["text"] = f"{size(download)} ({download} Bytes)"
			label_total_usage["text"] = f"{size(total)}\n"
			
			label_upload["text"] = size(upload_speed)
			label_download["text"] = size(down_speed)
			f = '%.2f'%float(down_speed/KB)
			b = float(f)
			p1.set_value(b)

			label_total_upload.pack()
			label_total_download.pack()
			label_total_usage.pack()
			label_upload.pack()
			label_download.pack()
			
			frame2.after(REFRESH_DELAY, update)  # reschedule event in refresh delay.

		frame2.after(REFRESH_DELAY, update)
		start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
		start_page.pack()
		page_one = Button(self, text="Page One", command=lambda:controller.show_frame(PageOne))
		page_one.pack()


app = App()
app.mainloop()