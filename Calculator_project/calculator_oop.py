from tkinter import*
import math
class Calculator:
    def __init__(self,root):
        # # functions
        self._f_nbr=None
        self._s_nbr=None
        self._op=None
        self._result=0

        self.root=root

        # place the result text
        self.result_label=Label(self.root,text="",bg="black",fg="white")
        self.result_label.grid(pady=(30,20),row=0,column=0,columnspan=10,sticky="w")
        self.result_label.config(font=("Arial",24,"bold"))

        # buttons
        # place the button in row one
        self.btn_inv=Button(root,text="INV",bg="orange",fg="white",width=5)
        self.btn_inv.grid(row=1,column=0)
        self.btn_inv.config(font=("Arial",14,"bold"))

        
        self.btn_deg=Button(root,text="DEG",bg="orange",fg="white",width=5)
        self.btn_deg.grid(row=1,column=1)
        self.btn_deg.config(font=("Arial",14,"bold"))

        self.btn_fact=Button(root,text="x!",bg="orange",fg="white",width=5)
        self.btn_fact.grid(row=1,column=2,padx=(0,3))
        self.btn_fact.config(font=("Arial",14,"bold"))


        self.btn_clear=Button(root,text="C",bg="orange",fg="white",width=5,command=lambda:self.clear())
        self.btn_clear.grid(row=1,column=3)
        self.btn_clear.config(font=("Arial",14,"bold"))

        self.btn_div=Button(root,text="/",bg="orange",fg="white",width=5,command=lambda: self.get_op("/"))
        self.btn_div.grid(row=1,column=4)
        self.btn_div.config(font=("Arial",14,"bold"))

        self.btn_mul=Button(root,text="*",bg="orange",fg="white",width=5,command=lambda: self.get_op("*"))
        self.btn_mul.grid(row=1,column=5)
        self.btn_mul.config(font=("Arial",14,"bold"))

        self.btn_cross=Button(root,text="AC",bg="orange",fg="white",width=5)
        self.btn_cross.grid(row=1,column=6)
        self.btn_cross.config(font=("Arial",14,"bold"))

        # # place the button in row two
        self.btn_sin=Button(root,text="sin",bg="orange",fg="white",width=5)
        self.btn_sin.grid(row=2,column=0)
        self.btn_sin.config(font=("Arial",14,"bold"))

        self.btn_cos=Button(root,text="cos",bg="orange",fg="white",width=5 )
        self.btn_cos.grid(row=2,column=1)
        self.btn_cos.config(font=("Arial",14,"bold"))

        self.btn_tan=Button(root,text="tan",bg="orange",fg="white",width=5,command=lambda:self.scientific("tan"))
        self.btn_tan.grid(row=2,column=2,padx=(0,3))
        self.btn_tan.config(font=("Arial",14,"bold"))

        
        self.btn_7=Button(root,text=7,bg="orange",fg="white",width=5,command=lambda:self.get_digit(7))
        self.btn_7.grid(row=2,column=3)
        self.btn_7.config(font=("Arial",14,"bold"))

        self.btn_8=Button(root,text=8,bg="orange",fg="white",width=5,command=lambda: self.get_digit(8))
        self.btn_8.grid(row=2,column=4)
        self.btn_8.config(font=("Arial",14,"bold"))

        self.btn_9=Button(root,text=9,bg="orange",fg="white",width=5,command=lambda: self.get_digit(9))
        self.btn_9.grid(row=2,column=5)
        self.btn_9.config(font=("Arial",14,"bold"))

        self.btn_min=Button(root,text="-",bg="orange",fg="white",width=5,command=lambda: self.get_op("-"))
        self.btn_min.grid(row=2,column=6)
        self.btn_min.config(font=("Arial",14,"bold"))

        # # place the button in row three
        self.btn_log1=Button(root,text="ln",bg="orange",fg="white",width=5)
        self.btn_log1.grid(row=3,column=0)
        self.btn_log1.config(font=("Arial",14,"bold"))

        self.btn_log2=Button(root,text="log",bg="orange",fg="white",width=5)
        self.btn_log2.grid(row=3,column=1)
        self.btn_log2.config(font=("Arial",14,"bold"))

        self.btn_power=Button(root,text="x^y",bg="orange",fg="white",width=5,command=lambda: self.get_op("^"))
        self.btn_power.grid(row=3,column=2,padx=(0,3))
        self.btn_power.config(font=("Arial",14,"bold"))


        self.btn_4=Button(self.root,text=4,bg="orange",fg="white",width=5,command=lambda: self.get_digit(4))
        self.btn_4.grid(row=3,column=3)
        self.btn_4.config(font=("Arial",14,"bold"))

        self.btn_5=Button(self.root,text=5,bg="orange",fg="white",width=5,command=lambda: self.get_digit(5))
        self.btn_5.grid(row=3,column=4)
        self.btn_5.config(font=("Arial",14,"bold"))

        self.btn_6=Button(self.root,text=6,bg="orange",fg="white",width=5,command=lambda: self.get_digit(6))
        self.btn_6.grid(row=3,column=5)
        self.btn_6.config(font=("Arial",14,"bold"))

        self.btn_plus=Button(self.root,text="+",bg="orange",fg="white",width=5,command=lambda: self.get_op("+"))
        self.btn_plus.grid(row=3,column=6)
        self.btn_plus.config(font=("Arial",14,"bold"))

        # # place the button in row four
        self.btn_pi=Button(self.root,text="π",bg="orange",fg="white",width=5)
        self.btn_pi.grid(row=4,column=0)
        self.btn_pi.config(font=("Arial",14,"bold"))

        self.btn_root_e=Button(self.root,text="e",bg="orange",fg="white",width=5)
        self.btn_root_e.grid(row=4,column=1,padx=(0,3))
        self.btn_root_e.config(font=("Arial",14,"bold"))

        self.btn_root=Button(self.root,text="√",bg="orange",fg="white",width=5)
        self.btn_root.grid(row=4,column=2,padx=(0,3))
        self.btn_root.config(font=("Arial",14,"bold"))


        self.btn_1=Button(self.root,text=1,bg="orange",fg="white",width=5,command=lambda:self.get_digit(1))
        self.btn_1.grid(row=4,column=3)
        self.btn_1.config(font=("Arial",14,"bold"))

        self.btn_2=Button(self.root,text=2,bg="orange",fg="white",width=5,command=lambda: self.get_digit(2))
        self.btn_2.grid(row=4,column=4)
        self.btn_2.config(font=("Arial",14,"bold"))

        self.btn_3=Button(self.root,text=3,bg="orange",fg="white",width=5,command=lambda: self.get_digit(3))
        self.btn_3.grid(row=4,column=5)
        self.btn_3.config(font=("Arial",14,"bold"))

        self.btn_equal=Button(self.root,text="=",bg="orange",fg="white",width=5,command=lambda: self.get_result())
        self.btn_equal.grid(row=4,column=6)
        self.btn_equal.config(font=("Arial",14,"bold"))

