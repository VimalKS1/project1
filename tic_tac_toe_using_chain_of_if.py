from tkinter import *
import random as r
#accracy 85%.
i1=0
i2=0
i3=0
i4=0
i5=0
i6=0
i7=0
i8=0
i9=0
m=0
n=0
v=0
mid=0
count=0
j1=""
j2=""
j3=""
j4=""
j5=""
j6=""
j7=""
j8=""
j9=""
def check():
        global j1,j2,j3,j4,j5,j6,j7,j8,j9,i1,i2,i3,i4,i5,i6,i7,i8,i9
        if((j1=="x")and(j2=="x")and(j3=="x")):
                b1.config(bg="white")
                b2.config(bg="white")
                b3.config(bg="white")
                l2.config(text="you won")
                freeze()
        elif((j4=="x")and(j5=="x")and(j6=="x")):
                b4.config(bg="white")
                b5.config(bg="white")
                b6.config(bg="white")
                l2.config(text="you won")
                freeze()
        elif((i7=="x")and(j8=="x")and(i9=="x")):
                b7.config(bg="white")
                b8.config(bg="white")
                b9.config(bg="white")
                l2.config(text="you won")
                freeze()
        elif((j1=="x")and(j4=="x")and(j7=="x")):
                b1.config(bg="white")
                b4.config(bg="white")
                b7.config(bg="white")
                l2.config(text="you won")
                freeze()
        elif((j2=="x")and(j5=="x")and(j8=="x")):
                b2.config(bg="white")
                b5.config(bg="white")
                b8.config(bg="white")
                l2.config(text="you won")
                freeze()
        elif((j3=="x")and(j6=="x")and(j9=="x")):
                b3.config(bg="white")
                b6.config(bg="white")
                b9.config(bg="white")
                l2.config(text="you won")
                freeze()
        elif((j1=="x")and(j5=="x")and(j9=="x")):
                b1.config(bg="white")
                b5.config(bg="white")
                b9.config(bg="white")
                l2.config(text="you won")
                freeze()
        elif((j3=="x")and(j5=="x")and(j7=="x")):
                b3.config(bg="white")
                b5.config(bg="white")
                b7.config(bg="white")
                l2.config(text="you won")
                freeze()
        elif((j1=="o")and(j2=="o")and(j3=="o")):
                b1.config(bg="white")
                b2.config(bg="white")
                b3.config(bg="white")
                l2.config(text="computer won")
                freeze()
        elif((j4=="o")and(j5=="o")and(j6=="o")):
                b4.config(bg="white")
                b5.config(bg="white")
                b6.config(bg="white")
                l2.config(text="computer won")
                freeze()
        elif((j7=="o")and(j8=="o")and(j9=="o")):
                b7.config(bg="white")
                b8.config(bg="white")
                b9.config(bg="white")
                l2.config(text="computer won")
                freeze()
        elif((j1=="o")and(j4=="o")and(j7=="o")):
                b1.config(bg="white")
                b4.config(bg="white")
                b7.config(bg="white")
                l2.config(text="computer won")
                freeze()
        elif((j2=="o")and(j5=="o")and(j8=="o")):
                b2.config(bg="white")
                b5.config(bg="white")
                b8.config(bg="white")
                l2.config(text="computer won")
                freeze()
        elif((j3=="o")and(j6=="o")and(j9=="o")):
                b3.config(bg="white")
                b6.config(bg="white")
                b9.config(bg="white")
                l2.config(text="computer won")
                freeze()
        elif((j1=="o")and(j5=="o")and(j9=="o")):
                b1.config(bg="white")
                b5.config(bg="white")
                b9.config(bg="white")
                l2.config(text="computer won")
                freeze()
        elif((j3=="o")and(j5=="o")and(j7=="o")):
                b3.config(bg="white")
                b5.config(bg="white")
                b7.config(bg="white")
                l2.config(text="computer won")
                freeze()
        elif((i1==1)and(i2==1)and(i3==1)and(i4==1)and(i5==1)and(i6==1)and(i7==1)and(i8==1)and(i9==1)):
                l2.config(text="Draw")
                freeze()
                
