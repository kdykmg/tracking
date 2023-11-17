import time
import os
import tello
import cv2
import threading
import queue
import yolo_predict
import yolo_data
import track
import yolo_data_human

path=os.path.dirname(__file__)
path=path+''
os.chdir(path)
        
Tello=tello.Tello()
yolo=yolo_predict.Predict(Tello)
#data=yolo_data.Move()
data=yolo_data_human.Move()
Track=track.tracking()
vid=Tello.video
frame_que=queue.Queue(maxsize=1)

def Que():
    while 1:
        sucess,frame=vid.read()
        if sucess:
            frame_que.put(frame)
    
que_thread=threading.Thread(target=Que)
que_thread.daemon=True
que_thread.start()

while 1:
    height=Tello.get_height()
    Track.tracking(data.move(yolo.predict(frame_que.get())),height)
    #Tello.send_data(msg)
    yolo.predict()
    
        



