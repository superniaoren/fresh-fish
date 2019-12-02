## 
## ref link: https://luminousmen.com/post/asynchronous-programming-blocking-and-non-blocking
##

import socket

if __name__ == '__main__':
    print("test client-server example, to learn async programming. ")

    # blocking I/O; by defalut, tcp sockets are placed in a blocking mode.
    # server: 
    sock = socket.socket()

    host = socket.gethostname()
    port = 8868
    
    sock.bind((host, port))
    sock.listen(5)

    while True:
        conn, attr = sock.accept()
        data = sock.recv(1024)
        while data:
            print(data)
            data = sock.recv(1024)
        print("[server] Data have been received.")
        conn.close()
        break 
    
    
