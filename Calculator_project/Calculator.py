from tkinter import*
import math as m
root=Tk()
root.geometry("490x288")
root.title("My Calculator")
root.config(bg="black")
root.resizable(0,0)
# functions
f_nbr=None
s_nbr=None
op=None
def get_digit(nbr):
    curr=result_label["text"]
    new=curr+str(nbr)
    result_label.config(text=new)

def get_op(oper):
    global f_nbr,op
    f_nbr=float(result_label["text"])
    op=oper
    result_label.config(text="")
    print(f_nbr,op)

def get_result():
    global f_nbr,op,s_nbr
    try:
        s_nbr=float(result_label["text"])
        print(f_nbr,op,s_nbr)

        if op=="+":
            result_label.config(text=str(f_nbr+s_nbr))
        elif op=="-":
            result_label.config(text=str(f_nbr - s_nbr))
        elif op=="*":
            result_label.config(text=str(f_nbr * s_nbr))
        elif op=="%":
            result_label.config(text=str(f_nbr%s_nbr))
        elif op=="/":
            if s_nbr ==0:
                result_label.config(text="can't divisible by zero")
            else:
                result_label.config(text=str(f_nbr / s_nbr))
        elif(op=="^"):
            result_label.config(text=str(m.pow(f_nbr,s_nbr)))

        else:
            scientific(op)
    except:
        curr=result_label["text"]
        for i in curr:
            if i=="":
                result_label.config(text="0")
            else:
                result_label.config(text=curr)

def clear():
    result_label.config(text="")

def redo():
    curr=result_label["text"]
    for i in curr:
        if(i==""):
            result_label.config(text="")
        else:
            result_label.config(text=curr[:-1])

def scientific(oper):
    global f_nbr,s_nbr,op
    f_nbr=float(result_label["text"])
    op=oper
    result_label.config(text="")
    # print(f_nbr,op)

    if(op=="sin"):
        result_label.config(text=str(round(m.sin(f_nbr),3)))
    elif (op == "cos"):
        result_label.config(text=str(round(m.cos(f_nbr), 3)))
    elif (op == "tan"):
        result_label.config(text=str(round(m.tan(f_nbr), 3)))
    elif (op == "π"):
        result_label.config(text=str(round(m.pi*(f_nbr), 3)))
    elif (op == "√"):
        result_label.config(text=str(round(m.sqrt(f_nbr), 3)))
    elif (op == "log"):
        result_label.config(text=str(round(m.log(f_nbr), 3)))
    elif (op == "!"):
        result_label.config(text=str(m.factorial(int(f_nbr))))
    elif(op=="^2"):
        result_label.config(text=str(f_nbr**2))
    elif (op == "e"):
        result_label.config(text=str(m.e*f_nbr))
# functions

# place the result text
result_label=Label(root,text="",bg="black",fg="white")
result_label.grid(pady=(30,20),row=0,column=0,columnspan=10,sticky="w")
result_label.config(font=("Arial",24,"bold"))

# place the button in row one
btn_inv=Button(root,text="INV",bg="orange",fg="white",width=5)
btn_inv.grid(row=1,column=0)
btn_inv.config(font=("Arial",14,"bold"))

btn_deg=Button(root,text="DEG",bg="orange",fg="white",width=5)
btn_deg.grid(row=1,column=1)
btn_deg.config(font=("Arial",14,"bold"))

btn_fact=Button(root,text="x!",bg="orange",fg="white",width=5,command=lambda:scientific("!"))
btn_fact.grid(row=1,column=2,padx=(0,3))
btn_fact.config(font=("Arial",14,"bold"))


btn_clear=Button(root,text="C",bg="orange",fg="white",width=5,command=clear)
btn_clear.grid(row=1,column=3)
btn_clear.config(font=("Arial",14,"bold"))

btn_div=Button(root,text="/",bg="orange",fg="white",width=5,command=lambda:get_op("/"))
btn_div.grid(row=1,column=4)
btn_div.config(font=("Arial",14,"bold"))

btn_mul=Button(root,text="*",bg="orange",fg="white",width=5,command=lambda:get_op("*"))
btn_mul.grid(row=1,column=5)
btn_mul.config(font=("Arial",14,"bold"))

btn_cross=Button(root,text="AC",bg="orange",fg="white",width=5,command=lambda:redo())
btn_cross.grid(row=1,column=6)
btn_cross.config(font=("Arial",14,"bold"))


# place the button in row two
btn_sin=Button(root,text="sin",bg="orange",fg="white",width=5,command=lambda: scientific("sin"))
btn_sin.grid(row=2,column=0)
btn_sin.config(font=("Arial",14,"bold"))

btn_cos=Button(root,text="cos",bg="orange",fg="white",width=5 ,command=lambda :scientific("cos"))
btn_cos.grid(row=2,column=1)
btn_cos.config(font=("Arial",14,"bold"))

btn_tan=Button(root,text="tan",bg="orange",fg="white",width=5,command=lambda :scientific("tan"))
btn_tan.grid(row=2,column=2,padx=(0,3))
btn_tan.config(font=("Arial",14,"bold"))


