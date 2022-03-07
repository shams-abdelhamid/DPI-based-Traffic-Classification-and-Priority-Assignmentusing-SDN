import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu,tearoff=0)

        file_menu.add_command(label="New File")
        file_menu.add_command(label="Open")
        file_menu.add_separator()
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save as...")
        
        combo = ttk.Combobox(values=["UDP","TCP","Ethernet","ISMP","Ipv4","Ipv6"]).pack()
        ttk.Style().configure("TButton", padding=6, relief="flat",
        background="#ccc")
        btn = ttk.Button(text="Add Protocol")
        btn.pack()

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_command(label="About")
        menu.add_command(label="Quit", command=self.destroy)
        self.config(menu=menu)
        
if __name__ == "__main__":
    app = App()
    app.geometry("1000x500+10+20")
    app.mainloop()