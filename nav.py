from logging import root
from tkinter import *
from tkinter import ttk
import tkinter as tk
#from psutil import net_io_counters

#import tk_tools
from tkinter import PhotoImage

#from tk_tools.images import rotary_gauge_volt, rotary_scale, rotary_gauge_bar
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
"blue" : "#74CCE0"}
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
		self.title("Portia")
		
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()

		global topFrame, homeLabel, navRoot
		topFrame = tk.Frame(self, bg=color["blue"])
		topFrame.pack(side="top", fill=tk.X)

		# Header label text:
		homeLabel = tk.Label(topFrame, text="Portia",font=("Quicksand bold",16), bg=color["blue"], fg="white", height=2)
		homeLabel.pack(side="left", padx=50)


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
		options = ["Profile", "Settings", "Help", "About", "Feedback"]
		# Navbar Option Buttons:
		tk.Label(navRoot, text="Portia", font="Quicksand 15", bg=color["blue"],fg="white").place(x = 25, y=15)
		tk.Button(navRoot, text="Dashboard", font="Quicksand 15", bg=color["blue"], fg="white", activebackground="white", activeforeground=color["blue"], bd=0,command=lambda:self.show_frame(PageOneDashboard)).place(x=25, y=80)
		tk.Button(navRoot, text="Predict Priority", font="Quicksand 15", bg=color["blue"], fg="white", activebackground="white", activeforeground=color["blue"], bd=0,command=lambda:self.show_frame(PagePredict)).place(x=25, y=y+80)
		tk.Button(navRoot, text="Bandwidth", font="Quicksand 15", bg=color["blue"], fg="white", activebackground="white", activeforeground=color["blue"], bd=0,command=lambda:self.show_frame(PageTwoBandwidth)).place(x=25, y=y+160)

		# Navbar Close Button:
		closeBtn = tk.Button(navRoot, image=get('close'), bg=color["blue"], activebackground=color["blue"], bd=0, command=switch)
		closeBtn.place(x=250, y=10)
		
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		

		self.frames = {}

		for F in (PagePredict, PageOneDashboard, PageTwoBandwidth):
			frame = F(container, self)
			self.frames[F] = frame
			frame.config(bg="white")
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

