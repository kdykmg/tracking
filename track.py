import math


class tracking:
    def __init__(self):
        self.land=True
        self.weight=960
        self.height=720
        self.middle=self.weight/2
        self.stand_tello_height=2
        """
        self.stand_scooter_height=1
        self.stand_scooter_weight=1
        self.stand_distance=1
        self.real_distance=0.879*self.stand_distance/self.middle
        self.cross_scooter=math.sqrt(self.stand_scooter_height**2+self.stand_scooter_weight**2)
        self.croos_distance=math.sqrt((self.stand_tello_height-self.stand_scooter_height)**2+self.stand_distance**2)
        self.distsnce=self.cross_scooter/(((self.stand_tello_height-self.stand_scooter_height)/self.croos_distance)*self.stand_scooter_height/self.cross_scooter+self.stand_distance/self.croos_distance*self.stand_scooter_weight/self.cross_scooter)/self.stand_distance
        """
        
        self.stand_heigh=1.7
        self.stand_distance=1
        self.stand_distance=1
        self.real_distance=0.879*self.stand_distance/self.middle
        
        
    def tracking(self,scooter,d_h):
        if scooter==[]:
            return "stop" 
       
        x=scooter[0]
        y=scooter[1]
        h=scooter[3]
        print(x,y,h)
        
        h=h*self.real_distance
        #distance=h*self.distsnce-self.stand_scooter_weight/2 
        distance=h*(d_h-self.stand_heigh)/(math.sqrt(self.stand_heigh**2-h**2))
        print(distance)
        
        if distance<self.stand_distance:
             #self.tello.send_data("stop")
             print("stop")
             return    
        set_speed=int(100-100*self.stand_distance/distance)
        print("speed:",set_speed)
        
        if self.land:
            #self.tello.send_data("takeoff")
            self.land=False
            print("takeoff")
        if x/self.middle>1.1:
            #self.tello.send_data("ccw 10")
            print("ccw10")
        elif x/self.middle<0.9:
            #self.tello.send_data("cw 10")
            print("cw10")
        self.tello.send_data("speed %d" %set_speed)            