import socket
import sys
import threading
from pyexpat.errors import messages

HOST = '0.0.0.0'
PORT = 21002
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except OSError as msg:
    s = None
    print(f"Error creating socket: {msg}")
    exit(1)

try:
    s.bind((HOST, PORT))
    s.listen()
    print("Socket bound and listening")
except OSError as msg:
    print("Error binding/listening!")
    s.close()
    exit(1)


def send_message_function(client_socket):
    while True:
        message = input("Enter a message: ")
        client_socket.send((message + "\n").encode())
        


conn, addr = s.accept()
with conn:
    print('Connection accepted from ', addr)
    
    send_thread = threading.Thread(target=send_message_function, args=(conn,))
    send_thread.start()

    while True:
        # message = input("Enter a message: ")
        # s.send((message+"\n").encode())

        message_received = ""
        while True:
            data = conn.recv(32)
            if data:
                print('Received data chunk from server: ', repr(data))
                message_received += data.decode()
                if message_received.endswith("\n"):
                    print("End of message received")
                    break
            else:
                print("Connection lost!")
                break
        if not message_received:
            break

        print("Received message: ", message_received)

s.close()
print("Server finished")