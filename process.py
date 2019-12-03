from flask import url_for, jsonify, Flask, render_template, request, jsonify
import numpy as np
# from flask_socketio import SocketID,send
import cv2
import time
from threading import Thread, Lock
import blinkrate_new
from Test.face_classification.src.face_expr_test import expr,ret_exp
from quantify import quant, ret_quant
import time
import xlwt 
from xlwt import Workbook 


app = Flask(__name__)

ques = 0

class WebcamVideoStream :
	def __init__(self, src = 0, width = 640, height = 480) :
		self.stream = cv2.VideoCapture(src)
		self.stream.set( cv2.CAP_PROP_FRAME_WIDTH, width)
		self.stream.set( cv2.CAP_PROP_FRAME_HEIGHT, height)
		(self.grabbed, self.frame) = self.stream.read()
		self.started = False
		self.read_lock = Lock()

	def start(self) :
		if self.started :
			# print ("already started!!")
			return None
		self.started = True
		self.thread = Thread(target=self.update, args=())
		self.thread.start()
		return self

	def update(self) :
		while self.started :
			(grabbed, frame) = self.stream.read()
			self.read_lock.acquire()
			self.grabbed, self.frame = grabbed, frame
			self.read_lock.release()

	def read(self) :
		self.read_lock.acquire()
		frame = self.frame.copy()
		self.read_lock.release()
		return frame

	def stop(self) :
		self.started = False
		self.thread.join()

	def __exit__(self, exc_type, exc_value, traceback) :
		self.stream.release()


def capture(cap=None):
	# cap = cv2.VideoCapture(0)
	cap = cap.start()
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('capture.avi',fourcc, 20.0, (640,480))
	x = 0

	while(True and ques<10000):
		frame = cap.read()
		out.write(frame)
		# cv2.imshow('capture', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		# while True:
		   #  frame1 = frame.copy()
		   #  print(frame1)
		   #  time.sleep(5)
		# 	frame2 = frame.copy()
		# 	print(frame2)
		# 	quant(frame1, frame2)
		# 	break
		
		if x%(5*10*2) == 0:
			frame2 = frame
		if (x-50)%(5*10*2) == 0:
			frame1 = frame
			# quant(frame1, frame2)
			if x%2==0:
				quant(frame1, frame2)
			else:
				quant(frame2, frame1)
		x+=1

		# a = 0
		# b = 30*5
		# c = a+b
		# if x%
		# c = a+b
		# a = b
		# b = c
		# c = a+b

	cap.stop()
	out.release()
	cv2.destroyAllWindows()

timer_run = True
i = 0

def timer ():
	
	while (timer_run and ques<10000):
		time.sleep(1)
		global i
		i = i+1
		# print (i)
		# if i > 20:
		# 	break

		
# t1 = Thread(target = capture)
# t2 = Thread(target = timer)
# t3 = Thread(target = blinkrate_new.func)

@app.route('/')
def index():
	wvs = WebcamVideoStream()
	t1 = Thread(target = capture, kwargs={'cap': wvs})
	t2 = Thread(target = timer)
	t3 = Thread(target = blinkrate_new.func, kwargs={'vs': wvs})
	t4 = Thread(target = expr, kwargs={'video_capture': wvs})
	
	if ques == 10000:
		wvs.stop()
		wvs.stream.release()
		cv2.destroyAllWindows()
		t1.stop()
		t2.stop()
		t3.stop()
		t4.stop()

	t1.start()
	t2.start()
	t3.start()
	t4.start()

	# while True :
	#     frame1 = vs.read()
	#     frame2 = vs.read()
	#    	cv2.imshow('webcam1', frame1)
	#    	cv2.imshow('webcam2', frame2)
	#     if cv2.waitKey(1) == 27 :
	#         break
	return render_template('quiz.html')

sum = 0
a = 0
b = 0
c = 0
click_c = 0
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
sheet1.write(0, 1, 'Q#') 
sheet1.write(0, 2, 'Time taken') 
sheet1.write(0, 3, 'Blink count') 
sheet1.write(0, 4, 'Manhattan Norm') 
sheet1.write(0, 5, 'Manhattan Zero') 
sheet1.write(0,6,'Max of Norm')
sheet1.write(0,7,'Max of Zero')
sheet1.write(0, 8,'Click#')
sheet1.write(0,9,'Confidence')
sheet1.write(0,10,'Face Expr')
sheet1.write(0,11,'Answer')

