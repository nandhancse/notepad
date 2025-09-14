from tkinter import*


def submit():
    input=text.get(1.0,END)
    print(input)
window=Tk()
#window.geometry("300x300")
text=Text(window,bg='#ede09d',font=('Ink Free',20),height=8,width=20)
text.pack()
button =Button(window,text='Submit',command=submit)
button.pack()

window.mainloop()
