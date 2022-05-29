from cProfile import label
from pydoc import text 
from tkinter import *
from tkinter import ttk
import pip._vendor.requests as requests
import os

def send():
    r = requests.get('http://127.0.0.1:5000/'+name.get())
    print(r.text)

def flip():
    input = time.get()
    input2 = host.get()
    input3 = priority.get()
    f = open("sendc.txt","w")
    f.write(input + "\n")
    f.write(input2 + "\n")
    f.write(input3 + "\n")
    f.close()
    success.pack()

root = Tk()

root.title('Portia')
root.geometry('400x400')

label = Label(root,text='welcome to portia').pack()
label = Label(root,text='Choost Time').pack()
time = ttk.Combobox(root)
time['values'] = ('1', '2', '3', '4', '5')
time.pack()
label = Label(root,text='Choose Host').pack()
host = ttk.Combobox(root)
os.chdir("../../../../mininet")
with open('hosts.txt',"r") as flfile:
            row = flfile.readlines()
            print(type(row))
            stri=[]
            for st in row:
                stri.append(st.strip())
os.chdir("../ryu/ryu/app/DPI-based-Traffic-Classification-and-Priority-Assignmentusing-SDN")
host['values'] = stri
host.pack()
label = Label(root,text='Set Priority').pack()
priority = Entry(root)
priority.pack()
button = Button(root,text='Test',fg='white',bg='blue',command=flip).pack()
success = Label(root,text='Success')
success.pack_forget()
root.mainloop()