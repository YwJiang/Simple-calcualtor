from tkinter import*
root=Tk()
var=StringVar()

EN=Entry()
EN.pack()

def fighting():
    print('1')
btn=Button(root,text='Jiang',command= lambda:fighting)

var.set(btn)
root.mainloop()