def freeze():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        return 0
def AI():
    global j1,j2,j3,j4,j5,j6,j7,j8,j9,i1,i2,i3,i4,i5,i6,i7,i8,i9,m,v
    v=v+1
    u=1
    try:
        if(((j1=="o")and(j2=="o"))or((j6=="o")and(j9=="o"))or((j7=="o")and(j5=="o"))):
           if ((i3==0)and(v==1)):
              b3.config(text="O",font=("Arial",15),state=DISABLED)
              j3="o"
              i3+=1
              m-=1
              v-=1
              u-=1
        if(((j4=="o")and(j5=="o"))or((j3=="o")and(j9=="o"))):
           if ((i6==0)and(v==1)):
              b6.config(text="O",font=("Arial",15),state=DISABLED)
              j6="o"
              i6+=1
              m-=1
              v-=1
              u-=1
        if(((j7=="o")and(j8=="o"))or((j3=="o")and(j6=="o"))or((j1=="o")and(j5=="o"))):
           if ((i9==0)and(v==1)):
              b9.config(text="O",font=("Arial",15),state=DISABLED)
              j9="o"
              i9+=1
              m-=1
              v-=1
              u-=1
        if(((j1=="o")and(j3=="o"))or((j5=="o")and(j8=="o"))):
           if ((i2==0)and(v==1)):
              b2.config(text="O",font=("Arial",15),state=DISABLED)
              j2="o"
              i2+=1
              m-=1
              v-=1
              u-=1
        if(((j4=="o")and(j6=="o"))or((j2=="o")and(j8=="o"))or((j1=="o")and(j9=="o"))or((j3=="o")and(j7=="o"))):
           if ((i5==0)and(v==1)):
              b5.config(text="O",font=("Arial",15),state=DISABLED)
              j5="o"
              i5+=1
              m-=1
              v-=1
              u-=1
        if(((j7=="o")and(j9=="o"))or((j2=="o")and(j5=="o"))):
           if ((i8==0)and(v==1)):
              b8.config(text="O",font=("Arial",15),state=DISABLED)
              j8="o"
              i8+=1
              m-=1
              v-=1
              u-=1
        if(((j2=="o")and(j3=="o"))or((j4=="o")and(j7=="o"))or((j5=="o")and(j9=="o"))):
           if ((i1==0)and(v==1)):
              b1.config(text="O",font=("Arial",15),state=DISABLED)
              j1="o"
              i1+=1
              m-=1
              v-=1
              u-=1
        if(((j5=="o")and(j6=="o"))or((j1=="o")and(j7=="o"))):
           if ((i4==0)and(v==1)):
              b4.config(text="O",font=("Arial",15),state=DISABLED)
              j4="o"
              i4+=1
              m-=1
              v-=1
              u-=1
        if(((j8=="o")and(j9=="o"))or((j1=="o")and(j4=="o"))or((j3=="o")and(j5=="o"))):
           if ((i7==0)and(v==1)):
              b7.config(text="O",font=("Arial",15),state=DISABLED)
              j7="o"
              i7+=1
              m-=1
              v-=1
              u-=1
        ########################################################################################################################################################
        if(((j1=="x")and(j2=="x"))or((j6=="x")and(j9=="x"))or((j7=="x")and(j5=="x"))):
           if ((i3==0)and(v==1)):
              b3.config(text="O",font=("Arial",15),state=DISABLED)
              j3="o"
              i3+=1
              m-=1
              v-=1
              u-=1
        if(((j4=="x")and(j5=="x"))or((j3=="x")and(j9=="x"))):
           if ((i6==0)and(v==1)):
              b6.config(text="O",font=("Arial",15),state=DISABLED)
              j6="o"
              i6+=1
              m-=1
              v-=1
              u-=1
        if(((j7=="x")and(j8=="x"))or((j3=="x")and(j6=="x"))or((j1=="x")and(j5=="x"))):
           if ((i9==0)and(v==1)):
              b9.config(text="O",font=("Arial",15),state=DISABLED)
              j9="o"
              i9+=1
              m-=1
              v-=1
              u-=1
        if(((j1=="x")and(j3=="x"))or((j5=="x")and(j8=="x"))):
           if ((i2==0)and(v==1)):
              b2.config(text="O",font=("Arial",15),state=DISABLED)
              j2="o"
              i2+=1
              m-=1
              v-=1
              u-=1
        if(((j4=="x")and(j6=="x"))or((j2=="x")and(j8=="x"))or((j1=="x")and(j9=="x"))or((j3=="x")and(j7=="x"))):
           if ((i5==0)and(v==1)):
              b5.config(text="O",font=("Arial",15),state=DISABLED)
              j5="o"
              i5+=1
              m-=1
              v-=1
              u-=1
        if(((j7=="x")and(j9=="x"))or((j2=="x")and(j5=="x"))):
           if ((i8==0)and(v==1)):
              b8.config(text="O",font=("Arial",15),state=DISABLED)
              j8="o"
              i8+=1
              m-=1
              v-=1
              u-=1
        if(((j2=="x")and(j3=="x"))or((j4=="x")and(j7=="x"))or((j5=="x")and(j9=="x"))):
           if ((i1==0)and(v==1)):
              b1.config(text="O",font=("Arial",15),state=DISABLED)
              j1="o"
              i1+=1
              m-=1
              v-=1
              u-=1
        if(((j5=="x")and(j6=="x"))or((j1=="x")and(j7=="x"))):
           if ((i4==0)and(v==1)):
              b4.config(text="O",font=("Arial",15),state=DISABLED)
              j4="o"
              i4+=1
              m-=1
              v-=1
              u-=1
        if(((j8=="x")and(j9=="x"))or((j1=="x")and(j4=="x"))or((j3=="x")and(j5=="x"))):
           if ((i7==0)and(v==1)):
              b7.config(text="O",font=("Arial",15),state=DISABLED)
              j7="o"
              i7+=1
              m-=1
              v-=1
              u-=1
    finally:
        if u==1:
          ran_com()
          v-=1
    check()
        