class PagePredict(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		global current_page
		if current_page is not None:
			current_page.pack_forget()

		
		label = Label(self, text="Predict Priority", fg = "black", bg = "white", font = ('Quicksand bold',25))
		label.pack(padx=10, pady=10)
		current_page = label
		label = Label(self,text='Choose Time',bg= "white",font=(11)).pack()
		time = ttk.Combobox(self)
		time['values'] = ('1', '2', '3', '4', '5')
		time.pack()
		label = Label(self,text='Choose Host',bg= "white",font=(11)).pack()
		host = ttk.Combobox(self)
		host.pack()
		label = Label(self,text='Set Priority',bg= "white",font=(11)).pack()
		priority = Entry(self)
		priority.pack()
		#white text for space
		Label(self,text='white text',bg="white",fg="white").pack()
		button = Button(self,text='Test',font=('quicksand bold',14),height=1,width=9,fg='white',bg=color['blue']).pack()
		success = Label(self,text='Success')
		success.pack_forget()

		page_one = Button(self, text="Predict Priority",font=('quicksand bold',14),height=1,width=11, bg = color["blue"], fg = "white",command=lambda:controller.show_frame(PagePredict))
		page_one.pack()
		page_two = Button(self, text="Bandwidth",font=('quicksand bold',14),height=1,width=13, bg = color["blue"], fg = "white", command=lambda:controller.show_frame(PageTwoBandwidth))
		page_two.pack()

class PageOneDashboard(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		lambda:controller.show_frame(PageOneDashboard)
		label = Label(self, text="Dashboard", fg = "black", bg = "white", font = ('Quicksand bold',25))
		label.pack(padx=10, pady=10)
		label = Label(self,text='Welcome to Portia!',bg= "white", font =('quicksand',15)).pack()

		#white text to make space
		label = Label(self, text="Devices Connected",bg="white",fg="white").pack()

		#Devices
		label = Label(self, text="Devices Connected",bg="white",font=(11)).pack()

		#Images
		self.img = tk.PhotoImage(file = "images/iphonepicc.png")

		label = Label(self, image = self.img, bg="white").place(x= 320, y=149)
		label = Label(self, image = self.img, bg="white").pack(padx=10,pady=10)
		label = Label(self, image = self.img, bg="white").place(x=475,y=149)
		label = Label(self, text="Device 1", bg="white").place(x= 346, y=273.453)
		label = Label(self, text="Device 2", bg="white").pack(padx=10,pady=10)
		label = Label(self, text="Device 3", bg="white").place(x= 495, y=273.453)

		
		predict_page = Button(self, text="Predict Priority",font=('quicksand bold',14),height=1,width=11, bg = color["blue"], fg = "white", command=lambda:controller.show_frame(PagePredict))
		predict_page.pack()
		page_two = Button(self, text="Bandwidth",font=('quicksand bold',14),height=1,width=13,bg = color["blue"], fg = "white", command=lambda:controller.show_frame(PageTwoBandwidth))
		page_two.pack()

class PageTwoBandwidth(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		frame2 = self
		label = Label(self, text="Bandwidth", fg = "black", bg = "white", font = ('Quicksand bold',25))
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

		label_total_upload_header = Label(self, text = "Total Upload:", bg= "white", font = "Quicksand 12 bold")
		label_total_upload_header.pack()
		label_total_upload = Label(self, text = "Calculating...", bg= "white",font = "Quicksand 12")
		label_total_upload.pack()

		label_total_download_header = Label(self, text = "Total Download:",bg= "white", font = "Quicksand 12 bold")
		label_total_download_header.pack()
		label_total_download = Label(self, text = "Calculating...",bg= "white", font = "Quicksand 12")
		label_total_download.pack()

		label_total_usage_header = Label(self, text = "Total Usage:",bg= "white", font = "Quicksand 12 bold")
		label_total_usage_header.pack()
		label_total_usage = Label(self, text = "Calculating...\n",bg= "white", font = "Quicksand 12")
		label_total_usage.pack()

		label_upload_header = Label(self, text = "Upload:",bg= "white", font = "Quicksand 12 bold")
		label_upload_header.pack()
		label_upload = Label(self, text = "Calculating...", bg= "white",font = "Quicksand 12")
		label_upload.pack()

		label_download_header = Label(self, text = "Download:", bg= "white",font = "Quicksand 12 bold")
		label_download_header.pack()
		label_download = Label(self, text = "Calculating...",bg= "white", font = "Quicksand 12")
		label_download.pack()

		attribution = Label(self, bg= "white", font = "Quicksand 11 italic")
		attribution.pack()
		#p1 = tk_tools.RotaryScale(self, max_value=100, size=100, unit=' KB',img_data=rotary_gauge_bar)
		#p1.pack()

		#p2 = tk_tools.RotaryScale(self, max_value=100,
                            #   size=100,
                            #   needle_thickness=3,
                            #   needle_color='black',
                            #   img_data=rotary_gauge_volt)

		#p2.pack()
		# Updating Labels
		def update():
			global last_upload, last_download, upload_speed, down_speed
			#counter = net_io_counters()

			#upload = counter.bytes_sent
			#download = counter.bytes_recv
			#total = upload + download

			if last_upload > 0:
				#if upload < last_upload:
					upload_speed = 0
				#else:
				#	upload_speed = upload - last_upload

			if last_download > 0:
			#	if download < last_download:
					down_speed = 0
				#else:
				#	down_speed = download - last_download

			#last_upload = upload
			#last_download = download
			
			# label_total_upload["text"] = f"{size(upload)} ({upload} Bytes)"
			# label_total_download["text"] = f"{size(download)} ({download} Bytes)"
			# label_total_usage["text"] = f"{size(total)}\n"
			
			label_upload["text"] = size(upload_speed)
			label_download["text"] = size(down_speed)
			f = '%.2f'%float(down_speed/KB)
			b = float(f)
			#p1.set_value(b)

			label_total_upload.pack()
			label_total_download.pack()
			label_total_usage.pack()
			label_upload.pack()
			label_download.pack()
			
			frame2.after(REFRESH_DELAY, update)  # reschedule event in refresh delay.

		frame2.after(REFRESH_DELAY, update)
		predict_page = Button(self, text="Predict Priority",font=('quicksand bold',14), height=1,width=11, bg=color["blue"], fg='white', command=lambda:controller.show_frame(PagePredict))
		predict_page.pack()
		page_one = Button(self, text="Dashboard",font=('quicksand bold',14),height=1,width=13,bg=color["blue"], fg='white', command=lambda:controller.show_frame(PageOneDashboard))
		page_one.pack()


app = App()
app.mainloop()