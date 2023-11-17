import time
import os
import tello
import cv2
import threading
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

def tello_data():
    height=Tello.get_height()
    Track.tracking(data.move(yolo.get_result()),height)
    #Tello.send_data(msg)
    
tello_thread=threading.Thread(target=tello_data)
tello_thread.daemon=True
tello_thread.start()

while 1:
    yolo.predict()
    
        



