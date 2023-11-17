from ultralytics import YOLO
import os
import cv2

class Predict:
    def __init__(self):
        self.model = YOLO("train10.onnx",task='detect')
        
    def predict(self,frame):
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
        cv2.imshow("Video", plot) 
        return result_arr
    