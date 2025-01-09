import socket

HOST = 'localhost'  # Адреса сервера
PORT = 12345        # Порт сервера

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Підключено до сервера.")
    
    message = "IASA!"
    client_socket.sendall(message.encode('utf-8'))
    print(f"Надіслано повідомлення: {message}")
    
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Отримано відповідь від сервера: {response}")
