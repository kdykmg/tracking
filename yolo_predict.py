from ultralytics import YOLO
import os
import cv2

class Predict:
    def __init__(self,Tello):
        self.model = YOLO("train10.onnx",task='detect')
        self.vid=Tello.video
        self.arr=[[],[],[],[]]
    def predict(self):
        
        total_frame=int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, total_frame-1)
        sucess,frame=self.vid.read()
        if sucess:
            result_arr=[[],[],[],[]]
            result=self.model.track(frame,persist=True,imgsz=640,agnostic_nms=True,verbose=False)
            plot=result[0].plot()
            for box in result[0].boxes:
                if result[0].boxes.id!=None:
                    ids=box.id.int().cpu().tolist()
                    num=box.cls[0].cpu().detach().numpy().tolist()
                    box=box.xywh
                    x=box[0][0].cpu().detach().numpy().tolist()
                    y=box[0][1].cpu().detach().numpy().tolist()
                    h=box[0][3].cpu().detach().numpy().tolist()
                    line = [x,y,h,ids]
                    if num==0:
                        result_arr[0].append(line)
                    elif num==1:
                        result_arr[1].append(line)
                    elif num==2:
                        result_arr[2].append(line)
                    elif num==3:
                        result_arr[3].append(line)
            self.arr=result_arr
            cv2.imshow("Video", plot) 
            if cv2.waitKey(1) & 0xFF == ord("q"):
                return
    def get_result(self):
        return self.arr
    