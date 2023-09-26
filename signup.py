from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox

def login_page():
    signup_window.destroy()
    import login
def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)
def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('ERROR', "Fill all the fields")
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('ERROR', "'Password' and 'Confirm Password' should be same")
    elif check.get()==0:
        messagebox.showerror('ERROR', 'Agree to the Terms & Comnditions to proceed')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='revanth_654')
            mycursor = con.cursor()
        except:
            messagebox.showerror('ERROR',"There is an issue with the Database.\nPlease try again")
            return

        try:
            mycursor.execute('create database userdata')
            mycursor.execute('use userdata')
            mycursor.execute('create table data(id int auto_increment primary key not null, email varchar(50), username varchar(30), password varchar(20))')
        except:
            mycursor.execute('use userdata')

        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))
        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('ERROR', 'Your desired Username already exists')
        else:
            query = 'insert into data(email, username, password) values (%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('CONGRATULATIONS', 'New Account created')
            clear()
            signup_window.destroy()
            import login



signup_window = Tk()
signup_window.title("SIGN-UP")
signup_window.resizable(False,False)


background = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window, width=50, height=20, bg='white')
frame.place(x=554, y=100)

heading = Label(frame, text='CREATE NEW ACCOUNT', font=('Microsoft Yahei UI Light', 16, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=19, pady=10)

emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25)
emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
emailEntry.grid(row=2,column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10,0))
usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
usernameEntry.grid(row=4,column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10,0))
passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
passwordEntry.grid(row=6,column=0, sticky='w', padx=25)

confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10,0))
confirmEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
confirmEntry.grid(row=8,column=0, sticky='w', padx=25)

check = IntVar()
termsandconditions = Checkbutton(frame, text='I agree to all Terms & Conditions', font=('Microsoft Yahei UI Light', 10, 'bold'), fg='firebrick1', bg='white', activeforeground='firebrick1', activebackground='white', cursor='hand2', variable=check)
termsandconditions.grid(row=9,column=0, padx=5, pady=10)

signupButton = Button(frame, text='Signup', font=('Open Sans', 16, 'bold'), bd=0, fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', width=17, command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

alreadyaccount = Label(frame, text="Already have an account?", font=('Open Sans',9,'bold'), fg='firebrick1', bg='white')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25)

loginButton = Button(frame, text='Log In', font=('Open Sans', 9, 'bold underline'), fg='blue', bg='white', activebackground='white', activeforeground='blue', cursor='hand2', bd=0, command=login_page)
loginButton.place(x=176,y=383)



signup_window.mainloop()