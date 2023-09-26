import tkinter as tk
from tkinter import messagebox
import socket
import threading
import random
import time
from PIL import ImageTk,Image




window = tk.Tk()
window.title("Client")

window.configure(bg="firebrick1")


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
        return str(choice)+":"+str("01012305104689704578546987123654")+";"+cyphertext
    elif choice == 5:
        return str(choice)+":"+str("45154788956258895626369845155487")+";"+cyphertext

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
        return str(choice)+":"+str(key)+";"+cyphertext

    elif choice == 2:
        input_str = msgg
        output_str = ""
        key = str(random.randint(1, 9999))
        for i, char in enumerate(input_str):
            output_str += chr(ord(char) ^ ord(key[i % len(key)]))
        return str(choice)+":"+str(key)+";"+output_str

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
        return str(choice)+":"+str(key)+";"+cyphertext
    elif choice == 4:
        return cyphertext
    elif choice == 5:
        return cyphertext


topFrame = tk.Frame(window, bg='firebrick1')
lblName = tk.Label(topFrame, text = "                             Name:", bg='tomato').pack(side=tk.LEFT)
entName = tk.Entry(topFrame,width=57,background="coral")
entName.pack(side=tk.LEFT, fill=tk.Y, padx=(6, 0), pady=(5, 5))
btnConnect = tk.Button(topFrame, text="Connect", command=lambda : connect())
btnConnect.pack(side=tk.LEFT,padx=(5, 13), pady=(5, 10))
#btnConnect.bind('<Button-1>', connect)
#topFrame.pack(side=tk.TOP)
topFrame.grid(row=0, column=0)

dFrame=tk.Frame(window, bg='firebrick1')
lblName = tk.Label(dFrame, text = "              Encrypted Text:",bg="tomato").pack(side=tk.LEFT)
tkD = tk.Text(dFrame, height=0.1, width=50)
tkD.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 13), pady=(5, 10))
#dFrame.pack(side=tk.TOP)
dFrame.grid(row=1, column=0)
var = tk.StringVar()
var.set("0")
displayFrame = tk.Frame(window, bg='tomato')
#lblLine = tk.Label(displayFrame, text="*********************************************************************").pack()
scrollBar = tk.Scrollbar(displayFrame,activebackground="firebrick1")
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(displayFrame, height=20, width=50)
tkDisplay.pack(side=tk.RIGHT, fill=tk.Y, padx=(5, 0))
tkDisplay.tag_config("tag_your_message", foreground="red")
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="firebrick1", highlightbackground="firebrick1", state="disabled")
tkDisplay.config(yscrollcommand=scrollBar.set, background="coral", highlightbackground="firebrick1", state="disabled")
#displayFrame.pack(side=tk.TOP)
displayFrame.grid(row=2, column=0)

RFrame=tk.Frame(window,bg="firebrick1")
lblName = tk.Label(displayFrame, text = "\nEncryption Algo:",bg="tomato").pack(padx=(5, 13), pady=(5, 10))
radio = tk.Radiobutton(displayFrame, text="Ceaser Cipher", padx=14, variable=var, value="1", bg='tomato').pack(anchor="w")
radio = tk.Radiobutton(displayFrame, text="XOR Encrypt", padx=14, variable=var, value="2", bg='tomato').pack(anchor="w")
radio = tk.Radiobutton(displayFrame, text="Reverse Ceaser", padx=14, variable=var, value="3", bg='tomato').pack(anchor="w")
radio = tk.Radiobutton(displayFrame, text="DES Encrypt", padx=14, variable=var, value="4", bg='tomato').pack(anchor="w")
radio = tk.Radiobutton(displayFrame, text="RSA Encrypt", padx=14, variable=var, value="5", bg='tomato').pack(anchor="w")
#RFrame.pack(side=tk.TOP)
RFrame.grid(row=2, column=0)



