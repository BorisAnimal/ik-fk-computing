from fk import fk
from ik import ik
from math import pi


class KukaKR10:
    def __init__(self):
        """
        Sizes taken from:
            https://www.kuka.com/-/media/kuka-downloads/imported/6b77eecacfe542d3b736af377562ecaa/0000290003_en.pdf
        
        """
        self.l0 = 400 
        self.l1 = 25
        self.l2 = 560
        self.l3 = 25
        self.l4 = 515
        self.l5 = 90 # End effector
        
        # Or in DH notation
        self.theta = [0,-pi/2,0,0,0,0]
        self.d = [400,0,0,515,0,90]
        self.a = [25,560,25,0,0,0]
        self.alpha = [-pi/2,0,-pi/2,pi/2,-pi/2,0]
    
    def fk(self, q, vis=True):
        return fk(self,q,vis)
    
    def ik(self, xyz, rpy):
        return ik(self,xyz,rpy)