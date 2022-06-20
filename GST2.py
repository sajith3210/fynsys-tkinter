from ast import Lambda
from textwrap import fill
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from click import command
import mysql.connector
from tkcalendar import DateEntry


def fun(): #db connection
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='finsystkinter'
    )
    mycursor=mydb.cursor()
# Add tax frontend 
def addtax():
    global addtaxwindow,img
    addtaxwindow=Toplevel(gstwindow)
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
    Label(addtaxwindow,image=img,width=300,height=300,bg="#243e54").place(x=30,y=260)

    Label(addtaxwindow,text='TAX Name' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=280)
    Entry(addtaxwindow,bg='#243e54',fg='white',width=50,textvariable=taxname).place(x=580,y=340,height=30)

    Label(addtaxwindow,text='Description' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=400)
    Entry(addtaxwindow,bg='#243e54',fg='white',width=50,textvariable=description,).place(x=580,y=440,height=30)

    Button(addtaxwindow,bg='#243e54',text="SAVE",font='arial 15',fg='white',width=20,command=addtx).place(x=580,y=500,)

# addtax backend
def addtx():
    fun()
    txname=taxname.get()
    desc=description.get()
    # sql='SELECT * FROM addtax WHERE taxname=%s' #selecting entire table from db,taking taxname nd check the existence
    # val=(txname,)
    # mycursor.execute(sql,val)
    sql="INSERT INTO addtax (taxname,description)  VALUES  (%s,%s)" #Adding values into db
    val=(txname,desc)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Added successfully","Added record successfully")

def gotxpayment():
    global GotTaxWindow ,img
    GotTaxWindow=Toplevel(gstwindow)
    GotTaxWindow.title('Record Payments')
    GotTaxWindow.configure(bg="#2f516f")
    GotTaxWindow.geometry("3600x3600")
    Lbfr1=LabelFrame(GotTaxWindow,width=1400,height=150,bg="#243e54",).place(x=4,y=50)
    Label(GotTaxWindow,text='RECORD PAYMENTS' ,font='arial 25', bg="#243e54" , fg='white').place(x=500,y=80)
    Lbfr2=LabelFrame(GotTaxWindow,width=1200,height=580,bg="#243e54",).place(x=4,y=240)

    img=PhotoImage(file='creditcardbillpayment.PNG')
    Label(GotTaxWindow,image=img,width=400,height=400,bg="white").place(x=30,y=260)  #243e54
    

    global textname,paymentdate,recordamount,recordmemo
    textname=StringVar()
    paymentdate=StringVar()
    recordamount=StringVar()
    recordmemo=StringVar()

    Label(GotTaxWindow,text='Enter text' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=300)
    Entry(GotTaxWindow,bg='#243e54',fg='white',width=50,textvariable=textname).place(x=580,y=340,height=25)

    Label(GotTaxWindow,text='Payment date' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=380)
    # Entry(GotTaxWindow,bg='#243e54',width=50,).place(x=580,y=420)
    cal=DateEntry(GotTaxWindow,selectmode='day',textvariable=paymentdate).place(x=580,y=420,height=25,width=300)


    Label(GotTaxWindow,text='Amount' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=470)
    Entry(GotTaxWindow, bg='#243e54',fg='white', width=50,textvariable=recordamount).place(x=580,y=520,height=25)

    Label(GotTaxWindow,text='Memo' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=560,)
    Entry(GotTaxWindow,bg='#243e54',fg='white', width=50,textvariable=recordmemo).place(x=580,y=590,height=50)

    Button(GotTaxWindow , bg='#673ab7',text="Submit form",font='arial 15',fg='white',width=30,command=gottaxpaymentadd).place(x=580,y=650,)
   

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