def c1():
        global i1,j1
        if i1==0:
            b1.config(text="X",font=("Arial",15),state=DISABLED)
            i1+=1
            j1="x"
            check()
def c2():
        global i2,j2
        if i2==0:
            b2.config(text="X",font=("Arial",15),state=DISABLED)
            i2+=1
            j2="x"
            check()
def c3():
        global i3,j3
        if i3==0:
            b3.config(text="X",font=("Arial",15),state=DISABLED)
            i3+=1
            j3="x"
            check()
def c4():
        global i4,j4
        if i4==0:
           b4.config(text="X",font=("Arial",15),state=DISABLED)
           i4+=1
           j4="x"
           check()
def c5():
        global i5,j5
        if i5==0:
           b5.config(text="X",font=("Arial",15),state=DISABLED)
           i5+=1
           j5="x"
           check()
def c6():
        global i6,j6
        if i6==0:
           b6.config(text="X",font=("Arial",15),state=DISABLED)
           i6+=1
           j6="x"
           check()
def c7():
        global i7,j7
        if i7==0:
           b7.config(text="X",font=("Arial",15),state=DISABLED)
           i7+=1
           j7="x"
           check()
def c8():
        global i8,j8
        if i8==0:
           b8.config(text="X",font=("Arial",15),state=DISABLED)
           i8+=1
           j8="x"
           check()
def c9():
        global i9,j9
        if i9==0:
           b9.config(text="X",font=("Arial",15),state=DISABLED)
           i9+=1
           j9="x"
           check()
def d1():
        global m,n
        c1()
        m=m+1
        if n==0:
          ran_com()
          n+=1
        else:
          AI()
def d2():
        global m,n
        c2()
        m=m+1
        if n==0:
          ran_com()
          n+=1
        else:
          AI()
def d3():
        global m,n
        c3()
        m=m+1
        if n==0:
          ran_com()
          n+=1
        else:
          AI()
def d4():
        global m,n
        c4()
        m=m+1
        if n==0:
          ran_com()
          n+=1
        else:
          AI()
def d5():
        global m,n
        c5()
        m=m+1
        if n==0:
          ran_com()
          n+=1
        else:
          AI()
def d6():
        global m,n
        c6()
        m=m+1
        if n==0:
          ran_com()
          n+=1
        else:
          AI()
def d7():
        global m,n
        c7()
        m=m+1
        if n==0:
          ran_com()
          n+=1
        else:
          AI()
def d8():
        global m,n
        c8()
        m=m+1
        if n==0:
          ran_com()
          n+=1
        else:
          AI()
def d9():
        global m,n
        c9()
        m=m+1
        if n==0:
          ran_com()
          n+=1
        else:
          AI()
def reset():
        global j1,j2,j3,j4,j5,j6,j7,j8,j9,i1,i2,i3,i4,i5,i6,i7,i8,i9,m,n,count,v,mid
        i1=0
        i2=0
        i3=0
        i4=0
        i5=0
        i6=0
        i7=0
        i8=0
        i9=0
        m=0
        n=0
        v=0
        mid=0
        count=0
        j1=""
        j2=""
        j3=""
        j4=""
        j5=""
        j6=""
        j7=""
        j8=""
        j9=""
        b1.config(state=NORMAL,text="",bg="turquoise1")
        b2.config(state=NORMAL,text="",bg="turquoise1")
        b3.config(state=NORMAL,text="",bg="turquoise1")
        b4.config(state=NORMAL,text="",bg="turquoise1")
        b5.config(state=NORMAL,text="",bg="turquoise1")
        b6.config(state=NORMAL,text="",bg="turquoise1")
        b7.config(state=NORMAL,text="",bg="turquoise1")
        b8.config(state=NORMAL,text="",bg="turquoise1")
        b9.config(state=NORMAL,text="",bg="turquoise1")
        l2.config(text="")
