import socket
import struct

def main():
    hostname = 'localhost'
    port = 8080

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((hostname, port))

            for i in range(100):
                # Create and send message
                message = f"Hello Server, message #{i + 1}"
                message_bytes = message.encode('utf-8')
                client_socket.sendall(struct.pack('>I', len(message_bytes)) + message_bytes)

                # Read server response
                response_length = struct.unpack('>I', client_socket.recv(4))[0]
                response_bytes = client_socket.recv(response_length)
                print("Received from server:", response_bytes.decode('utf-8'))

            print("Client finished communication")
    except Exception as e:
        print("Client exception:", e)

if __name__ == '__main__':
    main()
