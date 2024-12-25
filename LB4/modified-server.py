import socket


def handle_client(client_socket, client_address):
    print(f"Connected by {client_address}")
    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            client_socket.sendall(data)


def modified_server(host='127.0.0.1', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")
        while True:
            client_socket, client_address = server_socket.accept()
            handle_client(client_socket, client_address)


if __name__ == "__main__":
    modified_server()