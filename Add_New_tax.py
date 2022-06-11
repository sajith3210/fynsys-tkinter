from tkinter import *
addtaxwindow = Tk()
addtaxwindow.title("ADD NEW TAX")
addtaxwindow.geometry("1400x800")
addtaxwindow.configure(bg="#2f516f")
#for connecting a scrollbar to a widget
#1) widget (yscrollcommand = scrollbar.set)
#2.) scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(addtaxwindow)
scrollbar.pack(fill=Y, side=RIGHT)
Lbfr1=LabelFrame(addtaxwindow,width=1200,height=150,bg="#243e54",).place(x=4,y=50)
Label(Lbfr1,text='ADD NEW TAX' ,font='arial 25', bg="#243e54" , fg='white').place(x=500,y=80)

Lbfr2=LabelFrame(addtaxwindow,width=1200,height=380,bg="#243e54",).place(x=4,y=240)
img=PhotoImage(file='TAX.PNG')
Label(Lbfr2,image=img,width=300,height=300,bg="#243e54").place(x=30,y=260)
Label(Lbfr2,text='TAX Name' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=280)

Entry(Lbfr2,bg='#243e54',width=50,).place(x=580,y=340)
Label(Lbfr2,text='Description' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=400)
Entry(Lbfr2,bg='#243e54',width=50,).place(x=580,y=440)
Button(Lbfr2,bg='#243e54',text="SAVE",font='arial 15',fg='white',width=20).place(x=580,y=500)


# #Scrollbar Connect to text widget
# text = Text(addtaxwindow, yscrollcommand = scrollbar.set)
# text.pack(fill = BOTH)
# # scrollbar.config(command= listbox .yview)
# scrollbar.config(command= text .yview)

addtaxwindow.mainloop()