import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Check if the message is a private message
            if data.startswith('/msg '):
                recipient, message = data[5:].split(' ', 1)
                send_private_message(client_socket, client_address, recipient, message)
            else:
                print(f"Received message from {client_address}: {data}")

                # Broadcast the message to all connected clients
                broadcast(data)
        except:
            break

    # Remove the client from the list when they disconnect
    clients.remove((client_socket, client_address))
    client_socket.close()

def broadcast(message):
    for client, _ in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            # Remove the client if unable to send message
            clients.remove((client, _))

def send_private_message(sender_socket, sender_address, recipient, message):
    for client, address in clients:
        if address[0] == recipient:
            try:
                client.send(f"Private message from {sender_address[0]}: {message}".encode('utf-8'))
                return
            except:
                # Remove the client if unable to send private message
                clients.remove((client, address))

# Set up the server
host = '0.0.0.0'  # Listen on all available interfaces
port = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"[*] Listening on {host}:{port}")

# List to store connected clients (client socket, client address)
clients = []

# Accept and handle incoming connections
while True:
    client, addr = server.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    # Add the new client to the list
    clients.append((client, addr))

    # Create a thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client, addr))
    client_handler.start()
