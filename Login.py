#Front End
import sqlite3
import tkinter.messagebox

# import Bill Management
from tkinter import *
a=Tk()
a.title("Login")

def sign_in():
    conn=sqlite3.connect('signup.db')
    c=conn.cursor()

    c.execute('SELECT *,email, pass FROM users')

    records=c.fetchall()
    # print(records)
    found_username = ''
    found_password=''
    for record in records:

        if str(record[2])==entry1.get():
            print ("Found Username")
        else:
            print("Not Found")



a.configure(bg='Purple')
# a.iconbitmap('H:\\My Drive\\a\\icon.ico')
a.maxsize(width=1000,height=660)
a.minsize(width=1000,height=660)
# canvas=Canvas(a,bg='#06518d',height=1000,width=500).place(x=500,y=0)
photo=PhotoImage(file='lockremove.png')
image=Label(a,image=photo,bg='purple').place(x=0,y=200)
label1=Label(a,text=" WELCOME TO BIll MANAGEMENT SYSTEM",font=('Times New Roman',24,'bold'),fg='black',bg='purple').place(x=50,y=50)
# label2=Label(a,text='One place for all your needs.',font=('Calisto MT Bold',18),bg='White',fg='').place(x=100,y=125)
label4=Label(a,text='_______',font=('Calisto MT Bold',14,'bold'),fg='black',bg="purple").place(x=600,y=195)
label3=Label(a,text='Login',fg='black',font=('Calisto MT Bold',14,'bold'),bg="purple").place(x=600,y=180)
label5=Label(a,text='Username :',font=('Calisto MT Bold',14,'bold'),fg='black',bg="purple").place(x=600,y=230)
entry1=Entry(a,borderwidth=1,bg='White')
entry1.config(width=30)
entry1.place(x=710,y=235)
label6=Label(a,text='Password :',font=('Calisto MT Bold',14,'bold'),fg='black',bg="purple").place(x=600,y=270)
pas=Entry(a,borderwidth=1,bg='White',show='*')
pas.place(x=710,y=275)









# C1=Checkbutton(a,text='Show Password',bg='#06518d',fg='White',font=('Calisto MT Bold',10))
# C1.place(x=600,y=310)

def invalid():
    invalid=tkinter.messagebox.Message('Invalid','Invalid Crediantials')


def des():
    a.destroy()
    import dashboard
button1=Button(a,text='Login',fg='white',bg='purple',font=('Calisto MT Bold',14,'bold'),height=1,width=7,command=des).place(x=690,y=360)

def hee():
    git.config(text=CheckVar1.get())
CheckVar2=IntVar()

def forget():
    a.destroy()
    import fpas

label7=Button(a,text='Forgot Password?',bg='purple',fg='white',font=('Roboto ',10),command=forget).place(x=780,y=300)
show_pass=IntVar()
def show_pass_check():
    if show_pass.get():
        pas.config(show='')
    else:
        pas.config(show='*')

# c = Checkbutton(root,fg='black',border=0,text ="Show",bg='white',font=('roboto',8)).place(x=50,y=395)
c1 = Checkbutton(a,fg='white',border=0,text ="Show",bg='purple',font=('roboto',8),command=show_pass_check,variable=show_pass,onvalue=1,offvalue=0).place(x=600,y=310)




# img3=PhotoImage(file='add-on-services.png')
# image=Label(a,image=img3,bg='White').place(x=300,y=500)


a.mainloop()