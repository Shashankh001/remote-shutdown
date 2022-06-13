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