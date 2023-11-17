import socket
import cv2

class Tello:
    def __init__(self):
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("0.0.0.0",8889))
        self.tello_address = ("192.168.10.1", 8889)
        self.local_video_port = 11111
        self.socket.sendto('command'.encode('utf-8'),self.tello_address)
        self.socket.sendto('streamon'.encode('utf-8'),self.tello_address)
        self.video=cv2.VideoCapture("udp://@0.0.0.0:11111")
        
        
    def send_data(self,msg):
        self.socket.sendto('msg'.encode('utf-8'),self.tello_address)