bottomFrame = tk.Frame(window, bg='firebrick1')
lblName = tk.Label(bottomFrame, text = "\n             Enter Message: \n",bg="tomato").pack(side=tk.LEFT)
tkMessage = tk.Text(bottomFrame, height=4, width=41,background="coral")
tkMessage.pack(side=tk.LEFT, padx=(5, 5), pady=(5, 10))
tkMessage.config(highlightbackground="firebrick1", state="disabled")
tkMessage.bind("<Return>", (lambda event: getChatMessage(tkMessage.get("1.0", tk.END))))
#Import the image using PhotoImage function
click_btn= tk.PhotoImage(file="sa.png")

#Let us create a label for button event
img_label= tk.Label(image=click_btn)

#Let us create a dummy button and pass the image
button= tk.Button(bottomFrame, image=click_btn)
button.bind("<Return>", (lambda event: send_mssage_to_server(tkMessage.get("1.0", tk.END))))
button.pack(pady=(5,10),padx=(0,10))

#bottomFrame.pack(side=tk.BOTTOM)
bottomFrame.grid(row=3, column=0)


def connect():
    global username, client
    if len(entName.get()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
    else:
        nickname="Akhilesh"
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
        client.send(name.encode()) # Send name to server after connecting

        entName.config(state=tk.NORMAL)
        btnConnect.config(state=tk.NORMAL)
        tkMessage.config(state=tk.NORMAL)

        # start a thread to keep receiving message from server
        # do not block the main thread :)
        threading._start_new_thread(receive_message_from_server, (client, "m"))
    except Exception as e:
        tk.messagebox.showerror(title="ERROR!!!", message="Cannot connect to host: " + HOST_ADDR + " on port: " + str(HOST_PORT) + " Server may be Unavailable. Try again later")


def receive_message_from_server(sck, m):
    while True:
        message = sck.recv(4096).decode()

        if not message: break

        # display message from server on the chat window

        # enable the display area and insert the text and then disable.
        # why? Apparently, tkinter does not allow us insert into a disabled Text widget :(
        texts = tkDisplay.get("1.0", tk.END).strip()
        tkDisplay.config(state=tk.NORMAL)
        if len(texts) < 1:

            tkD.insert(tk.END, message)
            msg=denc(int(message[:message.find(':')]),int(message[message.find(':') + 1:message.find(';')]),message[message.find(';') + 1:])
            tkDisplay.insert(tk.END, msg)
        else:

            tkD.insert(tk.END, "\n\n" + message)
            msg = denc(int(message[:message.find(':')]), int(message[message.find(':') + 1:message.find(';')]),message[message.find(';') + 1:])
            tkDisplay.insert(tk.END, "\n\n"+ msg)

        tkDisplay.config(state=tk.DISABLED)
        tkD.see(tk.END)

        # print("Server says: " +from_server)
    tkD.see(tk.END)
    sck.close()
    window.destroy()


def getChatMessage(msg):

    msg = msg.replace('\n', '')
    texts = tkDisplay.get("1.0", tk.END).strip()

    # enable the display area and insert the text and then disable.
    # why? Apparently, tkinter does not allow use insert into a disabled Text widget :(
    tkDisplay.config(state=tk.NORMAL)
    if len(texts) < 1:
        tkDisplay.insert(tk.END, ":" + msg, "tag_your_message") # no line
    else:
        tkDisplay.insert(tk.END, "\n\n" + ":" + msg, "tag_your_message")

    tkDisplay.config(state=tk.DISABLED)

    send_mssage_to_server(username+":"+msg)

    tkDisplay.see(tk.END)
    tkMessage.delete('1.0', tk.END)


def send_mssage_to_server(msg=""):
    client_msg = enc(str(msg))
    client.send(username.encode('ascii'))
    client.send(client_msg.encode('ascii'))
    if msg == "exit":
        client.close()
        window.destroy()
    print("Sending message")


window.mainloop()