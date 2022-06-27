from logging import root
import os
import datetime
import time
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
from psutil import net_io_counters
import requests

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

color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101",
"blue" : "#74CCE0", "lghtgray": "#f0f0f0"}
btnState = False
current_page = None
class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		#Setup Menu
		#Setup Frame
		# top Navigation bar:

		verd = tkFont.Font(family="Georgia",size=36,weight="bold")
		self.geometry('900x620')
		container = tk.Frame(self)
		self.title("Portia")
		
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()

		global topFrame, homeLabel, navRoot
		topFrame = tk.Frame(self, bg=color["blue"])
		topFrame.pack(side="top", fill=tk.X)

		# Header label text:
		homeLabel = tk.Label(topFrame, text="Portia",font=("Quicksand bold",16), bg=color["blue"], fg="white", height=2)
		homeLabel.pack(side="left", padx=50)
		self.original = Image.open('images/logo.png')
		resized = self.original.resize((60, 60),Image.ANTIALIAS)

		self.img = ImageTk.PhotoImage(resized)
		logo = tk.Label(topFrame, image=self.img, bg=color["blue"], fg="white", width="60",height="60")
		logo.pack(side="right", padx=50)


		# Navbar button:
		navbarBtn = tk.Button(topFrame, image=get('menu'), bg=color["blue"], activebackground=color["blue"], bd=0, padx=20, command=switch)
		navbarBtn.place(x=10, y=10)

		# setting Navbar frame:
		navRoot = tk.Frame(self, bg=color["blue"], height=1000, width=300)
		navRoot.place(x=-300, y=0)
		tk.Label(navRoot,font="Bahnschrift 15", bg=color["blue"], fg="blue", height=2, width=300, padx=20).place(x=0, y=0)

		# set y-coordinate of Navbar widgets:
		y = 80
		# option in the navbar:
		# Navbar Option Buttons:
		tk.Label(navRoot, text="Portia", font=verd, bg=color["blue"],fg="white").place(x = 25, y=15)
		tk.Button(navRoot, text="Dashboard", font="Quicksand 15", bg=color["blue"], fg="white", activebackground="white", activeforeground=color["blue"], bd=0,command=lambda:self.show_frame(PageOneDashboard)).place(x=25, y=100)
		tk.Button(navRoot, text="Testing Flow", font="Quicksand 15", bg=color["blue"], fg="white", activebackground="white", activeforeground=color["blue"], bd=0,command=lambda:self.show_frame(PageFlow)).place(x=25, y=y+100)
		tk.Button(navRoot, text="Bandwidth", font="Quicksand 15", bg=color["blue"], fg="white", activebackground="white", activeforeground=color["blue"], bd=0,command=lambda:self.show_frame(PageTwoBandwidth)).place(x=25, y=y+180)
		tk.Button(navRoot, text="Predict Priority", font="Quicksand 15", bg=color["blue"], fg="white", activebackground="white", activeforeground=color["blue"], bd=0,command=lambda:self.show_frame(PagePredict)).place(x=25, y=y+260)

		# Navbar Close Button:
		closeBtn = tk.Button(navRoot, image=get('close'), bg=color["blue"], activebackground=color["blue"], bd=0, command=switch)
		closeBtn.place(x=250, y=10)
		
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		

		self.frames = {}

		for F in (PagePredict, PageOneDashboard, PageTwoBandwidth,PageFlow):
			frame = F(container, self)
			self.frames[F] = frame
			frame.config(bg=color["lghtgray"])
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(PageOneDashboard)	
		
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
        homeLabel.config(bg=color["blue"])
        topFrame.config(bg=color["blue"])

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        homeLabel.config(bg=color["blue"])
        topFrame.config(bg=color["blue"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

os.chdir("../../../../mininet")
with open('nodesmap.txt',"r") as flfile:
	row = flfile.readlines()
	names=[]
	macs=[]
	for st in row:
		line = st.strip().split()
		names.append(line[1])
		macs.append(line[0])
os.chdir("../ryu/ryu/app/DPI-based-Traffic-Classification-and-Priority-Assignmentusing-SDN")
class PagePredict(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		global current_page
		if current_page is not None:
			current_page.pack_forget()
		def send_flow(priority):
			f = open("FL.txt","w")
			f.write("5")
			input = str(datetime.datetime.now())
			input2_p = device.get()
			input2 = macs[names.index(input2_p)]
			input3 = str(priority)
			f = open("sendc.txt","w")
			f.write(input + "\n")
			f.write(input2 + "\n")
			f.write(input3 + "\n")
			f.close()
		now = datetime.datetime.now()
		days={'Saturday':0,'Sunday':1,'Monday':2,'Tuesday':3,'Wednesday':4,'Thursday':5,'Friday':6}
		hour = time.strftime("%I:%M")
		def predict():
			inp = device.get()[-1]
			r = requests.post('http://127.0.0.1:5000/api',json={'device_id':inp,'day':days[now.strftime("%A")],'start_time':hour,'server':server.get()})
			res = int(r.text)
			prio_max = 6550
			data_max = 5
			new_prio = round((prio_max / data_max) * res)
			print(new_prio)
			send_flow(new_prio)

		helv36 = tkFont.Font(family="Georgia",size=36,weight="bold")
		label = Label(self, text="Predict Priority", fg = "black", bg=color["lghtgray"], font = helv36)
		label.pack(padx=10, pady=10)
		current_page = label
		label = Label(self,text='Choose Device',bg=color["lghtgray"],font=(11)).pack()
		device = ttk.Combobox(self)
		server = ttk.Combobox(self)
		os.chdir("../../../../mininet")
		with open('nodesmap.txt',"r") as flfile:
			row = flfile.readlines()
			names=[]
			device_macs=[]
			hosts=[]
			hosts_mac=[]
			for st in row[0:6]:
				line = st.strip().split()
				names.append(line[1])
				device_macs.append(line[0])
			for st in row[7:12]:
				line=st.strip().split()
				hosts.append(line[1])
				hosts_mac.append(line[0])
		os.chdir("../ryu/ryu/app/DPI-based-Traffic-Classification-and-Priority-Assignmentusing-SDN")
		device['values'] = names
		device.pack()
		label = Label(self,text='Choose Server',bg=color["lghtgray"],font=(11)).pack()
		server['values'] = hosts
		server.pack()
		#white text for space
		Label(self,text='white text',bg=color["lghtgray"],fg="white").pack()
		button = Button(self,text='Predict',font=('quicksand bold',14),height=1,width=9,fg='white',bg=color['blue'],command=predict).pack()
		success = Label(self,text='Success')
		success.pack_forget()

		page_one = Button(self, text="Predict Priority",font=('quicksand bold',14),height=1,width=11, bg = color["blue"], fg = "white",command=lambda:controller.show_frame(PagePredict))
		page_one.pack()
		page_two = Button(self, text="Bandwidth",font=('quicksand bold',14),height=1,width=13, bg = color["blue"], fg = "white", command=lambda:controller.show_frame(PageTwoBandwidth))
		page_two.pack()

class PageFlow(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		global current_page
		if current_page is not None:
			current_page.pack_forget()
		def flip():
			f = open("FL.txt","w")
			f.write("5")
			input = time.get()
			input2_p = host.get()
			input2 = macs[names.index(input2_p)]
			input3 = priority.get()
			f = open("sendc.txt","w")
			f.write(input + "\n")
			f.write(input2 + "\n")
			f.write(input3 + "\n")
			f.close()
			success.pack()

		helv36 = tkFont.Font(family="Georgia",size=36,weight="bold")
		label = Label(self, text="Testing Flow", fg = "black", bg=color["lghtgray"], font = helv36)
		label.pack(padx=10, pady=10)
		current_page = label
		label = Label(self,text='Choose Time',bg=color["lghtgray"],font=(11)).pack()
		time = ttk.Combobox(self)
		time['values'] = ('1', '2', '3', '4', '5')
		time.pack()
		label = Label(self,text='Choose Host',bg=color["lghtgray"],font=(11)).pack()
		host = ttk.Combobox(self)
		host['values'] = names
		host.pack()
		label = Label(self,text='Set Priority',bg=color["lghtgray"],font=(11)).pack()
		priority = Entry(self)
		priority.pack()
		#white text for space
		Label(self,text='white text',bg=color["lghtgray"],fg="white").pack()
		button = Button(self,text='Test',font=('quicksand bold',14),height=1,width=9,fg='white',bg=color['blue'],command=flip).pack()
		success = Label(self,text='Success')
		success.pack_forget()


class PageOneDashboard(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		helv36 = tkFont.Font(family="Georgia",size=36,weight="bold")
		seg = tkFont.Font(family="Segeo Script",size=26)
		lambda:controller.show_frame(PageOneDashboard)
		label = Label(self, text="Dashboard", fg = "black", bg=color["lghtgray"], font = helv36)
		label.pack(padx=10, pady=10)
		label = Label(self,text='Welcome to Portia!',bg=color["lghtgray"], font =seg).pack()

		#white text to make space
		label = Label(self, text="Devices Connected",bg=color["lghtgray"],fg=color["lghtgray"]).pack()

		#Devices
		label = Label(self, text="Devices Connected",bg=color["lghtgray"],font=(11)).pack()

		#Images
		self.img = tk.PhotoImage(file = "images/iphonepicc.png")

		label = Label(self, image = self.img, bg=color["lghtgray"]).place(x= 220, y=183)
		label = Label(self, image = self.img, bg=color["lghtgray"]).pack(padx=10,pady=10)
		label = Label(self, image = self.img, bg=color["lghtgray"]).place(x=413,y=183)
		label = Label(self, text="Device 1", bg=color["lghtgray"]).place(x= 241, y=304)
		label = Label(self, text="Device 2", bg=color["lghtgray"]).pack(padx=10,pady=10)
		label = Label(self, text="Device 3", bg=color["lghtgray"]).place(x= 439, y=304)

		
		predict_page = Button(self, text="Predict Priority",font=('quicksand bold',14),height=1,width=11, bg = color["blue"], fg = "white", command=lambda:controller.show_frame(PagePredict))
		predict_page.pack()
		page_two = Button(self, text="Bandwidth",font=('quicksand bold',14),height=1,width=13,bg = color["blue"], fg = "white", command=lambda:controller.show_frame(PageTwoBandwidth))
		page_two.pack()

class PageTwoBandwidth(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		frame2 = self
		helv36 = tkFont.Font(family="Georgia",size=36,weight="bold")
		label = Label(self, text="Bandwidth Meter", fg = "black", bg=color["lghtgray"], font = helv36)
		label.grid(row = 0, column = 1,rowspan=2,columnspan=2, sticky = W, padx= 20 ,pady = 20)
		# Variables for use in the size() function.
		KB = float(1024)
		MB = float(KB ** 2) # 1,048,576
		GB = float(KB ** 3) # 1,073,741,824
		TB = float(KB ** 4) # 1,099,511,627,776
		def size(B):

			
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

		label_total_upload_header = Label(self, text = "Total Upload:", bg=color["lghtgray"], font = "Quicksand 12 bold")
		label_total_upload_header.grid(row = 2, column = 0, sticky = W, pady = 2)
		label_total_upload = Label(self, text = "Calculating...", bg=color["lghtgray"],font = "Quicksand 12")
		label_total_upload.grid(row = 2, column = 1, sticky = W, pady = 2)

		label_total_download_header = Label(self, text = "Total Download:",bg=color["lghtgray"], font = "Quicksand 12 bold")
		label_total_download_header.grid(row = 3, column = 0, sticky = W, pady = 2)
		label_total_download = Label(self, text = "Calculating...",bg=color["lghtgray"], font = "Quicksand 12")
		label_total_download.grid(row = 3, column = 1, sticky = W, pady = 2)

		label_total_usage_header = Label(self, text = "Total Usage:",bg=color["lghtgray"], font = "Quicksand 12 bold")
		label_total_usage_header.grid(row = 4, column = 0, sticky = W, pady = 2)
		label_total_usage = Label(self, text = "Calculating...\n",bg=color["lghtgray"], font = "Quicksand 12")
		label_total_usage.grid(row = 4, column = 1, sticky = W, pady = 2)

		label_upload_header = Label(self, text = "Upload Speed:",bg=color["lghtgray"], font = "Quicksand 12 bold")
		label_upload_header.grid(row = 5, column = 0, sticky = W, pady = 2)
		label_upload = Label(self, text = "Calculating...", bg=color["lghtgray"],font = "Quicksand 12")
		label_upload.grid(row = 5, column = 1, sticky = W, pady = 2)

		label_download_header = Label(self, text = "Download Speed:", bg=color["lghtgray"],font = "Quicksand 12 bold")
		label_download_header.grid(row = 6, column = 0, sticky = W, pady = 2)
		label_download = Label(self, text = "Calculating...",bg=color["lghtgray"], font = "Quicksand 12")
		label_download.grid(row = 6, column = 1, sticky = W, pady = 2)

		attribution = Label(self, bg= "white", font = "Quicksand 11 italic")
		attribution.grid(row = 6, column = 0, sticky = W, pady = 2)
		p1 = tk_tools.RotaryScale(self, max_value=100, size=200, bg=color["lghtgray"],unit=' KB/s',img_data=rotary_gauge_bar)
		p1.grid(row = 2, column = 2,
       columnspan = 1, rowspan = 5, padx = 150, pady = 20)

	
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

			label_total_upload.grid(row = 2, column = 1, sticky = W, pady = 2)
			label_total_download.grid(row = 3, column = 1, sticky = W, pady = 2)
			label_total_usage.grid(row = 4, column = 1, sticky = W, pady = 2)
			label_upload.grid(row = 5, column = 1, sticky = W, pady = 2)
			label_download.grid(row = 6, column = 1, sticky = W, pady = 2)
			
			frame2.after(REFRESH_DELAY, update)  # reschedule event in refresh delay.

		frame2.after(REFRESH_DELAY, update)



app = App()
app.mainloop()