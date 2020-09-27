from functools import reduce
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from numpy import sin as S
from numpy import cos as C
from math import atan2, sqrt
from math import pi
from matrices import *

def fk(self, q, vis=True):
    """
    Returns transformation matrix
    """
    trans = [Rz(q[0]),Tz(self.l0), Tx(self.l1) ,Ry(q[1]),Tz(self.l2),
             Ry(q[2]+pi/2), Tx(-self.l3), # This two tricks could be fixed with DH
             Tz(self.l4),Rx(q[3]),Tz(self.l5),Ry(q[4]),Rx(q[5])]
    points = []
    res = trans[0]
    for t in trans[1:]:
        points.append(res[0:3, 3].flatten())
        res = res @ t
    # Just one of general cases
    if abs(res[0,2]) != 1:
        r = atan2(res[2,1], res[2,2])
        p = atan2(-res[2,1], sqrt(res[0,0]**2 + res[1,0]**2))
        y = atan2(res[1,0], res[0,0])
    else:
        print("Singular case")
        return

    points = np.array(points)

    if vis:
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(points[:,0],points[:,1],points[:,2],s=30)
        ax.plot(points[:,0],points[:,1],points[:,2])
        plt.show()
#         res = reduce(lambda a,b: a@b, trans)

    return res[:3,3].flatten(), [r,p,y]