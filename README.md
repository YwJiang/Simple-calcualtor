# Simple-calcualtor
# This is a calculator making homework using Python
from tkinter import *
from math import*
root = Tk()
root.title('计算器')

frm0 = Frame(root)
frm1 = Frame(root)
frm0.pack(side=TOP,expand=YES,fill=BOTH)
frm1.pack(side=TOP,expand=YES,fill=BOTH)

var=StringVar()
var.set(0)
numlabel=Label(frm0,textvariable=var)
numlabel.config(height=3,width=20,anchor='e',font=('consolas',13))
numlabel.pack()

Out_result=''

def get_input(num):
    global Out_result
    Out_result= Out_result+str(num)
    var.set(Out_result)

def cal(sign):
    global Out_result
    Out_result=Out_result+sign
    var.set(Out_result)

def back():
    global Out_result
    Str=[]
    for i in Out_result:
        
        Str.append(i)
    del Str[len(Str)-1]
    change_form=''
    for i in Str:
        change_form=change_form+i
    Out_result=change_form
    var.set(Out_result)

def clear():
    global Out_result
    Out_result=''
    var.set(0)
    
def equal():
    global Out_result
    Out_result=str(eval(Out_result))
    var.set(Out_result)
    
#数字    
btn9= Button(frm1, text='9',command=lambda:get_input(9))
btn9.grid(row=1,column=2,ipadx=11,ipady=11)

btn8= Button(frm1, text='8',command=lambda:get_input(8))
btn8.grid(row=1,column=1,ipadx=11,ipady=11)

btn7= Button(frm1, text='7',command=lambda:get_input(7))
btn7.grid(row=1,column=0,ipadx=11,ipady=11)

btn4= Button(frm1, text='4',command=lambda:get_input(4))
btn4.grid(row=2,column=0,ipadx=11,ipady=11)

btn5= Button(frm1, text='5',command=lambda:get_input(5))
btn5.grid(row=2,column=1,ipadx=11,ipady=11)

btn6= Button(frm1, text='6',command=lambda:get_input(6))
btn6.grid(row=2,column=2,ipadx=11,ipady=11)

btn1= Button(frm1, text='1',command=lambda:get_input(1))
btn1.grid(row=3,column=0,ipadx=11,ipady=11)

btn2= Button(frm1, text='2',command=lambda:get_input(2))
btn2.grid(row=3,column=1,ipadx=11,ipady=11)

btn3= Button(frm1, text='3',command=lambda:get_input(3))
btn3.grid(row=3,column=2,ipadx=11,ipady=11)

btn0= Button(frm1, text='0',command=lambda:get_input(0))
btn0.grid(row=4,column=0,columnspan=2,ipadx=34,ipady=10)

#符号
btnright0= Button(frm1, text='.',command=lambda:cal('.'))
btnright0.grid(row=4,column=2,ipadx=11,ipady=11)

btnright9= Button(frm1, text='/',command=lambda:cal('/'))
btnright9.grid(row=1,column=3,ipadx=11,ipady=11)

btnright6= Button(frm1, text='*',command=lambda:cal('*'))
btnright6.grid(row=2,column=3,ipadx=11,ipady=11)

btnright3= Button(frm1, text='-',command=lambda:cal('-'))
btnright3.grid(row=3,column=3,ipadx=11,ipady=11)

btnright9= Button(frm1, text='+',command=lambda:cal('+'))
btnright9.grid(row=4,column=3,ipadx=9,ipady=11)

#操作

btnback= Button(frm1, text='<-',command=lambda:back())
btnback.grid(row=0,column=0,ipadx=9,ipady=10)

btnclean= Button(frm1, text='c',command=lambda:clear())
btnclean.grid(row=0,column=1,ipadx=31,ipady=10,columnspan=2)

btnequal= Button(frm1, text='=',command=lambda:equal())
btnequal.grid(row=0,column=3,ipadx=9,ipady=10)

root.mainloop()
