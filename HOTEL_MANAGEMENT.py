from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import datetime
from datetime import date
from time import strftime
from PIL import ImageTk, Image
import sqlite3
conn=sqlite3.connect("set your database")  #CONNECTING DATABASE FILE
cur=conn.cursor()
def checkin():   #CHECKIN MODULE
    def alarm():
        x=sn.get()
        h=timer.get()
        gi=no_of_days.get()
        g=gi-1
        tday=datetime.date.today()
        tom=tday+datetime.timedelta(days=g)
        formate="insert into Time(Sno,time,nextday)values({a1},'{b1}','{c1}')"
        sql=formate.format(a1=x,b1=h,c1=tom)
        res=cur.execute(sql)
        cur.execute("commit")
    def call():
        x=sn.get()
        formate="select bedtype from cusdetail where (sno={a1})"
        sql=formate.format(a1=x)
        cur.execute(sql)
        res=cur.fetchone()
        t=res[0]
        if(t=="single"):
            cur.execute("select singlebed from counter")
            a=cur.fetchone()
            i=a[0]
            i=i-1
            formate="update counter set singlebed={a1}"
            sql=formate.format(a1=i)
            res=cur.execute(sql)
            cur.execute("commit")
        elif(t=="double"):
            cur.execute("select doublebed from counter")
            a=cur.fetchone()
            i=a[0]
            i=i-1
            formate="update counter set doublebed={a1}"
            sql=formate.format(a1=i)
            res=cur.execute(sql)
            cur.execute("commit")
    def enterdetails(x,y,z,v,u,p,o,g,h):
           try:
                  formate="insert into cusdetail(sno,name,contno,Email,Homeplace,bedtype,dateofentry,daysengaged,checkintime) values ({a1},'{b1}',{c1},'{d1}','{e1}','{f1}','{g1}',{h1},'{i1}')"
                  sql=formate.format(a1=x,b1=y,c1=z,d1=v,e1=u,f1=p,g1=o,h1=g,i1=h)
                  cur.execute(sql)
                  cur.execute("commit")
                  h1.config(text="DATA ENTERED SUCCESSFULLY!")
                  call()
                  alarm()
           except:
               messagebox.showinfo(title="Alert",message=str(x) + "is already booked give another slno")
    def temp():
       x=sn.get()
       y=nam.get()
       z=con_no.get()
       v=mail.get()
       u=homeplace.get()
       p=bedtype.get()
       o=date.get()
       g=no_of_days.get()
       h=timer.get()
       if((y=="")or(v=="")or(u=="")or(p=="")or(h=="")):
            messagebox.showinfo(title="Alert",message="Pls fill all details!")
       else:
            enterdetails(x,y,z,v,u,p,o,g,h)
    def datee():
        a=datetime.date.today()
        ll6.insert(0,a)
        B3.config(state=DISABLED)
        ll6.config(state=DISABLED)
    def timm():
        a=strftime('%H:%M:%S')
        e8.insert(0,a)
        B4.config(state=DISABLED)
        e8.config(state=DISABLED)
    nam=StringVar()
    con_no=IntVar()
    mail=StringVar()
    homeplace=StringVar()
    bedtype=StringVar()
    no_of_days=IntVar()
    sn=IntVar()
    date=StringVar()
    timer=StringVar()
    F3=Frame(bg="mint cream")
    F3.place(x=0,y=0,width="1600",height="1000")
    l1=Label(F3,text="Full name------->",bg="mint cream",font=("Arial",20))
    l2=Label(F3,text="Contact no----->",bg="mint cream",font=("Arial",20))
    l3=Label(F3,text="E-mail----------->",bg="mint cream",font=("Arial",20))
    l4=Label(F3,text="Home Place---->",bg="mint cream",font=("Arial",20))
    l5=Label(F3,text="Bed type-------->",bg="mint cream",font=("Arial",20))
    l6=Label(F3,text="Date of checkin-->",bg="mint cream",font=("Arial",20))
    l7=Label(F3,text="Days engaged--->",bg="mint cream",font=("Arial",20))
    l8=Label(F3,text="Sl.no------------->",bg="mint cream",font=("Arial",20))
    l9=Label(F3,text="Checkin time-->",bg="mint cream",font=("Arial",20))
    l10=Label(F3,text="Click button to store--->",bg="mint cream",bd=10,font=("Arial",20))
    h1=Label(F3,text="",bg="mint cream",bd=10,font=("Arial",20))
    l1.place(x=200,y=100)
    l2.place(x=200,y=150)
    l3.place(x=200,y=200)
    l4.place(x=200,y=250)
    l5.place(x=200,y=300)
    l6.place(x=200,y=350)
    l7.place(x=200,y=400)
    l8.place(x=200,y=450)
    l9.place(x=200,y=500)
    l10.place(x=200,y=610)
    h1.place(x=200,y=680)
    B=Button(F3,text="Menu page",bd=5,bg="ivory",command=start)
    B.place(x=0,y=85)
    e1=Entry(F3,textvariable=nam,bd=10)
    e2=Entry(F3,textvariable=con_no,bd=10)
    e3=Entry(F3,textvariable=mail,bd=10)
    e4=Entry(F3,textvariable=homeplace,bd=10)
    e5=ttk.Combobox(F3,textvariable=bedtype,width=20)
    e5['values']=("single","double")
    e5.current()
    ll6=Entry(F3,textvariable=date,bd=10)
    e6=Entry(F3,textvariable=sn,bd=10)
    e7=Entry(F3,textvariable=no_of_days,bd=10)
    e8=Entry(F3,textvariable=timer,bd=10)
    e1.place(x=400,y=100)
    e2.place(x=400,y=150)
    e3.place(x=400,y=200)
    e4.place(x=400,y=250)
    e5.place(x=400,y=310)
    e6.place(x=400,y=450)
    ll6.place(x=430,y=350)
    e7.place(x=420,y=400)
    e8.place(x=400,y=500)
    B2=Button(F3,text="Click to enter detail!",bd=5,width=15,height=2,bg="aquamarine",command=temp)
    B2.place(x=500,y=610)
    B3=Button(F3,text="Click to get date",bd=5,width=15,height=1,command=datee,bg="aquamarine")
    B3.place(x=580,y=350)
    B4=Button(F3,text="Click to get time",bd=5,width=15,height=1,command=timm,bg="aquamarine")
    B4.place(x=550,y=500)
    #mn=Label(F3,image=bk)
    #mn.place(x=0,y=80)
    n=Label(F3,text="WELCOME TO HOTEL KAAVYA",width=100,fg="purple",bg="lavender",font=("Gigi",40))
    n.place(x=-800,y=0)
    def time():
        t_s=strftime('%H:%M:%S%p\n%x\n%a')
        llr.config(text=t_s)
        llr.after(1000,time)
    ll=Label(F3,bg="gold")
    ll.place(x=710,y=100)
    llr=Label(F3,font=("Bold",20),bg="gold")
    llr.place(x=710,y=100)
    time()
