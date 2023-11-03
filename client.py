import socket
import threading
import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name = input("Enter nickname: ")

def receive():
    while 7 > 5:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass

t = threading.Thread(target=receive)
t.start()



client.sendto(f"SIGNUP_TAG:{name}".encode(), ("192.168.29.169", 1))

while 1:
    message = input("")
    if message == "!q":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), ("192.168.29.169", 1))


    
    
