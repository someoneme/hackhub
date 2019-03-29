import serial
import time
ser = serial.Serial()
ser.baudrate = 9600
ser.port = "/dev/serial0"
ser.timeout=10

class gps():
	def __init__(self):
		# ser.port = portName
		self.i=0

	def gpsvaluesLat(self):
		while 1:
			try:
				ser.open()
				#ser.flush()
				i = ser.readline()
				if i.split(',')[0]=='$GPGGA':
					print(i.split(',')[2])
					# print i.split(',')[2], i.split(',')[4]
					return i.split(',')[2]
					
			except KeyboardInterrupt as e:
				print("kkkk")
	#			print(e)
				ser.close()
				break
			except Exception as e:
				# return 1
				# print("Error.... wait")
				# print(e)
				ser.close()
				continue
			ser.close()
	def gpsvaluesLon(self):
		while 1:
			try:
				ser.open()
				#ser.flush()
				i = ser.readline()
				if i.split(',')[0]=='$GPGGA':
					# print i.split(',')[2], i.split(',')[4]
					return i.split(',')[4]
					
			except KeyboardInterrupt as e:
				print("kkkk")
	#			print(e)
				ser.close()
				break
			except Exception as e:
				# print("Error.... wait")
				# print(e)
				ser.close()
				continue
			ser.close()

	# def takeIrValue(self):
	# 	ser.write("2")
	# 	self.val = ser.readline()
	# 	return self.val

	

# a = gps()
# print(a.gpsvaluesLat())
# while 1:
# 	print str(a.takeValue())+" "+str(a.takeIrValue())