def checkout():            #CHECKOUT MODULE
    def amount():
        try:
          x=no.get()
          formate="select daysengaged,bedtype from cusdetail where (sno={a1})"
          sql=formate.format(a1=x)
          res=cur.execute(sql)
          a=res.fetchmany()
          for i in a:
            day=i[0]
            ty=i[1]
          if(ty=="single"):
              l2.config(text="RS="+str(day*4500)+" to be pay!!!")
              return day*4500
          elif(ty=="double"):
              l2.config(text="RS="+str(day*8000)+" to be pay!!!")
              return day*8000
        except:
             messagebox.showinfo(title="Alert",message="Slno is not in record pls checkit")
    def history():
        try:
           x=no.get()
           formate="select name,dateofentry,checkintime from cusdetail where (sno={a1})"
           sql=formate.format(a1=x)
           res=cur.execute(sql)
           a=res.fetchmany()
           for i in a:
             nam=i[0]
             da=i[1]
             de=i[2]
           amt=amount()
           ai=datetime.date.today()   ######################################
           formate="insert into historyofcus(name,amount,dat,dateofcheckout)values('{a1}',{b1},'{c1}','{d1}')"
           sql=formate.format(a1=nam,b1=amt,c1=da,d1=ai)
           res=cur.execute(sql)
           cur.execute("commit")
           l3.config(text="Successfully stored")
        except:
            messagebox.showinfo(title="Alert",message="Slno is not in record pls checkit")
    def delete():
        try:
           x=no.get()
           formate="select bedtype from cusdetail where (sno={a1})"
           sql=formate.format(a1=x)
           cur.execute(sql)
           res=cur.fetchone()
           t=res[0]
           if(t=="single"):
               cur.execute("select singlebed from counter")
               a=cur.fetchone()
               i=a[0]
               i=i+1
               formate="update counter set singlebed={a1}"
               sql=formate.format(a1=i)
               res=cur.execute(sql)
               cur.execute("commit")
           elif(t=="double"):
               cur.execute("select doublebed from counter")
               a=cur.fetchone()
               i=a[0]
               i=i+1
               formate="update counter set doublebed={a1}"
               sql=formate.format(a1=i)
               res=cur.execute(sql)
               cur.execute("commit")
           formate="delete from cusdetail where (sno={a1})"
           sql=formate.format(a1=x)
           res=cur.execute(sql)
           cur.execute("commit")
           formate="delete from Time where (sno={a1})"
           sql=formate.format(a1=x)
           res=cur.execute(sql)
           cur.execute("commit")
           l4.config(text="Deleted successfully")
        except:
           messagebox.showinfo(title="Alert",message="Slno is not in record pls checkit")
    no=IntVar()   
    F4=Frame(bg="mint cream")
    F4.place(x=0,y=0,width="1600",height="1000")
    B=Button(F4,text="Menu page",bg="ivory",fg="black",bd=5,command=start)
    B.place(x=0,y=80)
    L=Label(F4,text="Enter s.no of customer-->",bg="mint cream",bd=10,font=("Arial",20))
    L.place(x=200,y=140)
    e1=Entry(F4,textvariable=no,bd=10)
    e1.place(x=520,y=150)
    l1=Label(F4,text="Kindly pay your amount['click button']",bg="mint cream",bd=10,font=("Arial",20))
    l1.place(x=200,y=200)
    l2=Label(F4,text="<-0.",bg="mint cream",bd=10,font=("Arial",20))
    l2.place(x=850,y=200)
    B1=Button(F4,text="Click to display amount",bg="aquamarine",fg="black",bd=5,width=18,height=1,font=("Arial",12),command=amount)
    B1.place(x=670,y=210)
    B2=Button(F4,text="Click it to store in history",bg="aquamarine",bd=5,width=18,height=1,font=("Arial",12),command=history)
    B2.place(x=210,y=270)
    l3=Label(F4,text="->>Click button to store data permanently",bg="mint cream",bd=10,font=("Arial",20))
    l3.place(x=400,y=260)
    l4=Label(F4,text="--->Delete data from common DB",bg="mint cream",bd=10,font=("Arial",20))
    B3=Button(F4,text="Must click to free sl.no",bd=5,bg="aquamarine",width=20,height=1,font=("Arial",12),command=delete)
    l4.place(x=390,y=400)
    B3.place(x=200,y=410)
    n=Label(F4,text="WELCOME TO HOTEL KAAVYA",width=100,fg="purple",bg="lavender",font=("Gigi",40))
    n.place(x=-800,y=0)
