import serial
# import thread
import multiprocessing
from multiprocessing import Process, Queue
import time
ser = serial.Serial()
ser.baudrate = 9600
ser.timeout=10

ser1 = serial.Serial()
ser1.baudrate = 9600
ser1.port = "/dev/serial0"
ser1.timeout=10
# global qq
# lat=123
# qq = Queue()
# ll = []
# global lat
# lat=100
class sensor():
	def __init__(self,portName):

		ser.port = portName
		print "portport"+portName
		try:
			ser.open()
		except serial.serialutil.SerialException:
			print "port openeddd"
		self.val = 0
		
	def takeValue(self):
		# print("trying")
		ser.write("1")
		self.val = ser.readline()
		return self.val

	# def print1(self):
	# 	while 1:
	# 		print("1")
	# 		time.sleep(0.2)
		# return 1

	def takeUltrasonicValue2(self):
		ser.write("2")
		self.val = ser.readline()
		return self.val

	def takeUltrasonicValue3(self):
		ser.write("3")
		self.val = ser.readline()
		return self.val

	def takeUltrasonicValue4(self):
		ser.write("4")
		self.val = ser.readline()
		return self.val

	def sendMotor(self, v):
		ser.write(v)
		# self.val = ser.readline()
		# print(self.val)

	def gpsvaluesLat(self, result):
		while 1==1:
			# print("rrr")
			try:
				ser1.open()
				#ser1.flush()
				i = ser1.readline()
				# result[0] = 1.4
				# print("next line "+str(i.split(',')[0]))
				if i.split(',')[0]=="$GPGGA":
					# result[0] = 1.45
					lat = float(i.split(',')[2])
					lon = float(i.split(',')[4])
					result[0] = float(i.split(',')[2])
					result[1] = float(i.split(',')[4])
					# print("got the latitude")
					# print("a")
					# print(i.split(',')[2])
					# global qq
					# qq.clear()
					# qq.put(i.split(',')[2])
					# global ll
					# ll.append(i.split(',')[2])
					# send_end.send(123)
					# global lat
					# lat=i.split(','[2])
					# return 1
					# return i.split(','[2])
					# break

					# global lat
					# lat=i.split(',')[2]

					# print i.split(',')[2], i.split(',')[4]
					# return i.split(',')[2]
					
			except KeyboardInterrupt as e:
				print("kkkk")
				print("error"+str(e))
				ser1.close()
				# p.stop()
				exit(0)
				# break
			except Exception as e:
				# return 1
				# print("Error.... wait")
				# print(e)
				# ser1.close()
				continue
			ser1.close()
	def printgpsvaluesLat(self):
		# global ll
		# return 1
		global lat
		return lat

	def getGPS():
		return lat
		return lon

		# if (qq.empty()==0):
		# 	global lat
			# lat = qq.get()
		# 	# global lat
			# return lat
		# if qq.empty():
		# 	# global lat
		# 	# time.sleep(5)
		# 	return lat

# a = sensor("/dev/ttyACM1")

# print(a.gpsvaluesLat([1]))
# # # bb = a.print1()
# # # print(bb)
# # # Process(target=a.print1).start()
# # try:
# # 	print("asass")
# # recv_end, send_end = multiprocessing.Pipe(False)
# p = multiprocessing.Process(target=a.gpsvaluesLat)

# p.start()
# time.sleep(9)
# print("geeee")
# print("hehe"+str(a.printgpsvaluesLat()))
# p.start()
# 	print("qqqq")
# 	# time.sleep(3)
# 	print("hehe"+str(a.printgpsvaluesLat()))
# except KeyboardInterrupt as e:
# 	print("kkkk")
# 	print("error"+str(e))
# 	# ser1.close()
# 	# p.stop()
# 	exit(0)

# thread.start_new_thread( a.print1,() )
# thread.start_new_thread( a.gpsvaluesLat,() )
# t1 = threading.Thread(target=a.print1()) 
# t2 = threading.Thread(target=a.gpsvaluesLat()) 
# t1.start()
# t2.start()
# t1.join() 
#     # wait until thread 2 is completely executed 
# t2.join() 
# print(a.gpsvaluesLat())
# while 1:
# 	print str(a.takeValue())+" "+str(a.takeIrValue())
