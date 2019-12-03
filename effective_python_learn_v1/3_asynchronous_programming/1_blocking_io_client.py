## 
## ref link: https://luminousmen.com/post/asynchronous-programming-blocking-and-non-blocking
##

import socket

if __name__ == '__main__':
    print("test client-server example, to learn async programming. ")

    # blocking I/O; by defalut, tcp sockets are placed in a blocking mode.
    # client: 
    sock = socket.socket()

    host = socket.gethostname()
    port = 8868
    sock.connect((host, port))

    data = b"LamaTemple" * 10 * 1024
    assert sock.send(data)
    print("[client] Data has been sent.")
    
    