def historyofcustomers():       #HISTORY MODULE
    F5=Frame(bg="mint cream")
    F5.place(x=0,y=0,width="1600",height="1000")
    B=Button(F5,text="Menu page",bg="ivory",fg="black",bd=5,command=start)
    B.place(x=0,y=40)
    lk=Label(F5,text="WELCOME TO HOTEL KAAVYA",width=100,bg="lavender",font=("Arial",20))
    lk.pack()
    tree=ttk.Treeview(F5)
    d=ttk.Style(F5)
    d.theme_use("clam")
    tree["columns"]=("name","amount","dat","dateofcheckout")
    tree.column("#0",width=0,anchor=tk.CENTER,stretch=NO)
    tree.column("#1",width=100,anchor=tk.CENTER)
    tree.column("#2",width=100,anchor=tk.CENTER)
    tree.column("#3",width=100,anchor=tk.CENTER)
    tree.column("#4",width=100,anchor=tk.CENTER)
    tree.heading("#0",text="",anchor=tk.CENTER)
    tree.heading("#1",text="Name",anchor=tk.CENTER)
    tree.heading("#2",text="Amount",anchor=tk.CENTER)
    tree.heading("#3",text="Date of checkin",anchor=tk.CENTER)
    tree.heading("#4",text="Date of checkout",anchor=tk.CENTER)

    cur.execute("select * from historyofcus")
    a=cur.fetchall()
    for i in a:
        tree.insert("",index=0,values=(i[0],i[1],i[2],i[3]))
    tree.place(x=400,y=100)