def ran_com():
      global m,count,mid
      if mid==0:
          global i5,j5
          if i5==0:
              b5.config(text="O",font=("Arial",15),state=DISABLED)
              j5="o"
              i5+=1
              m-=1
              mid+=1
              check()
      if m==1:
        a=r.randint(1,9)
        count+=1
        if a==1:
           global i1,j1
           if i1==0:
              b1.config(text="O",font=("Arial",15),state=DISABLED)
              j1="o"
              i1+=1
              m-=1
              check()
           else:
              if count<30:
                ran_com()
              else:
                      freeze()
        if a==2:
           global i2,j2
           if i2==0:
              b2.config(text="O",font=("Arial",15),state=DISABLED)
              j2="o"
              i2+=1
              m-=1
              check()
           else:
              if count<30:
                ran_com()
              else:
                      freeze()
        if a==3:
           global i3,j3
           if i3==0:
              b3.config(text="O",font=("Arial",15),state=DISABLED)
              j3="o"
              i3+=1
              m-=1
              check()
           else:
              if count<30:
                ran_com()
              else:
                      freeze()
        if a==4:
           global i4,j4
           if i4==0:
              b4.config(text="O",font=("Arial",15),state=DISABLED)
              j4="o"
              i4+=1
              m-=1
              check()
           else:
              if count<30:
                ran_com()
              else:
                      freeze()
        if a==5:
          #global i5,j5
          if i5==0:
              b5.config(text="O",font=("Arial",15),state=DISABLED)
              j5="o"
              i5+=1
              m-=1
              check()
          else:
              if count<30:
                ran_com()
              else:
                      freeze()
        if a==6:
          global i6,j6
          if i6==0:
              b6.config(text="O",font=("Arial",15),state=DISABLED)
              j6="o"
              i6+=1
              m-=1
              check()
          else:
              if count<30:
                ran_com()
              else:
                      freeze()
        if a==7:
          global i7,j7
          if i7==0:
              b7.config(text="O",font=("Arial",15),state=DISABLED)
              j7="o"
              i7+=1
              m-=1
              check()
          else:
              if count<30:
                ran_com()
              else:
                      freeze()
        if a==8:
          global i8,j8
          if i8==0:
              b8.config(text="O",font=("Arial",15),state=DISABLED)
              j8="o"
              i8+=1
              m-=1
              check()
          else:
              if count<30:
                ran_com()
              else:
                      freeze()
        if a==9:
          global i9,j9
          if i9==0:
              b9.config(text="O",font=("Arial",15),state=DISABLED)
              j9="o"
              i9+=1
              m-=1
              check()
          else:
              if count<30:
                ran_com()
              else:
                      freeze()
if __name__=='__main__':
  window=Tk()
  window.title("TIC TAC TOE")
  f1=Frame()
  f1.config(bg="darkSlateGray1")
  f1.place(x=0,y=0,width="1600",height="1000")
  l=Label(f1,text="WELCOME",width=55,fg="purple",bg="SpringGreen2",font=("Gigi",40))
  l.place(x=0,y=0)
  b10=Button(f1,width=15,height=2,text="RESET",bg="ivory",font=("Arial",25),command=reset)
  b10.place(x=600,y=80)
  
  
  
  l1=Label(f1,text="You are X\nYou can start now!!!",bg="SeaGreen1",fg="blue",font=("Arial",25))
  l1.place(x=100,y=200)
  global l2,b1,b2,b3,b4,b5,b6,b7,b8,b9
  l2=Label(window,text="",bg="SeaGreen1",fg="blue",font=("Arial",25))
  l2.place(x=100,y=500)
  f2=Frame()
  f2.place(x=450,y=200,width=550,height=480)
  b1=Button(f2,width=25,height=10,text="",bg="turquoise1",command=d1)
  b1.place(x=0,y=0)
  b2=Button(f2,width=25,height=10,text="",bg="turquoise1",command=d2)
  b2.place(x=185,y=0)
  b3=Button(f2,width=25,height=10,text="",bg="turquoise1",command=d3)
  b3.place(x=370,y=0)
  b4=Button(f2,width=25,height=10,text="",bg="turquoise1",command=d4)
  b4.place(x=0,y=160)
  b5=Button(f2,width=25,height=10,text="",bg="turquoise1",command=d5)
  b5.place(x=185,y=160)
  b6=Button(f2,width=25,height=10,text="",bg="turquoise1",command=d6)
  b6.place(x=370,y=160)
  b7=Button(f2,width=25,height=10,text="",bg="turquoise1",command=d7)
  b7.place(x=0,y=320)
  b8=Button(f2,width=25,height=10,text="",bg="turquoise1",command=d8)
  b8.place(x=185,y=320)
  b9=Button(f2,width=25,height=10,text="",bg="turquoise1",command=d9)
  b9.place(x=370,y=320)
  






  