# Row 5
        self.btn_left_bra=Button(self.root,text="(",bg="orange",fg="white",width=5)
        self.btn_left_bra.grid(row=5,column=0)
        self.btn_left_bra.config(font=("Arial",14,"bold"))

        self.btn_right_bra=Button(self.root,text=")",bg="orange",fg="white",width=5)
        self.btn_right_bra.grid(row=5,column=1)
        self.btn_right_bra.config(font=("Arial",14,"bold"))

        self.btn_square=Button(self.root,text="x^2",bg="orange",fg="white",width=5)
        self.btn_square.grid(row=5,column=2,padx=(0,3))
        self.btn_square.config(font=("Arial",14,"bold"))


        self.btn_mod=Button(self.root,text="%",bg="orange",fg="white",width=5,command=lambda:self.get_op("%"))
        self.btn_mod.grid(row=5,column=3)
        self.btn_mod.config(font=("Arial",14,"bold"))

        self.btn_0=Button(self.root,text=0,bg="orange",fg="white",width=5,command=lambda: self.get_digit(0))
        self.btn_0.grid(row=5,column=4)
        self.btn_0.config(font=("Arial",14,"bold"))

        self.btn_dot=Button(self.root,text=".",bg="orange",fg="white",width=5)
        self.btn_dot.grid(row=5,column=5)
        self.btn_dot.config(font=("Arial",14,"bold"))

    # Get the number
    def get_digit(self,nbr):
        print(nbr)
        curr=self.result_label["text"]
        # curr=""
        new=curr+str(nbr)
        self.result_label.config(text=new)

    def get_op(self,oper):
        self._f_nbr=float(self.result_label["text"])
        self._result=self._f_nbr
        self._op=oper
        print("op: ",self._op)
        self.result_label.config(text="")
    


    def get_result(self):
        self._s_nbr=float(self.result_label["text"])
        print(self._f_nbr,self._op,self._s_nbr)
        try:
            if(self._op=="+"):
                self.result_label.config(text=str(self._f_nbr+self._s_nbr))
            elif(self._op=="-"):
                self.result_label.config(text=str(self._f_nbr-self._s_nbr))
            elif(self._op=="*"):
                self.result_label.config(text=str(self._f_nbr*self._s_nbr))
            elif(self._op=="/"):
                self.result_label.config(text=str(self._f_nbr/self._s_nbr))
            elif(self._op=="%"):
                self.result_label.config(text=str(self._f_nbr%self._s_nbr))
            elif(self._op=="^"):
                self.result_label.config(text=str(math.pow(self._f_nbr,self._s_nbr)))

            elif(self._op=="tan"):
                self.result_label.config(text=str(math.tan(self._f_nbr)))
                
        except:
            self.scientific(self._op)


    def scientific(self,op):
        self._f_nbr
        if(op=="tan"):
            print(self._f_nbr)
            self.result_label.config(text=str(math.tan(self._f_nbr)))

    def clear(self):
        self.result_label.config(text="")

    # start main loop
    def start(self):
        self.root.mainloop()


root=Tk()
root.geometry("490x288")
root.title("My Calculator")
root.config(bg="black")
root.resizable(0,0)

cal=Calculator(root)
cal.start()