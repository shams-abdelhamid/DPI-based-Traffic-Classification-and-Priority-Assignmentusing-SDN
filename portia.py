from cProfile import label
from pydoc import text 
from tkinter import *
from tkinter import ttk
import pip._vendor.requests as requests 

def send():
    r = requests.get('http://127.0.0.1:5000/'+name.get())
    print(r.text)

def flip():
    input = time.get()
    f = open("orders.txt","w")
    f.write(input)
    f.close()

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
host['values'] = ('h1', 'h2')
host.pack()
label = Label(root,text='Set Priority').pack()
priority = Entry(root)
priority.pack()
button = Button(root,text='Test',fg='white',bg='blue',command=flip).pack()
root.mainloop()