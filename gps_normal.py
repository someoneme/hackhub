import serial
import time
ser = serial.Serial()
ser.baudrate = 9600
ser.port = "/dev/serial0"
ser.timeout=10
def roverGps():
	while 1:
		try:
			ser.open()
			#ser.flush()
			i = ser.readline()
			if i.split(',')[0]=='$GPGGA':
				print i.split(',')[2], i.split(',')[4]
				return [i.split(',')[2], i.split(',')[4]]
				#print i.split(',')[4]
#				break
#			print i
#			ser.close()
		except KeyboardInterrupt as e:
			print("kkkk")
#			print(e)
			ser.close()
			break
		except Exception as e:
			print("Error.... wait")
			print(e)
			ser.close()
			continue
		ser.close()

#while 1:
print roverGps()