def main():  
    global gstwindow               
    gstwindow=Tk()
    gstwindow.configure(bg="#2f516f")
    gstwindow.title('GST')
    gstwindow.geometry("1700x1700")
    Lbfr1=LabelFrame(gstwindow,width=1400,height=150,bg="#243e54",).place(x=4,y=50)
    Label(Lbfr1,text='GST' ,font='arial 25', bg="#243e54" , fg='white').place(x=500,y=80)
    Addtxbtn=Button(Lbfr1,fg='white' , text='Add tax' ,bg="#243e54",padx='10',pady='10', width='7',command=addtax)
    Addtxbtn.place(x=700,y=80)

    #Label frame 2
    Lbfr2=LabelFrame(gstwindow,width=1350,height=550,bg="#243e54").place(x=4,y=260) 
    Label(Lbfr2,text='0.0',font='arial 25', bg="#243e54",fg='white').place(x=500,y=280,)
    Label(Lbfr2,text='Fri Apr 01 2022 - Sat Apr 30 2022',font='arial 12',bg='#243e54',fg='white').place(x=500,y=320)
    Label(Lbfr2,text='0.0',bg='#243e54',fg='white',font='arial 12',).place(x=20,y=350)
    Label(Lbfr2,text='IGST',bg='#243e54',fg='white',font='arial 12',).place(x=20,y=390)

    Label(Lbfr2,font='arial 12' , text='+',bg='#243e54',fg='white', ).place(x=120,y=390)

    Label(Lbfr2, text='0.0',bg='#243e54',fg='white',font='arial 12',).place(x=180,y=350)
    Label(Lbfr2 , text='CGST',bg='#243e54',fg='white',font='arial 12',).place(x=180,y=390)

    Label(Lbfr2,font='arial 12' , text='+',bg='#243e54',fg='white', ).place(x=250,y=390)

    Label(Lbfr2, text='0.0',bg='#243e54',fg='white',font='arial 12',).place(x=310,y=350)
    Label(Lbfr2 , text='CGST',bg='#243e54',fg='white',font='arial 12',).place(x=310,y=390)

    Label(Lbfr2, text='₹ 0.0',bg='#243e54',fg='white',font='arial 12',).place(x=800,y=350)
    Label(Lbfr2 , text='Payable balance',bg='#243e54',fg='white',font='arial 12',).place(x=800,y=390)

    # returntab=Button(gstwindow,bg='#243e54',fg='white',text='Returns',font=('Arial',15),command=rettab)
    # returntab.place(x=30,y=480)
    # paymenttab=Button(gstwindow,bg='#243e54',fg='white',text='Payment history',font=('Arial',15),command='paytab')
    # paymenttab.place(x=115,y=480)
    s=ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab',background='green',width=30)
    s.map('TNotebook',background=[('selected','yellow')])
    nb=ttk.Notebook(gstwindow)

    f1=Frame(nb,width=400,height=240,bg="#243e54")
    nb.add(f1,text='Returns')
    f2=Frame(nb,width=1200,height=180,bg="#1b2f40")
    nb.add(f2,text='Payment history')
    
    #Returns tab
    my_tree=ttk.Treeview(f1)
    
    # DEFINE COLUMN 
    my_tree['columns']=('STARTDATE','END DATE','PAYMENT DUE','ANNUAL DUE','PAYMENTS','BALANCE','STATUS')

    #format our columns
    my_tree.column("#0",width=0,stretch=NO)
    my_tree.column("STARTDATE",anchor=CENTER,width=120,)
    my_tree.column('END DATE',anchor=CENTER,width=120)
    my_tree.column('PAYMENT DUE',anchor=CENTER,width=125)
    my_tree.column('ANNUAL DUE',anchor=CENTER,width=125)
    my_tree.column('PAYMENTS',anchor=CENTER,width=125)
    my_tree.column('BALANCE',anchor=CENTER,width=125)
    my_tree.column('STATUS',anchor=CENTER,width=125)

    #Create Heading
    my_tree.heading("#0",text='',anchor=CENTER)
    my_tree.heading('STARTDATE',text='STARTDATE',anchor=CENTER)
    my_tree.heading('END DATE',text='END DATE',anchor=CENTER)
    my_tree.heading('PAYMENT DUE',text='PAYMENT DUE',anchor=CENTER)
    my_tree.heading('ANNUAL DUE',text='ANNUAL DUE',anchor=CENTER)
    my_tree.heading('PAYMENTS',text='PAYMENTS',anchor=CENTER)
    my_tree.heading('BALANCE',text='BALANCE',anchor=CENTER)
    my_tree.heading('STATUS',text='STATUS',anchor=CENTER)

    #Insert data
    my_tree.insert(parent='',index='end',iid=0,text='',values=('Fri Apr 01 2022','Sat Apr 30 2022','','₹0.0','₹ 0.0','₹ 0.0','open'))
    my_tree.place(x=30,y=50)

    # payment history tab
    my_tree2=ttk.Treeview(f2)
        # DEFINE COLUMN 
    my_tree2['columns']=('DATE','TYPE','TAX PERIOD','AMOUNT','MEMO',)

    #format our columns
    my_tree2.column("#0",width=0,stretch=NO)
    my_tree2.column("DATE",anchor=CENTER,width=170,)
    my_tree2.column('TYPE',anchor=CENTER,width=170)
    my_tree2.column('TAX PERIOD',anchor=CENTER,width=170)
    my_tree2.column('AMOUNT',anchor=CENTER,width=170)
    my_tree2.column('MEMO',anchor=CENTER,width=170)

         #Create Heading
    my_tree2.heading("#0",text='',anchor=CENTER)
    my_tree2.heading('DATE',text='DATE',anchor=CENTER)
    my_tree2.heading('TYPE',text='TYPE',anchor=CENTER)
    my_tree2.heading('TAX PERIOD',text='TAX PERIOD',anchor=CENTER)
    my_tree2.heading('AMOUNT',text='AMOUNT',anchor=CENTER)
    my_tree2.heading('MEMO',text='MEMO',anchor=CENTER)
    my_tree2.place(x=30,y=50)

    #Record payment button
    re=Button(f2,text='Record Payment',fg='white',bg='#1b2f40' ,command=gotxpayment)
    re.place(x=770,y=20,width=110,height=30)
     
    #Note book Place
    nb.place(x=30,y=430)
    
    
    gstwindow.mainloop()     
main()
