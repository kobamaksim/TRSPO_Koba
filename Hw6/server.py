import socket
import struct

def main():
    port = 8080

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('', port))
            server_socket.listen(1)
            print(f"Server is listening on port {port}")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Client connected from {addr}")

                for i in range(100):
                    # Read message length
                    length = struct.unpack('>I', conn.recv(4))[0]

                    # Read message payload
                    message_bytes = conn.recv(length)
                    received_message = message_bytes.decode('utf-8')
                    print("Received from client:", received_message)

                    # Respond to client
                    response_message = f"Message {i + 1} received"
                    response_bytes = response_message.encode('utf-8')
                    conn.sendall(struct.pack('>I', len(response_bytes)) + response_bytes)

                print("Server finished communication")
    except Exception as e:
        print("Server exception:", e)

if __name__ == '__main__':
    main()