option_clicks =[0,0,0,0]
opt = 0

@app.route('/click_count', methods=['POST'])
def click_count():
	global click_c
	global opt
	click_c = click_c + 1
	print("CLICK COUNT : " + format(click_c))
	opt = int(request.form.get('option'))
	option_clicks[opt]+=1
	print(option_clicks)
	return ''
# def getGopoints(request):
#     lat = str(request.GET['lat'])
#     print('jsvalue',lat)


@app.route('/foo', methods=['POST'])
def foo():
	# if request.method == 'POST':
	#     ans = request.form['canvas_data']
	# print(ans)
	# grab reddit data and write to csv

	ans = int(request.form.get('answer'))
	cans = int(request.form.get('canswer'))
	print(ans)
	global click_c
	# if click_c==1:
	# 	avg=100
	# elif click_c == 2:
	# 	avg=50
	# elif click_c ==3:
	# 	avg = 25
	# else:
	# 	avg = 0

	global option_clicks
	# global opt
	# print("Option" + format(opt))
	conf = option_clicks[cans]/click_c*100
	# conf = conf*ans
	print("Confidence = " + format(conf))

	timer_run = False
	global i
	time = i
	i = 0
	global sum
	sum = sum + time
	global ques
	ques = ques + 1
	timer_run = True
	global a
	global b
	global c
	# global click_c
	b = blinkrate_new.blink_count()
	c = b - a
	a = b
	b = c
	x, y, z, z1 = ret_quant()
	exp = ret_exp()
	exp_data=round(exp)
	if(exp_data==1):
		exp_send='happy'
	elif(exp_data==2):
		exp_send='angry'
	elif(exp_data==3):
		exp_send='sad'
	elif(exp_data==4):
		exp_send='surprise'
	else:
		exp_send='neutral'

	option_clicks = [0,0,0,0]
	
   # doc_ref = db.collection('quiz').document('mam' + format(ques))
	#doc_ref.set({
	#Question no'+ format(ques): ques,
	#'Time taken' + format(ques) : time,
	#'Total Time taken': sum,
	#'Blink Count' + format(ques): c,
	#'Zero norm per pixel' + format(ques) :y
	#},merge=True)

	# text_file = open('output' + format(ques) + '.txt', 'w')
	# text_file.write('\nQuestion no. : ' + format(ques))
	# text_file.write('\nTime taken : ' + format(time))
	# text_file.write('\nTotal Time taken : ' + format(sum))
	# text_file.write('\nBlink Count : ' + format(c))
	# text_file.write('\nManhattan norm per pixel : ' + format(x))
	# text_file.write('\nZero norm per pixel : ' + format(y))
	
  
	

	sheet1.write(ques,1,ques)
	sheet1.write(ques,2,time)
	sheet1.write(ques,3,c)
	sheet1.write(ques,4,x)
	sheet1.write(ques,5,y) 
	sheet1.write(ques,6,z)
	sheet1.write(ques,7,z1)
	sheet1.write(ques,8,click_c)
	sheet1.write(ques,9,conf)
	sheet1.write(ques,10,exp_send)
	sheet1.write(ques,11,ans)
	wb.save('xlwt example.xls')
	click_c=0

	return ''

	# text_file.write('\nOption Changes : ' + format(click_c) + '\n')
	# click_c = 0
	# text_file.write('[')
	# text_file.write(format( TOTAL ) )
	# text_file.write(',\t' )
   # text_file.close()
	# return jsonify({'time taken for previous question' : str(time), 'total time' : str(sum), 'Blink count for previous question' : str(blink)})
	

# @app.route('/process', methods=['POST'])
# def process():
	# return jsonify({'name': Next})
	# email = request.form['email']
	# name = request.form['name']

	# if name and email:
	# 	newName = name[::-1]

	# 	return jsonify({'name' : newName})

	# return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':

	app.run(port=8080, debug=True)

