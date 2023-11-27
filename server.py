"""The server.py file."""
import socket
import threading


def handle_client(client_socket, client_address):
    """Handle the requests from the clients."""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))

    client_socket.close()


def start_server():
    """Start the server and listen to client messages."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("[*] Listening on 0.0.0.0:5555")

    while True:
        client, addr = server.accept()
        client_handler = threading.Thread(target=handle_client,
                                          args=(client, addr))
        client_handler.start()


if __name__ == "__main__":
    start_server()
