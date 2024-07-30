import tkinter as tk
import requests
import threading
import time

class ClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Status")

        # Erstelle und platziere das Label für die Anzahl der verbundenen Clients
        self.label = tk.Label(root, text="Anzahl verbundener Clients: 0", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Starte den Hintergrund-Thread, der regelmäßig die Anzahl der Clients abfragt
        self.running = True
        self.update_thread = threading.Thread(target=self.update_client_count)
        self.update_thread.start()

    def update_client_count(self):
        server_url = 'http://127.0.0.1:12345/clients'
        while self.running:
            try:
                response = requests.get(server_url)
                data = response.json()
                count = data['connected_clients']
                self.label.config(text=f"Anzahl verbundener Clients: {count}")
            except requests.RequestException as e:
                self.label.config(text="Fehler beim Abrufen der Client-Zahl")
            time.sleep(5)

    def on_closing(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
