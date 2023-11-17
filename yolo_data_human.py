import math
from numba import jit

class Move:
    def __init__(self):
        self.before_arr=[[],[],[],[]]
        self.tracking=None
        self.tracking_scooter=[]                    
                
    @jit    
    def move(self,af_arr):
        if self.tracking!=None:
            for pe_ax,pe_ay,pe_ah,pe_aids in af_arr[3]:
                if self.tracking==pe_aids:
                    self.tracking_scooter=[pe_ax,pe_ay,pe_aids,pe_ah]
                    continue
                self.tracking_scooter=[]
        be_arr=self.before_arr              
        
        for pe_ax,pe_ay,pe_ah,pe_aids in af_arr[3]:
            for pe_bx,pe_by,pe_bh,pe_bids in be_arr[3]:
                if pe_aids==pe_bids:
                    dis_kb=math.sqrt((pe_ax-pe_bx)**2+(pe_ay-pe_by)**2) 
                    if dis_kb>pe_ah/100:
                        for he_ax,he_ay,he_ah,he_aids in af_arr[2]:
                            for he_bx,he_by,he_bh,he_bids in be_arr[2]:
                                if he_aids==he_bids:
                                    dis_he=math.sqrt((he_ax-he_bx)**2+(he_ay-he_by)**2)
                                    if dis_kb*0.7<dis_he and dis_he<dis_kb*1.3:
                                        self.tracking=pe_aids
                                        self.tracking_scooter=[pe_ax,pe_ay,pe_aids,pe_ah]                      
        self.before_arr=af_arr     
        return self.tracking_scooter           
        
        
