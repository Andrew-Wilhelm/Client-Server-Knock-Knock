import socket

knocking = {
    1: "A little old lady",
    2: "Euripides",
    3: "Snow",
    4: "Hawaii",
    "A little old lady who": "Hey, you can yodel!",
    "Euripides who": "Euripides clothes, you pay for them!",
    "Snow who": "Snow use. The joke is over",
    "Hawaii who": "I’m good. Hawaii you?"
}


# with connection
def joke(j):
    serversocket.send("Knock Knock".encode())
    done = "not"
    while True:
        msg = serversocket.recv(1024).decode()
        if msg == "who's there":
            serversocket.send(knocking[j].encode())
        elif msg not in knocking:
            serversocket.send("Improper response\n".encode())
            break
        elif j > 4:
            j = 1
        else:
            for key in knocking.keys():
                if msg == key:
                    serversocket.send(f"{knocking[key]}\nHear another!\n".encode())
                    done = "done"
        if done == "done":
            break
            # serversocket.send("Wrong Reply".encode())


# File to show cross-platform.
# Create a local "echo" server
# HOST = localhost IP, PORT = arbitrary number over 1023
HOST = socket.gethostbyname('localhost')
PORT = 12345
print(f"Our localhost ip is {HOST} and port is {PORT}")
# create a socket "instance" (object)
simple = socket.socket()
print("Socket created successfully")
# Bind to a port
simple.bind((HOST, PORT))
print(f"Socket is bound to {PORT}")
# once "bound" we must "listen"
simple.listen(5)
i = 1
while True:
    # Establish connection for our simple server
    serversocket, addr = simple.accept()
    print(f"Connection accepted from {addr}")
    # Send message confirming connection
    # clientsocket.send("You were successfully connected".encode())
    # We're closing after a single send event and then disconnecting (no infinite loop)
    while True:
        joke(i)
        i = i + 1
        if i > 4:
            i = 1
    serversocket.close()