def start():     #MAIN PAGE CONTENT MODULE CONTAINS SUB MODULE
    def show():     #FEED BACK MODULE
       def dele():
            cur.execute("delete from feedback")
            cur.execute("commit")
       F5=Frame(bg="mint cream")
       F5.place(x=0,y=0,width="1600",height="1000")
       B=Button(F5,text="Menu page",bg="ivory",fg="black",bd=5,command=start)
       B.place(x=0,y=50)
       lk=Label(F5,text="WELCOME TO HOTEL KAAVYA",width=100,bg="lavender",font=("Arial",20))
       lk.pack()
       tree=ttk.Treeview(F5)
       d=ttk.Style(F5)
       d.theme_use("clam")
       tree["columns"]=("note")
       tree.column("#0",width=0,anchor=tk.CENTER,stretch=NO)
       tree.column("#1",width=300,anchor=tk.CENTER)
       tree.heading("#0",text="",anchor=tk.CENTER)
       tree.heading("#1",text="Feedbacks",anchor=tk.CENTER)
       cur.execute("select * from feedback")
       a=cur.fetchall()
       for i in a:
            tree.insert("",index=0,values=(i[0]))
       tree.place(x=500,y=100)
       B1=Button(F5,text="Delete feedback",bg="ivory",fg="black",bd=5,font=("Arial",20),command=dele)
       B1.place(x=700,y=500)
    def shown():    
       F5=Frame(bg="mint cream")
       F5.place(x=0,y=0,width="1500",height="1000")
       B=Button(F5,text="Menu page",bg="ivory",fg="black",bd=5,command=start)
       B.place(x=0,y=40)
       lk=Label(F5,text="WELCOME TO HOTEL KAAVYA",width=100,bg="lavender",font=("Arial",20))
       lk.pack()
       cur.execute("select sum(amount) from historyofcus")
       x=cur.fetchone()
       y=str(x[0])      #calculating total amount
       l1=Label(F5,text="Total amount earned till now is->\nit is calculated on\nno of customers checkouts\nfor more details\npls check history of customers",bg="mint cream",font=("Bold",20))
       l1.place(x=0,y=500)
       e=Entry(F5,bd=5,width=50,font=("Bold",20))
       e.insert(0,"RS"+" "+y+"/-")
       e.config(state=DISABLED)
       e.place(x=400,y=510)
       tree=ttk.Treeview(F5)
       d=ttk.Style(F5)
       d.theme_use("clam")
       tree["columns"]=("sno","name","contno","Email","Homeplace","bedtype","dateofentry","daysengaged","checkintime")
       tree.column("#0",width=0,anchor=tk.CENTER,stretch=NO)
       tree.column("#1",width=100,anchor=tk.CENTER)
       tree.column("#2",width=100,anchor=tk.CENTER)
       tree.column("#3",width=100,anchor=tk.CENTER)
       tree.column("#4",width=100,anchor=tk.CENTER)
       tree.column("#5",width=100,anchor=tk.CENTER)
       tree.column("#6",width=100,anchor=tk.CENTER)
       tree.column("#7",width=100,anchor=tk.CENTER)
       tree.column("#8",width=100,anchor=tk.CENTER)
       tree.column("#9",width=100,anchor=tk.CENTER)
       tree.heading("#0",text="",anchor=tk.CENTER)
       tree.heading("#1",text="sno",anchor=tk.CENTER)
       tree.heading("#2",text="Name",anchor=tk.CENTER)
       tree.heading("#3",text="Contact",anchor=tk.CENTER)
       tree.heading("#4",text="E-mail",anchor=tk.CENTER)
       tree.heading("#5",text="Homeplace",anchor=tk.CENTER)
       tree.heading("#6",text="Bed type",anchor=tk.CENTER)
       tree.heading("#7",text="Date of entry",anchor=tk.CENTER)
       tree.heading("#8",text="Days engaged",anchor=tk.CENTER)
       tree.heading("#9",text="Checkin time",anchor=tk.CENTER) 
       cur.execute("select * from cusdetail")
       a=cur.fetchall()
       for i in a:
           tree.insert("",index=0,values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
       tree.place(x=150,y=100)
    def admin():
        pas=password.get()
        if(pas=="12345"):
            shown()
        else:
            l8.config(text="Access denied!")   
    K=StringVar()
    password=StringVar()
    def save():
       j=K.get()
       if(j==''):
           messagebox.showinfo(title="Alert",message="pls enter valid feedback!")
       else:
           formate="insert into feedback(note)values('{a1}')"
           sql=formate.format(a1=j)
           cur.execute(sql)
           cur.execute("commit")
           l5.config(text="Thank you for your response!")
           t.config(state=DISABLED)
           b7.config(state=DISABLED)
    def checkr():
       cur.execute("select singlebed from counter")
       a=cur.fetchone()
       i=a[0]
       L1=Label(F,text="single bed available=",bg="mint cream",font=("Arial",15))
       L2=Label(F,text=i,bg="mint cream",font=("Arial",15))
       cur.execute("select doublebed from counter")
       b=cur.fetchone()
       j=b[0]
       L3=Label(F,text="double bed available=",bg="mint cream",font=("Arial",15))
       L4=Label(F,text=j,bg="mint cream",font=("Arial",15))
       res=i+j
       e1.insert(0,res)
       e1.config(state=DISABLED)
       L1.place(x=1200,y=100)
       L2.place(x=1400,y=100)
       L3.place(x=1200,y=200)
       L4.place(x=1400,y=200)
    def checke():
       cur.execute("select singlebed from counter")
       a=cur.fetchone()
       i=a[0]
       cur.execute("select doublebed from counter")
       b=cur.fetchone()
       j=b[0]
       r=i+j
       res=20-r
       e2.insert(0,res)
       e2.config(state=DISABLED)
    def pa():
       F=Frame(bg="mint cream")
       F.place(x=0,y=0,width="1600",height="1000")
       b1=Button(F,text="Menu page",bg="ivory",fg="black",bd=5,command=start)
       b1.place(x=0,y=50)
       lk=Label(F,text="WELCOME TO HOTEL KAAVYA",width=100,bg="lavender",font=("Arial",20))
       lk.pack()
       cur.execute("select sno,nextday,time from Time")
       a=cur.fetchall()
       for i in a:
             no=i[0]
             nd=i[1]
             u=str(i[2])
             d=datetime.date.today()
             td=str(d)
             a=td[0:4]
             b=td[5:7]
             c=td[8:10]
             a11=nd[0:4]
             b11=nd[5:7]
             c11=nd[8:10]
             tday=date(int(a),int(b),int(c))
             nday=date(int(a11),int(b11),int(c11))
             remday=(nday-tday)
             x=int(u[0:2])
             y=int(u[3:5])
             z=int(u[6:8])
             h=datetime.datetime.now().time()
             ntim=datetime.time(int(x),int(y),int(z))
             diff=datetime.timedelta(hours=(ntim.hour-h.hour),minutes=(ntim.minute-h.minute),seconds=(ntim.second-h.second))
             temp=str(remday)
             a2=temp[0:6]
             tem=str(diff)
             b2=tem[8:16]
             try:         ####This will notify customer is out of checkout time
               a3=int(a2[0:2])
               if(a3<0):
                 messagebox.showinfo(title="Alert",message="SLNO"+" "+str(no)+" "+"is crossed time of checkout")
             except:
                 pass
             formate="insert into detail(sno,day,ti)values({a1},'{b1}','{c1}')"
             sql=formate.format(a1=no,b1=a2,c1=b2)
             res=cur.execute(sql)
             cur.execute("commit")
       tree=ttk.Treeview(F)
       d=ttk.Style(F)
       d.theme_use("clam")
       tree["columns"]=("sno","day","ti")
       tree.column("#0",width=0,anchor=tk.CENTER,stretch=NO)
       tree.column("#1",width=100,anchor=tk.CENTER)
       tree.column("#2",width=200,anchor=tk.CENTER)
       tree.column("#3",width=200,anchor=tk.CENTER)
       tree.heading("#0",text="",anchor=tk.CENTER)
       tree.heading("#1",text="SNO",anchor=tk.CENTER)
       tree.heading("#2",text="DAYS REMAINING",anchor=tk.CENTER)
       tree.heading("#3",text="TIME REMAINING",anchor=tk.CENTER)
       cur.execute("select sno,day,ti from detail")
       res=cur.fetchall()
       for j in res:
           tree.insert("",index=0,values=(j[0],j[1],j[2]))
       tree.place(x=300,y=100)
       cur.execute("delete from detail")
       cur.execute("commit")
    F=Frame(bg="mint cream")
    F2=Frame(bg="light cyan")
    F.place(x=0,y=0,width="1600",height="1000")
    F2.place(x=0,y=0,width=400,height=1000)
    b1=Button(F,text="Go to home page",bg="ivory",fg="black",command=home,bd=5)
    b1.place(x=400,y=40)
    lk=Label(F,text="WELCOME TO HOTEL KAAVYA",width=100,bg="lavender",fg="purple",font=("Arial",20))
    lk.pack()
    b2=Button(F,text="Rooms available",command=checkr,bd=5,height=1,width=15,bg="snow",font=("Arial",12))
    b3=Button(F,text="Rooms engaged",command=checke,bd=5,height=1,width=15,bg="snow",font=("Arial",12))
    b4=Button(F,text="customer checkin",command=checkin,height=1,width=15,bd=5,bg="snow",font=("Arial",12))
    b5=Button(F,text="customer checkout",command=checkout,height=1,width=15,bd=5,bg="snow",font=("Arial",12))
    b6=Button(F,text="History of customers",command=historyofcustomers,bd=5,height=1,width=15,bg="snow",font=("Arial",12))
    b7=Button(F,text="Feedback about Hotel\npositive or complain\nclick!!",command=save,bd=5,bg="snow",font=("Arial",12))
    b8=Button(F,text="History of Feedback about Hotel",command=show,bd=5,bg="snow",font=("Arial",12))
    b9=Button(F,text="Private details!",command=admin,bd=5,bg="snow",font=("Arial",12))
    b2.place(x=700,y=100)
    b3.place(x=700,y=150)
    b4.place(x=700,y=200)
    b5.place(x=700,y=250)
    b6.place(x=700,y=300)
    b7.place(x=700,y=555)
    b8.place(x=700,y=350)
    b9.place(x=700,y=450)
    e1=Entry(F,bd=10,font=("Arial",15))
    e2=Entry(F,bd=10,font=("Arial",15))
    e3=Entry(F,bd=10,font=("Arial",15),textvariable=password,show="*")
    e1.place(x=900,y=95)
    e2.place(x=900,y=145)
    e3.place(x=900,y=450)
    l1=Label(F2,text="Our's Address is\n77-A Marina Beach Road\n Chennai-600034.",bg="light cyan",font=("Bold",20))
    l1.place(x=0,y=0)
    l2=Label(F2,text="Our's E-mail is\nHotel_Kaavya@gmail.com",bg="light cyan",font=("Bold",20))
    l2.place(x=20,y=100)
    l3=Label(F2,text="1.Our Hotel is placed\n near Marina beach\n2.We provide 24hrs\nwater facility\n3.We provide hygenic food\n 4.Public Transport is available\nfor 24 hrs ",bg="light cyan",font=("Bold",20))
    l3.place(x=0,y=200)
    l4=Label(F2,text="We have totally 20 rooms\n10-single bed\n10-double bed",bg="light cyan",font=("Bold",20))
    l4.place(x=0,y=500)
    l5=Label(F2,text="Single bed for 24hrs=RS.4500/-\nDouble bed for 24hrs=RS.8000/-",bg="light cyan",font=("Bold",20))
    l5.place(x=0,y=600)
    l8=Label(F,text="Enter admin password!---->",bg="mint cream",font=("Arial",12))
    l8.place(x=500,y=460)
    b9=Button(F,text="show time of checkouts",command=pa,bd=5,bg="snow",font=("Arial",12))
    b9.place(x=700,y=400)
    t=Entry(F,width=30,bd=10,textvariable=K,font=("Bold",25))
    t.place(x=900,y=565)
    l5=Label(F,text="TELL YOUR RESPONSES ABOVE TEXT BOX\nWE ONCE AGAIN THANK YOU!!!\nVISIT AGAIN!!!",bg="lavender",fg="purple",font=("Bold",20))
    l5.place(x=700,y=650)
    def time():
        t_s=strftime('%H:%M:%S%p\n%x\n%a')
        l6.config(text=t_s)
        l6.after(1000,time)               #recursive time updation
    l6=Label(F2,font=("Bold",20),bg="gold")
    l6.place(x=110,y=680)
    time()
if __name__=='__main__':            #MAIN MODULE!!!!!!!! program starts from here
    window=Tk()
    window.title("HOTEL MANAGEMENT SYSTEM")
    window.maxsize(width="1600",height="1000")
    I=Image.open('set your image from drive')
    bk=ImageTk.PhotoImage(I)
    def home():      #HOME PAGE MODULE
        f=Frame()
        f.config(bg="mint cream")
        f.place(x=0,y=0,width="1600",height="1000")
        l1=Label(window,text="WELCOME TO HOTEL KAAVYA",width=100,fg="purple",bg="lavender",font=("Gigi",40))
        l2=Label(window,image=bk)
        B=Button(window,text="ENTER",bg="ivory",fg="purple",bd=10,width=20,height=10,font=("bold",10),command=start)
        l1.place(x=-700,y=0)
        l2.place(x=0,y=80)
        B.place(x=700,y=570)
    home()
    window.mainloop()
    
