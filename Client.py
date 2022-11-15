import socket

# Create a socket object
sclient = socket.socket()

# cross-platform, telnet-ish connection
PORT = 12345
HOST = socket.gethostbyname("localhost")
# in order to "connect" to a server - I must "connect" to its socket
sclient.connect((HOST, PORT))
# receive some data from our connected client (decode that string)
while True:
    msg = sclient.recv(1024).decode()
    print(f"Server: {msg}")
    evalmsg = msg[-1]
    if msg == "close":
        break
    # close connection
    if evalmsg == ".":
        data = input()
        if data == "close":
            sclient.sendall(data.encode())
            break
        sclient.sendall(data.encode())
sclient.close()
