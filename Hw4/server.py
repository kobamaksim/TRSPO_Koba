import socket

HOST = 'localhost'  # Локальний хост
PORT = 12345        # Порт, на якому працює сервер

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Сервер запущено, очікування підключення...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Підключено клієнта: {client_address}")
        with client_socket:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Отримано повідомлення: {message}")
            response = f"Сервер отримав ваше повідомлення: {message}"
            client_socket.sendall(response.encode('utf-8'))
            print("Відповідь надіслано.")
