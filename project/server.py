import socket
import threading
import json

HOST = '127.0.0.1'
PORT = 3737

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

def send_board_signal(conn):
    signal = {'signal': 'board'}
    conn.sendall(json.dumps(signal).encode())

def send_rules_signal(conn):
    signal = {'signal': 'rules'}
    conn.sendall(json.dumps(signal).encode())

def handle_client(conn, addr):
    connected = True
    while connected:
        msg = conn.recv(1024).decode('utf-8')
        if msg == 'quit':
            connected = False
        elif msg == 'pvp_button_pressed' or msg == 'pvai_button_pressed':
            # Sending signal for switching to board
            send_board_signal(conn)
        elif msg == 'rules_button_pressed':
            # Sending signal for showing rules
            send_rules_signal(conn)
        elif msg == 'quit_button_pressed':
            # Disconnect the client
            connected = False

    conn.close()

def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

start_server()
