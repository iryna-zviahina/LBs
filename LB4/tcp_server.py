import socket


def file_receiver_server(host="127.0.0.1", port=8080, output_file="received_file.txt"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connected by {client_address}")
            with client_socket:
                with open(output_file, "wb") as file:
                    while True:
                        data = client_socket.recv(1024)
                        if not data:
                            break
                        file.write(data)
            print(f"File received and saved as '{output_file}'")


if __name__ == "__main__":
    file_receiver_server()