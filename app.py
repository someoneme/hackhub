from flask import *
from random import randint
# from takevalues import *
import multiprocessing
from threading import Thread
from takeValueNew import *
import os
from multiprocessing import Process, Queue
import requests
result = multiprocessing.Array('f', 2)
app = Flask(__name__)
# global recv_end
# a = sensor("/dev/ttyACM0")
# os.chdir("/home/pi/mjpg-streamer")
# cameraOnCommand = "sudo /home/pi/mjpg-streamer/mjpg_streamer -i \"/home/pi/mjpg-streamer/input_uvc.so -f 10 -r 640x320 -n -y\" -o \"/home/pi/mjpg-streamer/output_http.so -w ./www -p 80\"&"
# os.system("LD_LIBRARY_PATH=~/mjpg-streamer")
# os.system(cameraOnCommand)
# os.chdir("/home/pi/Desktop/flask")
lq=0
ser_lora=serial.Serial()

@app.route("/")
def hello():
	return "enter / sensors"



@app.route("/<string:c>/<string:b>")
def portt(c,b):
	try:
		global ser_lora
		ser_lora = serial.Serial("/dev/ttyUSB0",115200,timeout=1)
		a = ser_lora.write("mac set_class A")
		time.sleep(1)
	# q = ser.read(ser.in_waiting)
	# print(q)
		a = ser_lora.write("mac join otaa")
	except:
		print("Lora not connected")
	print c+"/"+b
	global opened_port
	opened_port = sensor("/"+c+"/"+b)
	global qq
	# jobs = []
	# pipe_list = []
	# # global recv_end
	# i=1
	# global recv_end
	# p = multiprocessing.Process(target=opened_port.gpsvaluesLat, args=(i, send_end))
	# jobs.append(p)
	# pipe_list.append(recv_end)
	# p.start()
	# qq = Queue()
	# gpslat = Value("f", 2.0)
	# gpsData = gps()
	# t = Thread(target=opened_port.gpsvaluesLat)
	# t.start()
	# t.join()
	global result
	
	qqq = multiprocessing.Process(target=opened_port.gpsvaluesLat, args=(result,)).start()
	# print(opened_port.printgpsvaluesLat())
	# qq.start()
	# print a,b
	return render_template('web.html', **locals())

@app.route("/sensors")
def sensors():
	# q = a.takeValue()
	# print q
	score = randint(0,10)
	return render_template('web.html', **locals())

@app.route("/private")
def private():
	text = request.args.get('jsdata')
	if text=="1":
		global result
		q = opened_port.takeValue()
		print "1   "+str(q)
		return render_template('ultrasonic.html', val=q)	
	if text=="2":
		q = opened_port.takeUltrasonicValue2()
		print "2   "+str(q)
		return render_template('ultrasonic2.html', val=q)
	if text[0]=="3":
		q = opened_port.takeUltrasonicValue3()
		print "3   "+str(q)
		return render_template('ultrasonic2.html', val=q)
	if text[0]=="4":
		q = opened_port.takeUltrasonicValue4()
		print "4   "+str(q)
		return render_template('ultrasonic2.html', val=q)
	if text[0]=="a":
		q = opened_port.sendMotor("a")
		return render_template('m.html', val=q)
	if text[0]=="b":
		q = opened_port.sendMotor("b")
		return render_template('m.html', val=q)
	if text[0]=="c":
		q = opened_port.sendMotor("c")
		return render_template('m.html', val=q)
	if text[0]=="d":
		q = opened_port.sendMotor("d")
		return render_template('m.html', val=q)
	if text[0]=="e":
		q = opened_port.sendMotor("e")
		return render_template('m.html', val=q)
	if text[0]=="f":
		q = opened_port.sendMotor("f")
		return render_template('m.html', val=q)
	if text[0]=="g":
		q = opened_port.sendMotor("g")
		return render_template('m.html', val=q)
	if text[0]=="h":
		q = opened_port.sendMotor("h")
		return render_template('m.html', val=q)
	if text[0]=="i":
		q = opened_port.sendMotor("i")
		return render_template('m.html', val=q)
	if text[0]=="j":
		q = opened_port.sendMotor("j")
		return render_template('m.html', val=q)
	if text[0]=="k":
		q = opened_port.sendMotor("k")
		return render_template('m.html', val=q)
	

	

		
	 
if __name__ == "__main__":
	app.debug=True
	app.run(host='0.0.0.0')
