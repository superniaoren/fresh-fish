import socket

if __name__ == '__main__':
    sock = socket.socket()

    host = socket.gethostname()
    port = 8869

    sock.bind((host, port))
    sock.listen(5)

    while True:
        conn, attr = sock.accept()
        data = conn.recv(1024)
        while data:
            print(data)
            data = conn.recv(1024)
        print('Server NOT blocked')
        conn.close()
        break
