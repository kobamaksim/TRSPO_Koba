import socket

def start_server():
    port = 12345  # Порт, на якому працює сервер
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)

    print("Сервер запущено, очікування підключення...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Підключено клієнта: {client_address}")

            # Обробка повідомлень
            with client_socket:
                message = client_socket.recv(1024).decode('utf-8')
                print(f"Отримано повідомлення: {message}")

                # Відповідь клієнту
                response = f"Сервер отримав ваше повідомлення: {message}"
                client_socket.sendall(response.encode('utf-8'))

                print("Відповідь надіслано.")
    except KeyboardInterrupt:
        print("\nСервер зупинено.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
