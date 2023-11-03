import socket
import queue
import threading

messages = queue.Queue()
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("192.168.29.169", 9999))

def recieve():
    while 5 < 6:
        try:
            message, address = server.recvfrom(1024)
            messages.put((message, address))
        except:
            pass

def broadcast():
    while 4 < 5:
        while messages.empty == False:
            message, address = messages.get()
            print(message.decode())
            if address not in clients:
                clients.append(address)
            for client in clients:
                try:

                    if message.decode().startswith("SIGNUP_TAG:"):
                        name = message.decode()[message.decode().index(":")+1:]
                        server.sendto(f"{name} joined!".encode(), client)
                    else:
                        server.sendto(message, client)
                except:
                    clients.remove(client)

t1 = threading.Thread(target=recieve)
t2 = threading.Thread(target=broadcast)

t1.start()
t2.start()