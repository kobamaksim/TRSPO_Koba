import socket

def start_client():
    server_address = 'localhost'  # Адреса сервера
    port = 12345  # Порт сервера

    try:
        with socket.create_connection((server_address, port)) as client_socket:
            print("Підключено до сервера.")

            # Відправлення повідомлення серверу
            message = "IASA!"
            client_socket.sendall(message.encode('utf-8'))
            print(f"Надіслано повідомлення: {message}")

            # Отримання відповіді від сервера
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Отримано відповідь від сервера: {response}")
    except ConnectionError as e:
        print(f"Помилка клієнта: {e}")

if __name__ == "__main__":
    start_client()
