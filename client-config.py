import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Error receiving message.")
            break

# Set up the client
host = '127.0.0.1'  # Use the server's IP address or hostname
port = 5555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Send messages to the server or private messages to a specific user
while True:
    message = input()
    if message.startswith('/msg '):
        recipient, private_message = message[5:].split(' ', 1)
        client_socket.send(f'/msg {recipient} {private_message}'.encode('utf-8'))
    else:
        client_socket.send(message.encode('utf-8'))
