from tkinter import*
root=Tk()
var=StringVar()
for i in range(2):
    rad= Radiobutton(root,text=str(i),variable=var)
    rad.pack(side=LEFT)
var.set('happy')
root.mainloop()
