import socket
import struct
import random

HOST = 'localhost'
PORT = 8080

def generate_matrix(rows, cols):
    return [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))

            N, M, L = random.randint(1000, 2000), random.randint(1000, 2000), random.randint(1000, 2000)
            print(f"Generated matrices: A({N}x{M}), B({M}x{L})")

            matrix_a = generate_matrix(N, M)
            matrix_b = generate_matrix(M, L)

            client_socket.sendall(struct.pack('iii', N, M, L))

            for row in matrix_a:
                client_socket.sendall(struct.pack(f'{len(row)}i', *row))

            for row in matrix_b:
                client_socket.sendall(struct.pack(f'{len(row)}i', *row))

            result_matrix = []
            for _ in range(N):
                row = struct.unpack(f'{L}i', client_socket.recv(L * 4))
                result_matrix.append(row)

            print("Matrix multiplication result received.")
    except Exception as e:
        print(f"Client exception: {e}")

if __name__ == "__main__":
    main()