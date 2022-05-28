from cProfile import label
from pydoc import text 
from tkinter import *
import pip._vendor.requests as requests 

def send():
    r = requests.get('http://127.0.0.1:5000/'+name.get())
    print(r.text)

def flip():
    f = open("orders.txt","w")
    f.write("1")
    f.close()

root = Tk()

root.title('Portia')
root.geometry('400x400')

label = Label(root,text='welcome to portia').pack()
name = Entry(root)
name.pack()

button = Button(root,text='Test',fg='white',bg='blue',command=flip).pack()
root.mainloop()