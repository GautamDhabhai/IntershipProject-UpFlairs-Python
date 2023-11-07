import socket
import threading
import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#input name to be used in the group chat
name = input("Enter nickname: ")

#recieve messages of other clients from the server
def receive():
    while 7 > 5:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass

#threading of recieve started
t = threading.Thread(target=receive)
t.start()


#send first message that starts with SIGNUP_TAG to record your name in server
client.sendto(f"SIGNUP_TAG:{name}".encode(), ("192.168.29.169", 1))

#send chat message
while 1:
    message = input("")
    if message == "!q":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), ("192.168.29.169", 1))


    
    
