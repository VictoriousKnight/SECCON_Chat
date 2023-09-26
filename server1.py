import tkinter as tk
import socket
import threading

window = tk.Tk()
window.title("SECCON-Sever")

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Connect", command=lambda : start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(topFrame, text="Stop", command=lambda : stop_server(), state=tk.DISABLED)
btnStop.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

# Middle frame consisting of two labels for displaying the host and port info
middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text = f"Host: Initializing....")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text = f"Port: Searching....")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

# The client frame shows the client area
clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="---------------------------CLIENT LIST---------------------------").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=15, width=40)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
tkDisplay.insert(tk.END, f"Server Initialized!\n")
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
clientFrame.pack(side=tk.BOTTOM, pady=(5, 10))

server = None
# Connection Data
host = '172.16.199.101'
port = 55532

# Lists For Clients and Their Nicknames
clients = []
clients_names = []
adresses = []
def start_server():
    global server
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(2)
    lblHost["text"] = "Host: " + host
    lblPort["text"] = "Port: " + str(port)
    threading._start_new_thread(receive,(server,))


def stop_server():
    global server
    btnStart.config(state=tk.NORMAL)
    btnStop.config(state=tk.DISABLED)

# Sending Messages To All Connected Clients
def broadcast(u=b"New User",message="Joined"):
    if u.decode('ascii') in clients_names:
        print(u)
        print(message)
        clients[clients_names.index(u.decode('ascii'))].send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            user_to_connect = client.recv(1024)
            message = client.recv(1024)
            broadcast(user_to_connect,message)
            #clients_names.append(clients_names)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = clients_names[index]
            broadcast(user_to_connect,"{} left!".format(nickname).encode('ascii'))
            clients_names.remove(nickname)
            break

def receive(server):
    while True:
        # Accept Connection
        client, address = server.accept()
        # print("Connected with {}".format(str(address)))
        #tkDisplay.insert(tk.END, "User 1\n")

        # Request And Store Nickname
        #client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        #tkDisplay.insert(tk.END, f"{address}:{nickname}--Connected!\n")
        clients_names.append(nickname)
        clients.append(client)
        adresses.append(address)

        # Print And Broadcast Nickname
        #print("Nickname is {}".format(nickname))
        #broadcast("{} joined!".format(nickname).encode('ascii'))
        # client.send('Connected to server!'.encode('ascii'))
        update_client_names_display(adresses,clients_names)

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def update_client_names_display(adresses,name_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete('1.0', tk.END)

    for c in name_list:
        tkDisplay.insert(tk.END, str(c)+" connected with IP: \n"+str(adresses[name_list.index(c)])+"\n\n")
    tkDisplay.config(state=tk.DISABLED)


window.mainloop()