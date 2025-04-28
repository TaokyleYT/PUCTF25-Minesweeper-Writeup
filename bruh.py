from pwn import *
while True:
    p = remote("158.132.12.250", 31337)
    p.recv(628)
    p.send(bytes([1, 0, 0]))
    msg = p.recvall()
    if b"BOOM! That cell contains a mine. You lose." in msg:
        p.close()
        continue
    else:
        print(msg)
        break