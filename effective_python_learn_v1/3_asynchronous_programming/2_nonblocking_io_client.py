import socket

if __name__ == '__main__':
    sock = socket.socket()
    
    host = socket.gethostname()
    port = 8869
    # connect must be placed before setblocking 
    sock.connect((host, port))
    # non-blocking
    sock.setblocking(0)

    #sock.connect((host, port))

    data = b"Ming-"*10*1024

    assert sock.send(data)
    
    print('I am NOT blocked')
    
