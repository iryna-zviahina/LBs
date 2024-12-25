import socket


def file_sender_client(server_host="127.0.0.1", server_port=8080, file_to_send="file_to_send.txt"):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_host, server_port))
            print(f"Connected to server {server_host}:{server_port}")

            with open(file_to_send, "rb") as file:
                while chunk := file.read(1024):
                    client_socket.sendall(chunk)

            print(f"File '{file_to_send}' sent successfully!")
    except FileNotFoundError:
        print(f"Error: File '{file_to_send}' not found.")


if __name__ == "__main__":
    file_sender_client()
