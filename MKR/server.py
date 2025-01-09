import socket
import threading
import struct

HOST = 'localhost'
PORT = 8080
THREAD_POOL_SIZE = 10

def handle_client(client_socket):
    try:
        data = client_socket.recv(12)  # 3 int по 4 байта
        N, M, L = struct.unpack('iii', data)

        if M <= 0 or N <= 0 or L <= 0:
            client_socket.sendall(b"Invalid matrix dimensions")
            client_socket.close()
            return

        matrix_a = []
        for i in range(N):
            row = struct.unpack(f'{M}i', client_socket.recv(M * 4))
            matrix_a.append(row)

        matrix_b = []
        for i in range(M):
            row = struct.unpack(f'{L}i', client_socket.recv(L * 4))
            matrix_b.append(row)

        print(f"Received matrices: A({N}x{M}), B({M}x{L})")


        result_matrix = multiply_matrices(matrix_a, matrix_b)

        for row in result_matrix:
            client_socket.sendall(struct.pack(f'{len(row)}i', *row))

        print("Result matrix sent to client.")
    except Exception as e:
        print(f"Client handling exception: {e}")
    finally:
        client_socket.close()

def multiply_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_b[0])
    common = len(matrix_a[0])
    result = [[0] * cols for _ in range(rows)]

    def compute_row(row):
        for j in range(cols):
            for k in range(common):
                result[row][j] += matrix_a[row][k] * matrix_b[k][j]

    threads = []
    for i in range(rows):
        thread = threading.Thread(target=compute_row, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(THREAD_POOL_SIZE)
        print(f"Server is running on port {PORT}")

        while True:
            client_socket, _ = server_socket.accept()
            print("New client connected")
            threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()