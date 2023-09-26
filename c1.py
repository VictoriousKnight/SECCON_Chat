import tkinter as tk
from tkinter import messagebox
import socket
import threading

window = tk.Tk()
window.title("Connected to Seccon")
username = " "


topFrame = tk.Frame(window)
lblName = tk.Label(topFrame, text = "Name to Connect With:").pack(side=tk.LEFT)
entName = tk.Entry(topFrame)
entName.pack(side=tk.LEFT)
btnConnect = tk.Button(topFrame, text="Connect", command=lambda : connect())
btnConnect.pack(side=tk.LEFT)
#btnConnect.bind('<Button-1>', connect)
topFrame.pack(side=tk.TOP)

displayFrame = tk.Frame(window)
lblLine = tk.Label(displayFrame, text="*********************************************************************").pack()
scrollBar = tk.Scrollbar(displayFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(displayFrame, height=20, width=55)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
tkDisplay.tag_config("tag_your_message", foreground="blue")
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F2F3F2", highlightbackground="grey", state="disabled")
displayFrame.pack(side=tk.TOP)


bottomFrame = tk.Frame(window)
tkMessage = tk.Text(bottomFrame, height=2, width=55)
tkMessage.pack(side=tk.LEFT, padx=(5, 13), pady=(5, 10))
tkMessage.config(highlightbackground="red", state="disabled")
tkMessage.bind("<Return>", (lambda event: getChatMessage(tkMessage.get("1.0", tk.END))))
bottomFrame.pack(side=tk.BOTTOM)


def connect():
    global username, client
    if len(entName.get()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You Must Enter User to Connect with")
    else:
        username = entName.get()
        connect_to_server(username)


# network client
client = None
HOST_ADDR = "172.16.199.101"
HOST_PORT = 55124

def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))

        # start a thread to keep receiving message from server
        # do not block the main thread :)
        threading._start_new_thread(receive)
    except Exception as e:
        tk.messagebox.showerror(title="ERROR!!!", message="Cannot connect to host: " + HOST_ADDR + " on port: " + str(HOST_PORT) + " Server may be Unavailable. Try again later")

def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            nickname="Shivam"
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                entName.config(state=tk.DISABLED)
                btnConnect.config(state=tk.DISABLED)
                tkMessage.config(state=tk.NORMAL)
                write_thread = threading.Thread(target=write)
                write_thread.start()
            else:
                texts = tkDisplay.get("1.0", tk.END).strip()
                tkDisplay.config(state=tk.NORMAL)
                if len(texts) < 1:
                    tkDisplay.insert(tk.END, message)
                else:
                    tkDisplay.insert(tk.END, "\n\n" + message)

                tkDisplay.config(state=tk.DISABLED)
                tkDisplay.see(tk.END)
                print(message)
                print(denc(int(message[:message.find(':')]), int(message[message.find(':')+1:message.find(';')]),message[message.find(';')+1:]))
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

    sck.close()
    window.destroy()


def getChatMessage(msg):

    msg = msg.replace('\n', '')
    texts = tkDisplay.get("1.0", tk.END).strip()

    # enable the display area and insert the text and then disable.
    # why? Apparently, tkinter does not allow use insert into a disabled Text widget :(
    tkDisplay.config(state=tk.NORMAL)
    if len(texts) < 1:
        tkDisplay.insert(tk.END, "You->" + msg, "tag_your_message") # no line
    else:
        tkDisplay.insert(tk.END, "\n\n" + "You->" + msg, "tag_your_message")

    tkDisplay.config(state=tk.DISABLED)

    write(msg)

    tkDisplay.see(tk.END)
    tkMessage.delete('1.0', tk.END)


def write(msg):
    while True:
        enc_msg = enc(msg)
        print(enc_msg)
        user_to_connect=username
        client.send(user_to_connect.encode('ascii'))
        client.send(enc_msg.encode('ascii'))

window.mainloop()