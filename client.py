import socket
import time

def get_connected_clients(server_host='127.0.0.1', server_port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_host, server_port))
        while True:
            try:
                # Anfrage an den Server, um die Anzahl der verbundenen Clients zu erhalten
                client_socket.send(b'GET_COUNT')
                response = client_socket.recv(1024).decode()
                print(f"Anzahl verbundener Clients: {response}")
                time.sleep(5)
            except (ConnectionResetError, ConnectionRefusedError):
                print("Verbindung zum Server unterbrochen.")
                break

if __name__ == "__main__":
    get_connected_clients()
