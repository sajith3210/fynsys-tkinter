from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector
def fun(): #db connection
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='finsystkinter'
    )
    mycursor=mydb.cursor()

def gottaxpaymentadd():
    fun()
    # textname,paymentdate,recordamount,recordmemo
    txtname=textname.get()
    paydate=paymentdate.get()
    recamt=recordamount.get()
    recmemo=recordmemo.get()

    sql="INSERT INTO recordpay (textname,paymentdate,recordamount,recordmemo)  VALUES  (%s,%s,%s,%s)" #Adding values into db
    val=(txtname,paydate,recamt,recmemo)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Added successfully","Tax Payment Added")


def gottax():
    taxpaymentwindow=Tk()
    taxpaymentwindow.configure(bg="#2f516f")
    taxpaymentwindow.title('GST')
    taxpaymentwindow.geometry("3600x3600")

    Lbfr1=LabelFrame(taxpaymentwindow,width=1400,height=150,bg="#243e54",).place(x=4,y=50)
    Label(Lbfr1,text='RECORD PAYMENTS' ,font='arial 25', bg="#243e54" , fg='white').place(x=500,y=80)
    Lbfr2=LabelFrame(taxpaymentwindow,width=1200,height=580,bg="#243e54",).place(x=4,y=240)

    img=PhotoImage(file='creditcardbillpayment.PNG')
    Label(taxpaymentwindow,image=img,width=400,height=400,bg="#243e54").place(x=30,y=260)

    global textname,paymentdate,recordamount,recordmemo
    textname=StringVar()
    paymentdate=StringVar()
    recordamount=IntVar()
    recordmemo=StringVar()

    Label(taxpaymentwindow,text='Enter text' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=300)
    Entry(taxpaymentwindow,bg='#243e54',width=50,textvariable=textname).place(x=580,y=340,height=25)

    Label(taxpaymentwindow,text='Payment date' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=380)
    # Entry(taxpaymentwindow,bg='#243e54',width=50,).place(x=580,y=420)
    cal=DateEntry(taxpaymentwindow,selectmode='day',textvariable=paymentdate).place(x=580,y=420,height=25)


    Label(taxpaymentwindow,text='Amount' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=470)
    Entry(taxpaymentwindow, bg='#243e54',width=50,textvariable=recordamount).place(x=580,y=520,height=25)

    Label(taxpaymentwindow,text='Memo' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=560,)
    Entry(taxpaymentwindow,bg='#243e54',width=50,textvariable=recordmemo).place(x=580,y=590,height=50)

    Button(taxpaymentwindow , bg='#673ab7',text="Submit form",font='arial 15',fg='white',width=30,command=gottaxpaymentadd).place(x=580,y=650,)
    taxpaymentwindow.mainloop() #TBLE NME RECORD PAY

gottax()