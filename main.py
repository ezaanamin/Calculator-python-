from tkinter import *
import tkinter.font as font
import  parser
root=Tk()
root.title("Calculator")
root.geometry("250x260")
i=0
e = Entry(root)
e.grid(row=0,column=0,columnspan=10)
font1=font.Font(size=15)
def get_varaible(num):
    global i
    e.insert(i,num)
    i+=1

def delete():
    e.delete(0,END)

def undo():
    entire_string=e.get()
    if(len(entire_string)):
        new_string=entire_string[:-1]
        delete()
        e.insert(0,new_string)


def caluclate():
    entire_result=e.get()
    try:
        a=parser.expr(entire_result).compile()
        result=eval(a)
        delete()
        e.insert(0,result)
    except Exception:
        delete()
        e.insert(0,"Error")

def get_varaible1(num1):
    global i
    length=len(num1)
    e.insert(i,num1)
    i+=length



Button1=Button(root,text=1,command=lambda :get_varaible(1))
Button1.grid(row=1,column=0)
Button1['font']=font1
Button1=Button(root,text=2,command=lambda :get_varaible(2))
Button1.grid(row=1,column=1)
Button1['font']=font1
Button1=Button(root,text=3,command=lambda :get_varaible(3))
Button1.grid(row=1,column=2)
Button1['font']=font1

Button1=Button(root,text=4,command=lambda :get_varaible(4))
Button1.grid(row=2,column=0)
Button1['font']=font1
Button1=Button(root,text=5,command=lambda :get_varaible(5))
Button1.grid(row=2,column=1)
Button1['font']=font1
Button1=Button(root,text=6,command=lambda :get_varaible(6))
Button1.grid(row=2,column=2)
Button1['font']=font1

Button1=Button(root,text=7,command=lambda :get_varaible(7))
Button1.grid(row=3,column=0)
Button1['font']=font1
Button1=Button(root,text=8,command=lambda :get_varaible(8))
Button1.grid(row=3,column=1)
Button1['font']=font1
Button1=Button(root,text=9,command=lambda :get_varaible(9))
Button1.grid(row=3,column=2)
Button1['font']=font1

Button2=Button(root,text="+",command=lambda :get_varaible1("+"))
Button2.grid(row=1,column=3)
Button2['font']=font1
Button2=Button(root,text="/",command=lambda :get_varaible1("/"))
Button2.grid(row=1,column=3)
Button2['font']=font1
utton2=Button(root,text="-",command=lambda :get_varaible1("-"))
Button2.grid(row=2,column=3)
Button2['font']=font1
Button2=Button(root,text="*",command=lambda :get_varaible1("*"))
Button2.grid(row=3,column=3)
Button2['font']=font1

Button1=Button(root,text="AC",command=lambda :delete())
Button1.grid(row=4,column=0)
Button1['font']=font1
Button1=Button(root,text=0,command=lambda :get_varaible(0))
Button1.grid(row=4,column=1)
Button1['font']=font1
Button1=Button(root,text="=",command=lambda :caluclate())
Button1.grid(row=4,column=2)
Button1['font']=font1

Button1['font']=font1
Button1=Button(root,text="/",command=lambda :get_varaible1("/"))
Button1.grid(row=4,column=3)
Button1['font']=font1

Button1['font']=font1
Button1=Button(root,text="pie",command=lambda :get_varaible1("*3.142"))
Button1.grid(row=1,column=5)
Button1['font']=font1

Button1['font']=font1
Button1=Button(root,text="%")
Button1.grid(row=2,column=5)
Button1['font']=font1

Button1['font']=font1
Button1=Button(root,text="(",command=lambda :get_varaible1("("))
Button1.grid(row=3,column=5)
Button1['font']=font1
Button1['font']=font1
Button1=Button(root,text="exp",command=lambda :get_varaible1("**"))
Button1.grid(row=4,column=5)
Button1['font']=font1

Button1['font']=font1
Button1=Button(root,text="<-",command=lambda :undo())
Button1.grid(row=1,column=6)
Button1['font']=font1

Button1['font']=font1
Button1=Button(root,text="x!")
Button1.grid(row=2,column=6)
Button1['font']=font1
Button1['font']=font1
Button1=Button(root,text=")",command=lambda :get_varaible1(")"))
Button1.grid(row=3,column=6)
Button1['font']=font1
Button1['font']=font1
Button1=Button(root,text="^2",command=lambda :get_varaible1("**2"))
Button1.grid(row=4,column=6)
Button1['font']=font1

root.mainloop()
