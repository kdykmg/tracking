import time
import tello
import cv2
import yolo_predict
import yolo_data
import track
import yolo_data_human

Tello=tello.Tello()
yolo=yolo_predict.Predict()
#data=yolo_data.Move()
data=yolo_data_human.Move()
Track=track.tracking()
vid=Tello.video

while 1:
    height=Tello.get_height()
    total_frame=int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    vid.set(cv2.CAP_PROP_POS_FRAMES, total_frame-1)
    sucess,frame=vid.read()
    if sucess:
        Track.tracking(data.move(yolo.predict(frame)),height)
        #Tello.send_data(msg)
    
        



