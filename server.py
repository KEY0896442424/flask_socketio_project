import socket
import threading

# Globale Variable zum Zählen der Verbindungen
connections = []

def handle_client(client_socket):
    global connections
    # Füge die neue Verbindung zur Liste hinzu
    connections.append(client_socket)
    try:
        while True:
            # Lese vom Client (optional)
            message = client_socket.recv(1024).decode()
            if not message:
                break
    finally:
        # Entferne die Verbindung, wenn sie geschlossen wird
        connections.remove(client_socket)
        client_socket.close()

def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server läuft auf {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Verbindung von {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
