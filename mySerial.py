#!/usr/bin/python3
import serial
import threading
from flask_socketio import SocketIO

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)

def serial_start():
    stop_flag = False
    while not stop_flag:
        if ser.readable():
            res = ser.readline()
            res_decode = res.decode()
            print(res_decode)

def start_serial_thread():
    thread = threading.Thread(target=serial_start)
    thread.start()

