from tkinter import*
from math import*
root=Tk()
root.title('calculator')
frm1=Frame(root)
frm2=Frame(root)
frm1.pack(side=TOP)
frm2.pack(side=TOP)
var=StringVar()
var.set(0)
lbl=Label(frm1,textvariable=var).pack()
lbl.config(height=3,width=20,anchor='e',font=('consolas',13))
out_string=''
def num_out(num):
    global out_string
    out_string=num
    var.set(outstring)
def sign_out(sign):
    global out_string
    out_string=out_string+sign
    var.set(out_string)
def back():
    global out_string
    List=[]
    string_len=len(out_string)
    for i in out_string:
        List.append(i)
    del List[string_len-1]
    out_string=''
    for i in List:
        out_string=out_string+i
    var.set(out_string)
def clear():
    global out_string
    out_string=''
    var.set(0)
def cal():
    global out_string
    var.set(eval(out_string))
btn_list=[]
for i in range(1,10):
    btn[i]=button(frm2, text='%s'%i,command=lambda:get_input(i))
    if i%3==0:
        btn[i].grid(row=(i/3-1),column=1,ipadx=10,ipady=10)
    elif i%3==1:
        btn[i].grid(row=((i+1)/3-1),column=2,ipadx=10,ipady=10)
    else:
        btn[i].grid(row=((i+2)/3-1),column=2,ipadx=10,ipady=10)
root.mainloop()
        
    
    
    
        
