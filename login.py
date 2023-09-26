from tkinter import *
from tkinter import messagebox
import socket
import pymysql
from PIL import ImageTk,Image
import time
import random


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0,END)
def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0,END)
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
def signup_page():
    login_window.destroy()
    import signup


def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('ERROR', "Fill all the fields")
    else:
        try:
            client()
            """con = pymysql.connect(host='localhost', user='root', password='revanth_654')
            mycursor = con.cursor()"""
        except:
            messagebox.showerror('ERROR', "Connection not established.\nPlease try again")
            return
        mycursor.execute('use userdata')
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('ERROR', 'Invalid Username or Password')
        else:
            messagebox.showinfo('WELCOME', 'Login successful')


def client():

    window1 = Toplevel(login_window)
    window1.title("Seccon Client")

    window1.configure(bg="firebrick1")

    username = " "

    def denc(choice, key, cyphertext):
        if choice == 1:
            plaintext = ""

            for i in range(len(cyphertext)):
                char = cyphertext[i]

                if (char.isupper()):
                    plaintext += chr((ord(char) - key - 65) % 26 + 65)

                elif (char.islower()):
                    plaintext += chr((ord(char) - key - 97) % 26 + 97)

                else:
                    plaintext += cyphertext[i]

            return plaintext

        elif choice == 2:
            input_str = cyphertext
            output_str = ""
            keyy = str(key)
            for i, char in enumerate(input_str):
                output_str += chr(ord(char) ^ ord(keyy[i % len(keyy)]))
            return output_str

        elif choice == 3:
            cyphertext = cyphertext[::-1]
            plaintext = ""

            for i in range(len(cyphertext)):
                char = cyphertext[i]

                if (char.isupper()):
                    plaintext += chr((ord(char) - key - 65) % 26 + 65)

                elif (char.islower()):
                    plaintext += chr((ord(char) - key - 97) % 26 + 97)

                else:
                    plaintext += cyphertext[i]

            return plaintext

        elif choice == 4:
            return cyphertext
        elif choice == 5:
            return cyphertext

    def enc(msgg):
        """print("1.Ceaser Cipher")
        print("2.Simple XOR Cipher")
        print("3.Reverse Cipher")
        print("4.DES Encryption")
        print("5.RSA Encryption")
        choice = int(input("Enter Algo choice : "))"""
        global var
        choice = int(var.get())

        if choice == 1:
            text = msgg
            key = random.randint(1, 26)
            cyphertext = ""

            for i in range(len(text)):
                char = text[i]

                if (char.isupper()):
                    cyphertext += chr((ord(char) + key - 65) % 26 + 65)

                elif (char.islower()):
                    cyphertext += chr((ord(char) + key - 97) % 26 + 97)

                else:
                    cyphertext += text[i]

            print("Key: ", key)
            print(str(choice) + str(key) + cyphertext)
            return str(choice) + ":" + str(key) + ";" + cyphertext

        elif choice == 2:
            input_str = msgg
            output_str = ""
            key = str(random.randint(1, 9999))
            for i, char in enumerate(input_str):
                output_str += chr(ord(char) ^ ord(key[i % len(key)]))
            return str(choice) + ":" + str(key) + ";" + output_str

        elif choice == 3:
            text = msgg
            text = text[::-1]
            key = random.randint(1, 26)
            cyphertext = ""

            for i in range(len(text)):
                char = text[i]

                if (char.isupper()):
                    cyphertext += chr((ord(char) + key - 65) % 26 + 65)

                elif (char.islower()):
                    cyphertext += chr((ord(char) + key - 97) % 26 + 97)

                else:
                    cyphertext += text[i]
            return str(choice) + ":" + str(key) + ";" + cyphertext
        elif choice == 4:
            return str(choice) + ":" + str("01012305104689704578546987123654") + ";" + cyphertext
        elif choice == 5:
            return str(choice) + ":" + str("45154788956258895626369845155487") + ";" + cyphertext

    topFrame = Frame(window1, bg='firebrick1')
    lblName = Label(topFrame, text="                             Name:", bg='tomato').pack(side=LEFT)
    entName = Entry(topFrame, width=57)
    entName.pack(side=LEFT, fill=Y, padx=(6, 0), pady=(5, 5))
    btnConnect = Button(topFrame, text="Connect", command=lambda: connect())
    btnConnect.pack(side=LEFT, padx=(5, 13), pady=(5, 10))
    # btnConnect.bind('<Button-1>', connect)
    # topFrame.pack(side=tk.TOP)
    topFrame.grid(row=0, column=0)

    dFrame = Frame(window1, bg='firebrick1')
    lblName = Label(dFrame, text="              Encrypted Text:", bg="tomato").pack(side=LEFT)
    tkD = Text(dFrame, height=0.1, width=50)
    tkD.pack(side=LEFT, fill=Y, padx=(5, 13), pady=(5, 10))
    # dFrame.pack(side=tk.TOP)
    dFrame.grid(row=1, column=0)
    var = StringVar()
    var.set("0")
    displayFrame = Frame(window1, bg='tomato')
    # lblLine = tk.Label(displayFrame, text="*********************************************************************").pack()
    scrollBar = Scrollbar(displayFrame)
    scrollBar.pack(side=RIGHT, fill=Y)
    tkDisplay = Text(displayFrame, height=20, width=50)
    tkDisplay.pack(side=RIGHT, fill=Y, padx=(5, 0))
    tkDisplay.tag_config("tag_your_message", foreground="red")
    scrollBar.config(command=tkDisplay.yview)
    tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
    tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
    # displayFrame.pack(side=tk.TOP)
    displayFrame.grid(row=2, column=0)

    RFrame = Frame(window1, bg="firebrick1")
    lblName = Label(displayFrame, text="\nEncryption Algo:", bg="tomato").pack(padx=(5, 13), pady=(5, 10))
    radio = Radiobutton(displayFrame, text="Ceaser Cipher", padx=14, variable=var, value="1", bg='tomato').pack(
        anchor="w")
    radio = Radiobutton(displayFrame, text="XOR Encrypt", padx=14, variable=var, value="2", bg='tomato').pack(
        anchor="w")
    radio = Radiobutton(displayFrame, text="Reverse Ceaser", padx=14, variable=var, value="3", bg='tomato').pack(
        anchor="w")
    radio = Radiobutton(displayFrame, text="DES Encrypt", padx=14, variable=var, value="4", bg='tomato').pack(
        anchor="w")
    radio = Radiobutton(displayFrame, text="RSA Encrypt", padx=14, variable=var, value="5", bg='tomato').pack(
        anchor="w")
    # RFrame.pack(side=tk.TOP)
    RFrame.grid(row=2, column=0)

    bottomFrame = Frame(window1, bg='firebrick1')
    lblName = Label(bottomFrame, text="\n             Enter Message: \n", bg="tomato").pack(side=tk.LEFT)
    tkMessage = Text(bottomFrame, height=4, width=41)
    tkMessage.pack(side=LEFT, padx=(5, 5), pady=(5, 10))
    tkMessage.config(highlightbackground="firebrick1", state="disabled")
    tkMessage.bind("<Return>", (lambda event: getChatMessage(tkMessage.get("1.0", END))))
    # Import the image using PhotoImage function
    click_btn = PhotoImage(file="sa.png")

    # Let us create a label for button event
    img_label = Label(image=click_btn)

    # Let us create a dummy button and pass the image
    button = Button(bottomFrame, image=click_btn)
    button.bind("<Return>", (lambda event: send_mssage_to_server(tkMessage.get("1.0", END))))
    button.pack(pady=(5, 10), padx=(0, 10))

    # bottomFrame.pack(side=tk.BOTTOM)
    bottomFrame.grid(row=3, column=0)

    def connect():
        global username, client
        if len(entName.get()) < 1:
            messagebox.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
        else:
            nickname = "Akhilesh"
            username = entName.get()
            connect_to_server(nickname)

    # network client
    client = None
    HOST_ADDR = "172.16.199.101"
    HOST_PORT = 55532

    def connect_to_server(name):
        global client, HOST_PORT, HOST_ADDR
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((HOST_ADDR, HOST_PORT))
            client.send(name.encode())  # Send name to server after connecting

            entName.config(state=NORMAL)
            btnConnect.config(state=NORMAL)
            tkMessage.config(state=NORMAL)

            # start a thread to keep receiving message from server
            # do not block the main thread :)
            threading._start_new_thread(receive_message_from_server, (client, "m"))
        except Exception as e:
            messagebox.showerror(title="ERROR!!!",
                                    message="Cannot connect to host: " + HOST_ADDR + " on port: " + str(
                                        HOST_PORT) + " Server may be Unavailable. Try again later")

    def receive_message_from_server(sck, m):
        while True:
            message = sck.recv(4096).decode()

            if not message: break

            # display message from server on the chat window

            # enable the display area and insert the text and then disable.
            # why? Apparently, tkinter does not allow us insert into a disabled Text widget :(
            texts = tkDisplay.get("1.0", END).strip()
            tkDisplay.config(state=NORMAL)
            if len(texts) < 1:

                tkD.insert(END, message)
                msg = denc(int(message[:message.find(':')]), int(message[message.find(':') + 1:message.find(';')]),
                           message[message.find(';') + 1:])
                tkDisplay.insert(END, msg)
            else:

                tkD.insert(END, "\n\n" + message)
                msg = denc(int(message[:message.find(':')]), int(message[message.find(':') + 1:message.find(';')]),
                           message[message.find(';') + 1:])
                tkDisplay.insert(END, "\n\n" + msg)

            tkDisplay.config(state=DISABLED)
            tkD.see(END)

            # print("Server says: " +from_server)
        tkD.see(END)
        sck.close()
        window1.destroy()

    def getChatMessage(msg):

        msg = msg.replace('\n', '')
        texts = tkDisplay.get("1.0", END).strip()

        # enable the display area and insert the text and then disable.
        # why? Apparently, tkinter does not allow use insert into a disabled Text widget :(
        tkDisplay.config(state=NORMAL)
        if len(texts) < 1:
            tkDisplay.insert(END, ":" + msg, "tag_your_message")  # no line
        else:
            tkDisplay.insert(END, "\n\n" + ":" + msg, "tag_your_message")

        tkDisplay.config(state=DISABLED)

        send_mssage_to_server(msg)

        tkDisplay.see(END)
        tkMessage.delete('1.0', END)

    def send_mssage_to_server(msg=""):
        client_msg = enc(str(msg))
        client.send(username.encode('ascii'))
        client.send(client_msg.encode('ascii'))
        if msg == "exit":
            client.close()
            window1.destroy()
        print("Sending message")

    window1.mainloop()

