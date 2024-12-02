import socket
import json

s = socket.socket()
host = '192.168.10.111'  # Replace with your Raspberry Pi's IP address
port = 5000
s.connect((host, port))

response = s.recv(1024)
data = json.loads(response.decode('utf-8'))

print("Received Data from Server:")
for key, value in data.items():
    print(f"{key}: {value}")

s.close()
