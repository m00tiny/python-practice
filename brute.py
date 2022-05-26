import sys
import socket
import string
import itertools

target = sys.argv[1]
port = sys.argv[2]
port = int(port)
charset = string.ascii_letters + string.digits

bingo = True
while bingo:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    for x in range(1, 3):
        y = itertools.product(charset, repeat=x)
        for z in y:
            z = ''.join(z)
            s.send(z.encode())
            response = s.recv(1024).decode()
            if response == "Connection success!":
                print(z)
                bingo = False
