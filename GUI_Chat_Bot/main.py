# from openai import OpenAI
from tkinter import*
# client = OpenAI(api_key="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")

root=Tk()
root.title("My Chat Bot")
root.config(bg="white")
root.geometry("650x550")
root.resizable(0,0)

def action():
    get_text=input_label.get()
    input_label.delete(0,"end")
#     # Open Ai
#     response = client.completions.create(
#     model="text-davinci-002",
#     prompt=get_text,
#     temperature=1,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
#     )


    # end->
    # result.config(text=response.choices[0].text)


header=Label(root,text="Welcome to my chat bot",bg="white",fg="black",justify="center")
header.grid(padx=(20,20),pady=(20,20),row=0,column=1)
header.config(font=("Arial",24,"bold"))

text_label=Label(root,text="Enter: ",fg="black",bg="white",justify="left",anchor="nw")
text_label.grid(row=1,column=0,padx=(35,0))
text_label.config(font=("Arial",20,"bold"))

input_label=Entry(root,bg="white",fg="black",width=70,highlightthickness=4)
input_label.grid(row=1,column=1)
input_label.config()

btn=Button(root,text=">>",bg="white",fg="black",width=3,command=action)
btn.grid(column=2,row=1,padx=(4,4))
btn.config(font=("Arial",10))


scrol=Scrollbar(root)
scrol.grid(row=2,sticky=S+N)


result=Label(root,text="output:",bg="black",fg="white",anchor="nw",justify="left",wraplength=1000,)
result.grid(padx=(0,0),row=2,column=2,columnspan=10)
result.config(font=('Arial',13),height=20,width=60)


scrol.config(command=result.winfo_y)
root.mainloop()