from tkinter import *

import pyshorteners

root=Tk()
root.title("URL Shortener")
root.geometry("500x500")

def shorten():
    if ent2.get():
        ent2.delete(0, END)

    if ent1.get():
        url=pyshorteners.Shortener().tinyurl.short(ent1.get())
        ent2.insert(END, url)



lbl1=Label(root,text="Enter Link To Shorten",font=("Helvetica",30))
lbl1.pack(pady=20)
ent1=Entry(root,font=("Helvetica",20))
ent1.pack(pady=20)
btn1=Button(root,text="Shorten Link",command=shorten,font=("Helvetica",24))
btn1.pack(pady=20)

lbl2=Label(root,text="Shortened Link",font=("Helvetica",14))
lbl2.pack(pady=50)
ent2=Entry(root,font=("Helvetica",22),justify=CENTER)
ent2.pack(pady=20)
root.mainloop()