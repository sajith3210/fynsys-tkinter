from ast import Lambda
from textwrap import fill
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

def fun(): #db connection
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='finsystkinter'
    )
    mycursor=mydb.cursor()

def addtaxx():
    global addtaxwindow ,img
    addtaxwindow=Toplevel(taxwindow)
    addtaxwindow.title("ADD NEW TAX")
    addtaxwindow.geometry("1400x800")
    global taxname , description
    taxname=StringVar()
    description=StringVar()
    addtaxwindow.configure(bg="#2f516f")
    Lbfr1=LabelFrame(addtaxwindow,width=1200,height=150,bg="#243e54",).place(x=4,y=50)
    Label(addtaxwindow,text='ADD NEW TAX' ,font='arial 25', bg="#243e54" , fg='white').place(x=500,y=80)
    Lbfr2=LabelFrame(addtaxwindow,width=1200,height=380,bg="#243e54",).place(x=4,y=240)
    img=PhotoImage(file='TAX.PNG')
    Label(addtaxwindow,image=img,width=300,height=300,).place(x=30,y=260)
    Label(addtaxwindow,text='TAX Name' ,font='arial 15', bg="#243e54" , fg='white',).place(x=580,y=280)
    Entry(addtaxwindow,bg='#243e54',width=50,textvariable=taxname).place(x=580,y=340)
    Label(addtaxwindow,text='Description' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=400)
    Entry(addtaxwindow,bg='#243e54',width=50,textvariable=description).place(x=580,y=440)
    Button(addtaxwindow,bg='#243e54',text="SAVE",font='arial 15',fg='white',width=20,command=addtx).place(x=580,y=500,)

# addtax backend
def addtx():
    fun()
    txname=taxname.get()
    desc=description.get()
    # sql='SELECT * FROM addtax WHERE taxname=%s' #selecting entire table from db,taking taxname nd check the existence
    # val=(txname,)
    # mycursor.execute(sql,val)
    sql="INSERT INTO addtax (taxname,description) values (%s,%s)" #Adding values into db
    val=(txname,desc)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Added successfully","Added record successfully")

def main():
    fun()
    global taxwindow
    taxwindow=Tk()
    taxwindow.title('New')
    taxwindow.geometry("15000x1000")
    taxwindow.configure(bg="#2f516f")
    Lbfr1=LabelFrame(taxwindow,width=1250,height=150,bg="#243e54",).place(x=30,y=50)
    Label(Lbfr1,text='TAX' ,font='arial 25', bg="#243e54" , fg='white').place(x=500,y=80)

    Lbfr2=LabelFrame(taxwindow,width=1250,height=550,bg="#243e54",).place(x=30,y=300)
    Button(Lbfr2,text='Add TAX' ,font='arial 15', bg="#243e54" , fg='white',command=addtaxx).place(x=1000,y=350)
    Label(Lbfr2,text='TAX ID' ,font='arial 15', bg="#243e54" , fg='white').place(x=45,y=400)
    Label(Lbfr2,text='TAX NAME' ,font='arial 15', bg="#243e54" , fg='white').place(x=300,y=400)
    Label(Lbfr2,text='DESCRIPTION' ,font='arial 15', bg="#243e54" , fg='white').place(x=600,y=400)

    mycursor.execute("SELECT * FROM addtax")
    xax=[45,300,600]
    yax=500 
    for addtax in mycursor: 
        
        for j in range(len(addtax)):
            e = Entry(taxwindow, width=10,bg="#243e54", fg='white',font=('Arial,20')) 
            for xa in xax:
                if j==0 and xa==45:
                    e.place(x=xa,y=yax,width=200)
                if j==1 and xa==300:
                    e.place(x=xa,y=yax,width=200)
                if j==2 and xa==600:
                    e.place(x=xa,y=yax,width=200)
                # e.place(x=xa, y=yax,width=400) 
            e.insert(END, addtax[j])    
            print(addtax[j])
        # i=i+1
        yax=yax+35
    taxwindow.mainloop()
main()