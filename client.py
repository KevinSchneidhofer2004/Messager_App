"""The client.py file."""
import socket


def send_message(message):
    """Send a message to the server."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))
    client.send(message.encode('utf-8'))
    client.close()


if __name__ == "__main__":
    while True:
        user_input = input("Enter message to send to the server: ")
        if user_input.lower() == 'exit':
            break
        send_message(user_input)
