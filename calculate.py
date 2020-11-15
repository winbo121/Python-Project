from tkinter import*
import turtle as t
import random

def do(a):
    
    try:
        if a=="=":
        
            entry1.insert(END,"="+str(eval(entry1.get())))
        
        elif a=="C":
            entry1.delete(0,END)
    
        else:
            entry1.insert(END,a)

    except:
        entry1.delete(0,END)
        entry1.insert(END,"오류입니다")


window=Tk()

window.title("계산기")

frame1=Frame(window)

frame1.grid(row=0,column=0,columnspan=2,sticky=W)

label1=Label(frame1,text="계산")

label1.grid(row=0,column=0,sticky=W)

entry1=Entry(frame1,width=35)

entry1.grid(row=1,column=0,sticky=W)

frame2=Frame(window)

frame2.grid(row=1,column=0,sticky=W)



number=["0","1","2","3","4","5","6","7","8","9",".","="]
num=0
for i in range(0,4,1):
    for j in range(0,3,1):
        
        def active(a=number[num]):
            do(a)
            
        Bij=Button(frame2,width=5,text=number[num],command=active)
        Bij.grid(row=i,column=j,sticky=W)
        num=num+1
frame3=Frame(window)

frame3.grid(row=1,column=1,sticky=W)
        
operator=["+","-","*","/","(",")","C"]
oper=0
r=0
c=0
for i in range(0,len(operator),1):
    def active(a=operator[oper]):
        do(a)
    Bi=Button(frame3,width=5,text=operator[oper],command=active)
    Bi.grid(row=r,column=c,sticky=E)
    oper=oper+1
    c=c+1
    if c==2:
        r=r+1
        c=0
