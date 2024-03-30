from flask import Flask, render_template, request, jsonify, make_response
from threading import Thread, Lock
import time
import serial

import callssh

app = Flask(__name__)
app.config['DEBUG'] = False

ser = None
serial_message = ""
lock = Lock()

class SerialReadProgram(Thread):
    def __init__(self):
        super().__init__()
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        global ser
        global serial_message
        if ser is None or not ser.is_open:
            ser = serial.Serial("/dev/ttyS0", 9600, timeout=2)
            print("Serial Port Opened")
        else:
            print("Serial Port Already Opened")
        print("Serial Start")
        i = 0
        while self._running:
            with lock:
                try:
                    if i == 0:
                        time.sleep(5)
                        print("sensor start send")
                        ser.write(b'sensor start\n')
                    i+=1
                    if ser.in_waiting > 0:
                        serial_message = ser.readline().decode('utf-8').strip()
                        print(serial_message)
                        
                        # cam sensor call
                        if serial_message == "cam":
                            call_action_cam()
                        
                except serial.SerialException as e:
                    print(f"Serial Port Error: {e}")
                    time.sleep(0.5)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/serial_data')
def get_serial_data():
    global serial_message
    return jsonify({'data': serial_message})

@app.route('/call_action_cam')
def call_action_cam():
    remote_script_path = '/home/nsf/opencv-venv/opencv/samples/python/test.sh'
    result = callssh.execute_remote_sh('192.168.1.92', 22, 'nsf', '1234', remote_script_path)
    response = make_response(jsonify({'data': result}))
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response
    

serial_read = SerialReadProgram()
serial_read.start()

app.run(host='0.0.0.0', port=5000, debug=False)
