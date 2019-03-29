from flask import *
from random import randint
from takevalues import *
import os
import requests
app = Flask(__name__)

# a = sensor("/dev/ttyACM0")
# os.chdir("/home/pi/mjpg-streamer")
# cameraOnCommand = "sudo /home/pi/mjpg-streamer/mjpg_streamer -i \"/home/pi/mjpg-streamer/input_uvc.so -f 10 -r 640x320 -n -y\" -o \"/home/pi/mjpg-streamer/output_http.so -w ./www -p 80\"&"
# os.system("LD_LIBRARY_PATH=~/mjpg-streamer")
# os.system(cameraOnCommand)
# os.chdir("/home/pi/Desktop/flask")
lq=0

@app.route("/")
def hello():
	return "enter / sensors"


@app.route("/<string:c>/<string:b>")
def portt(c,b):
	print c+"/"+b
	global opened_port
	opened_port = sensor("/"+c+"/"+b)
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
		q = opened_port.takeValue()
		print "1   "+str(q)
		return render_template('ultrasonic.html', val=q)	
	if text=="2":
		q = opened_port.takeUltrasonicValue2()
		print "2   "+str(q)
		return render_template('ultrasonic2.html', val=q)
	if text[0]=="3":
		print("Forward")
		q = opened_port.sendMotor("3")
		return render_template('m.html', val=q)
	if text[0]=="4":
		print("Stop")
		q = opened_port.sendMotor("4")
		return render_template('m.html', val=q)
	if text[0]=="5":
		print("Back")
		q = opened_port.sendMotor("5")
		return render_template('m.html', val=q)
	# if text=="3":
	# 	q = opened_port.takeUltrasonicValue2()
	# 	print "3   "+str(q)
	# 	return render_template('ultrasonic2.html', val=q)	
	 
if __name__ == "__main__":
	app.debug=True
	app.run(host='0.0.0.0')