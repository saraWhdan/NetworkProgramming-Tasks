from socket import *

s = socket(AF_INET, SOCK_STREAM)
print("[*] socket created")

ip = '127.0.0.1'
port = 50000

s.connect((ip, port))
print("[*] Connected to server")

while True:
    x = input('Client : ')
    if x == 'q':
        print('[*] Bye')
        s.send(x.encode('utf-8'))
        break

    # Send the length of the message (fixed size: 10 bytes)
    message_data = x.encode('utf-8')
    message_length = str(len(message_data)).zfill(10).encode('utf-8')
    s.send(message_length)

    # Send the actual message
    s.send(message_data)

    # Receive the length of the message (fixed size: 10 bytes)
    length_data = s.recv(10)
    length = int(length_data.decode('utf-8'))

    # Receive the message with variable length
    received_message = s.recv(length).decode('utf-8')
    print("Server : " + received_message)

s.close()