def forget_pass():

    def change_password():
        if user_entry.get() == '' or newpass_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('ERROR', "Fill all the fields", parent=window1)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('ERROR', "'Password' and 'Confirm Password' should be same", parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='revanth_654', database='userdata')
            mycursor = con.cursor()
            query = 'select * from userdata where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('ERROR', 'Incorrect Username', parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('CONGRATULATIONS', 'Password updated successfully', parent=window)
                window.destroy()

    window = Toplevel()
    window.title('FORGOT PASSWORD')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font=('arial', 18, 'bold'), bg='white', fg='magenta2')
    heading_label.place(x=480, y=60)

    userLabel = Label(window, text='Username', font=('arial', 12, 'bold'), bg='white' , fg='orchid1')
    userLabel.place(x=470, y=130)
    user_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='magenta2')
    user_entry.place(x=470, y=160)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

    passwordLabel = Label(window, text='New Password', font=('arial', 12, 'bold'), fg='orchid1', bg='white')
    passwordLabel.place(x=470, y=210)

    newpass_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='magenta2')
    newpass_entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    confirmpassLabel = Label(window, text='Confirm Password', font=('arial', 12, 'bold'), fg='orchid1', bg='white')
    confirmpassLabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='magenta2')
    confirmpass_entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    submitButton = Button(window, text='Submit', font=('Open Sans', 16, 'bold'), fg='white', bg='magenta2', activebackground='magenta2', activeforeground='white', cursor='hand2', bd=0, width=19, command=change_password)
    submitButton.place(x=470, y=390)


    window.mainloop()




login_window = Tk()
login_window.geometry("990x660+50+50")
login_window.resizable(0,0)
login_window.title("SECCON CHAT")



bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=580, y=282)
openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

forgetButton = Button(login_window, text='Forgot Password?', font=('Microsoft Yahei UI Light', 9, 'bold'), bd=0, bg='white', fg='firebrick1', activebackground='white', activeforeground='firebrick1', cursor='hand2', command=forget_pass)
forgetButton.place(x=715, y=295)

loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1', activebackground='firebrick1', activeforeground='white', cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=578, y=350)

orLabel = Label(login_window, text='------------------OR------------------', font=('Open Sans',16), fg='firebrick1', bg='white')
orLabel.place(x=560, y=400)

facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640, y=440)

google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=690, y=440)

twitter_logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=740, y=440)

signupLabel = Label(login_window, text="Dont have an account?", font=('Open Sans',9,'bold'), fg='firebrick1', bg='white')
signupLabel.place(x=590, y=500)

newaccountButton = Button(login_window, text='Create a new one', font=('Open Sans', 9, 'bold underline'), fg='blue', bg='white', activebackground='white', activeforeground='blue', cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=727, y=500)



login_window.mainloop()