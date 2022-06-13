# remote-shutdown
Shutdown any computer remotely

# Modules
* socket
* os

Since this is a client-server based program, there will be two files:- `client.py` and `server.py`. The one whose computer shall be shutted down must be running `server.py`.

`server.py`
```py
import socket
import os


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',4321))
s.listen(5)

while True:
    cs, address = s.accept()
    os.system("shutdown /s /t 1")
```

Let us now have a look at the `client.py` file.
```py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


target = input("Enter target ip:")
target_port = input("Enter port: ")
print("")

if target == "":
    print("Target cannot be empty.")
    print("")
    quit()

IP = target
PORT = target_port

try:
    print(f'Attempting to shutdown {IP}:{PORT} remotely.\n')
    s.connect((IP,PORT))
except:
    print('FAILED')
    print("Either the reciever is offline, or the address enter is incorrect")
    quit()

s.send(bytes(target,'utf-8'))
print("Remote shutdown successfull.")
```
Note: The `server.py` should be ran before `client.py` is run.

If the program ran with no issues, the output would be as follows:
```
Remote shutdown successfull
``` 
