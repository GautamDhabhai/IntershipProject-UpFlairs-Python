import socket
import queue
import threading
import os

#a queue and a list for storing messages and client address
messages = queue.Queue()
clients = []

#binding the server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("192.168.29.169", 1))

#function to save chat history in a txt file
def save_chat_history(message, address):
    with open("chat_history.txt", "a") as chat_file:
        chat_file.write(f"{address}: {message.decode()}\n")
        
if not os.path.exists("chat_history.txt"):
    with open("chat_history.txt", "w"):
        pass

#function to recieve messages in the server and put in into message queue
def recieve():
    while 5 < 6:
        try:
            message, address = server.recvfrom(1024)
            messages.put((message, address))
            
            #calling save_chat
            save_chat_history(message, address)
        except:
            pass

#function for sending message to all of the clients
def broadcast():
    while 4 < 5:
        while messages.empty() == False:
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

#threading of recieve and breadcast started
t1 = threading.Thread(target=recieve)
t2 = threading.Thread(target=broadcast)

t1.start()
t2.start()
