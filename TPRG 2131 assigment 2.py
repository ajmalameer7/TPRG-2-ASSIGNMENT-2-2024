import socket
import os
import json

def get_core_temp():
    return os.popen('vcgencmd measure_temp').readline().strip()

def get_gpu_temp():
    return os.popen('vcgencmd measure_temp gpu').readline().strip()

def get_cpu_freq():
    return os.popen('vcgencmd measure_clock arm').readline().strip()

def get_gpu_mem():
    return os.popen('vcgencmd get_mem gpu').readline().strip()

def get_throttled_state():
    return os.popen('vcgencmd get_throttled').readline().strip()

s = socket.socket()
host = ''  # Localhost
port = 5000
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    
    # Collect data from functions
    data = {
        "Core Temperature": get_core_temp(),
        "GPU Temperature": get_gpu_temp(),
        "CPU Frequency": get_cpu_freq(),
        "GPU Memory": get_gpu_mem(),
        "Throttled State": get_throttled_state()
    }
    
    # Convert dictionary to JSON and send to client
    res = bytes(json.dumps(data), 'utf-8')
    c.send(res)
    c.close()