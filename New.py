from ast import Lambda
from itertools import count
from textwrap import fill
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import os 

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
    Entry(addtaxwindow,bg='#243e54',width=50,textvariable=taxname,fg='white').place(x=580,y=340,height=30)
    Label(addtaxwindow,text='Description' ,font='arial 15', bg="#243e54" , fg='white').place(x=580,y=400)
    Entry(addtaxwindow,bg='#243e54',width=50,textvariable=description,fg='white').place(x=580,y=440,height=30)
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
 
def delete(tableid): #Delete data from addtax table
    fun()
    sql='DELETE FROM addtax WHERE addtaxid=%s' #fetching
    val=(tableid,)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Delete',' Delete raw successfully') 

def editordelete(): #Edit data from addtax table
    fun()
    global editscreen ,txname,description ,taxid,taxdeleteid
    editscreen=Toplevel(taxwindow)
    editscreen.title('Edit Add tax table')
    editscreen.geometry('1400x1400')
    editscreen.configure(bg='#2f516f')
    taxid=IntVar()
    txname=StringVar()
    description=StringVar()
    taxdeleteid=IntVar()
    LabelFrame(editscreen,bg='#598ed5' , width=1200,height=300).place(x=10,y=150)
    Label(editscreen,text='Edit  data from the table',bg='#243e54',fg='white').place(x=200,y=200,width=730,height=30)

    Label(editscreen,text='choose tax id',bg='#243e54',fg='white').place(x=200,y=250,width=200)
    cb=ttk.Combobox(editscreen,textvariable=taxid)
    mycursor.execute('SELECT addtaxid FROM addtax')
    cb.place(x=430,y=250)
    cblist=list()  #create list combobox
    for addtax in mycursor:
        for j in range(0,len(addtax)):
            val=addtax[j]
            cblist.append(val)
            cb['values']=cblist
  
    Label(editscreen,text='Tax Name',bg='#243e54',fg='white').place(x=200,y=300,width=200)
    Entry(editscreen,bg='#243e54',fg='white',textvariable=txname).place(x=430,y=300,width=500)

    Label(editscreen,text='Description',bg='#243e54',fg='white').place(x=200,y=350,width=200)
    Entry(editscreen,bg='#243e54',fg='white',textvariable=description).place(x=430,y=350,width=500) 
    Button(editscreen,text='Edit', width=10,bg="#243e54", fg='white',font=('Arial,20'),command=ed).place(x=200,y=400,width=730) 

    LabelFrame(editscreen,bg='#598ed5' , width=1200,height=170).place(x=10,y=460)
    Label(editscreen,text='Delete  data from the table',bg='#243e54',fg='white').place(x=200,y=480,width=730,height=30)
    Label(editscreen,text='Choose delete id',bg='#243e54',fg='white').place(x=200,y=520,width=200)
    cbdelete=ttk.Combobox(editscreen,textvariable=taxdeleteid)
    cbdelete.place(x=420,y=520)
    cbdellist=list()
    mycursor.execute('SELECT addtaxid FROM addtax')
    for dte in mycursor:
        for j in range(0,len(dte)):
            val=dte[j]
            cbdellist.append(val)
            cbdelete['values']=cblist
    Button(editscreen,text='Delete', width=10,bg="#243e54", fg='white',font=('Arial,20'),command=dele).place(x=200,y=550,width=730) 

def ed():
    fun()
    global newtxname, newdescription,newtaxid
    newtaxid=taxid.get()
    newtxname=txname.get()
    newdescription=description.get()
    if newtxname =="" and newdescription == "" and newtaxid=="":
        Label(editscreen,text='Please provide data into the  textbox',fg='red',font=('Arial,20')).place(x=200,y=400,width=730)
    else:
        sql='UPDATE addtax  SET taxname=%s , description=%s where addtaxid=%s'
        val=(newtxname,newdescription,newtaxid)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo('Edited','Edited Add tax table successfully')

def dele():
    fun()
    global deltaxid
    deltaxid=taxdeleteid.get()
    if deltaxid=="":
        Label(editscreen,text='Please provide data into the  textbox',fg='red',font=('Arial,20')).place(x=200,y=400,width=730)
    else:
        sql='DELETE from addtax where addtaxid=%s'
        val=(deltaxid,)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo('Delete','Deleted from the Add tax table data successfully')



# def refresh():
#     taxwindow.destroy()
#     os.system('New.py')

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
    Button(Lbfr2,text='Edit or Delete', width=10,bg="#243e54", fg='white',font=('Arial,20'),command=editordelete).place(x=800,y=350,width=120,height=40)
   
    Button(Lbfr2,text='Add TAX' ,  font='arial 15', bg="#243e54" , fg='white',command=addtaxx).place(x=1000,y=350)
    # Button(Lbfr2,text='Refresh' ,font='arial 15', bg="#243e54" , fg='white',command=refresh).place(x=900,y=350)
    Label(Lbfr2,text='TAX ID' ,font='arial 15', bg="#243e54" , fg='white').place(x=45,y=400)
    Label(Lbfr2,text='TAX NAME' ,font='arial 15', bg="#243e54" , fg='white').place(x=300,y=400)
    Label(Lbfr2,text='DESCRIPTION' ,font='arial 15', bg="#243e54" , fg='white').place(x=600,y=400)
    # Label(Lbfr2,text='ACTION' ,font='arial 15', bg="#243e54" , fg='white').place(x=900,y=400)

    mycursor.execute("SELECT * FROM addtax")
    
    xax=[45,300,600]
    yax=500 

    btnxs=900 
    btnyx=500
    count=0
    for addtax in mycursor:    
        print('addtax value is',addtax)    
        for j in range(len(addtax)):
            e = Entry(taxwindow, width=10,bg="#243e54", fg='white',font=('Arial,20')) 
            for xa in xax:
                if j==0 and xa==45:
                    tableid=addtax[j]
                    e.place(x=xa,y=yax,width=200)
                    
           
                if j==1 and xa==300:
                    e.place(x=xa,y=yax,width=200)
                if j==2 and xa==600:
                    e.place(x=xa,y=yax,width=200)
                # e.place(x=xa, y=yax,width=400) 
      
            e.insert(END, addtax[j])    
            print(addtax[j])
        
        btnyx=btnyx+35 
        yax=yax+35 
  
    taxwindow.mainloop()
main()