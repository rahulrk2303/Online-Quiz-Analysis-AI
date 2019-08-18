from flask import url_for, jsonify, Flask, render_template, request, jsonify
import numpy as np
import cv2
import time
from threading import Thread, Lock
import blinkrate_new
from Test.face_classification.src.face_expr_test import expr
from Test.quantify import quant
import time

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

    while(True and ques<5):
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
	
	while (timer_run and ques<5):
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
	
	if ques == 5:
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

@app.route('/foo', methods=['POST'])
def foo():
    # grab reddit data and write to csv
    timer_run = False
    global i
    t = i
    i = 0
    global sum
    sum = sum + t
    global ques
    ques = ques + 1
    timer_run = True
    return jsonify({'time taken for previous question' : str(t), 'total time' : str(sum)})
	

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

