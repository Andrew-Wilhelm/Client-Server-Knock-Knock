import socket


def joke():
    serversocket.send("Knock Knock".encode())
    while True:
        msg = serversocket.recv(1024).decode()
        if msg == "who's there":
            serversocket.send(knock.clues[knock.i].encode())
        elif msg == knock.whoLine[knock.i]:
            serversocket.send(knock.punchLine[knock.i].encode())
            knock.i = knock.i + 1
            break
        elif msg == "close":
            serversocket.close()
            break


class KnockKnock:
    clues = ["A little old lady", "Euripides", "Snow", "Hawaii"]
    punchLine = ["Hey, you can yodel!", "Euripides clothes, you pay for them!", "Snow use. The joke is over",
                 "I’m good. Hawaii you?"]
    whoLine = ["A little old lady who", "Euripides who", "Snow who", "Hawaii who"]
    i = 0

    # infinite loop - until interrupt or error


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
knock = KnockKnock()
while True:
    # Establish connection for our simple server
    serversocket, addr = simple.accept()
    print(f"Connection accepted from {addr}")
    # Send message confirming connection
    # clientsocket.send("You were successfully connected".encode())
    # We're closing after a single send event and then disconnecting (no infinite loop)

    while True:
        joke()
        serversocket.send("Do you want to hear another?".encode())
        jokemsg = serversocket.recv(1024).decode()
        if knock.i <= 3:
            if jokemsg == 'no':
                serversocket.send("close".encode())
                serversocket.close()
                break
            continue
        serversocket.send("close".encode())
        serversocket.close()
        break