btn_7=Button(root,text="7",bg="orange",fg="white",width=5,command=lambda: get_digit(7))
btn_7.grid(row=2,column=3)
btn_7.config(font=("Arial",14,"bold"))

btn_8=Button(root,text="8",bg="orange",fg="white",width=5,command=lambda: get_digit(8))
btn_8.grid(row=2,column=4)
btn_8.config(font=("Arial",14,"bold"))

btn_9=Button(root,text="9",bg="orange",fg="white",width=5,command=lambda: get_digit(9))
btn_9.grid(row=2,column=5)
btn_9.config(font=("Arial",14,"bold"))

btn_min=Button(root,text="-",bg="orange",fg="white",width=5,command=lambda:get_op("-"))
btn_min.grid(row=2,column=6)
btn_min.config(font=("Arial",14,"bold"))


# place the button in row three
btn_log1=Button(root,text="ln",bg="orange",fg="white",width=5,command=lambda :scientific("log"))
btn_log1.grid(row=3,column=0)
btn_log1.config(font=("Arial",14,"bold"))

btn_log2=Button(root,text="log",bg="orange",fg="white",width=5,command=lambda :scientific("log"))
btn_log2.grid(row=3,column=1)
btn_log2.config(font=("Arial",14,"bold"))

btn_power=Button(root,text="x^y",bg="orange",fg="white",width=5,command=lambda :scientific("^"))
btn_power.grid(row=3,column=2,padx=(0,3))
btn_power.config(font=("Arial",14,"bold"))


btn_4=Button(root,text="4",bg="orange",fg="white",width=5,command=lambda: get_digit(4))
btn_4.grid(row=3,column=3)
btn_4.config(font=("Arial",14,"bold"))

btn_5=Button(root,text="5",bg="orange",fg="white",width=5,command=lambda: get_digit(5))
btn_5.grid(row=3,column=4)
btn_5.config(font=("Arial",14,"bold"))

btn_6=Button(root,text="6",bg="orange",fg="white",width=5,command=lambda: get_digit(6))
btn_6.grid(row=3,column=5)
btn_6.config(font=("Arial",14,"bold"))

btn_plus=Button(root,text="+",bg="orange",fg="white",width=5,command=lambda:get_op("+"))
btn_plus.grid(row=3,column=6)
btn_plus.config(font=("Arial",14,"bold"))


# place the button in row four
btn_pi=Button(root,text="π",bg="orange",fg="white",width=5,command=lambda: scientific("π"))
btn_pi.grid(row=4,column=0)
btn_pi.config(font=("Arial",14,"bold"))

btn_e=Button(root,text="e",bg="orange",fg="white",width=5,command=lambda:scientific("e"))
btn_e.grid(row=4,column=1)
btn_e.config(font=("Arial",14,"bold"))

btn_root=Button(root,text="√",bg="orange",fg="white",width=5,command=lambda:scientific("√"))
btn_root.grid(row=4,column=2,padx=(0,3))
btn_root.config(font=("Arial",14,"bold"))


btn_1=Button(root,text="1",bg="orange",fg="white",width=5,command=lambda: get_digit(1))
btn_1.grid(row=4,column=3)
btn_1.config(font=("Arial",14,"bold"))

btn_2=Button(root,text="2",bg="orange",fg="white",width=5,command=lambda: get_digit(2))
btn_2.grid(row=4,column=4)
btn_2.config(font=("Arial",14,"bold"))

btn_3=Button(root,text="3",bg="orange",fg="white",width=5,command=lambda: get_digit(3))
btn_3.grid(row=4,column=5)
btn_3.config(font=("Arial",14,"bold"))

btn_equal=Button(root,text="=",bg="orange",fg="white",width=5,command=get_result)
btn_equal.grid(row=4,column=6)
btn_equal.config(font=("Arial",14,"bold"))

# place the button in row five
btn_left_bra=Button(root,text="(",bg="orange",fg="white",width=5)
btn_left_bra.grid(row=5,column=0)
btn_left_bra.config(font=("Arial",14,"bold"))

btn_right_bra=Button(root,text=")",bg="orange",fg="white",width=5)
btn_right_bra.grid(row=5,column=1)
btn_right_bra.config(font=("Arial",14,"bold"))

btn_square=Button(root,text="x^2",bg="orange",fg="white",width=5,command=lambda:scientific("^2"))
btn_square.grid(row=5,column=2,padx=(0,3))
btn_square.config(font=("Arial",14,"bold"))


btn_mod=Button(root,text="%",bg="orange",fg="white",width=5,command=lambda: get_op("%"))
btn_mod.grid(row=5,column=3)
btn_mod.config(font=("Arial",14,"bold"))

btn_0=Button(root,text="0",bg="orange",fg="white",width=5,command=lambda: get_digit(0))
btn_0.grid(row=5,column=4)
btn_0.config(font=("Arial",14,"bold"))

btn_dot=Button(root,text=".",bg="orange",fg="white",width=5)
btn_dot.grid(row=5,column=5)
btn_dot.config(font=("Arial",14,"bold"))

root.mainloop()
