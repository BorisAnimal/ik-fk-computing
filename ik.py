import numpy as np
from numpy import sin as S
from numpy import cos as C
from math import atan2, sqrt
from math import pi
from matrices import *

def ik(self, xyz, rpy):
    R = Rx(rpy[0]) @ Ry(rpy[1]) @ Rz(rpy[2])
    # Coord of wrist center
    Oc = np.array(xyz) - np.array([[0,0,self.l5]]) @ R[:3,:3] 
    [xc,yc,zc] = Oc.flatten()
    if xc == yc == 0:
        print("Singularity")
        return
    q0 = atan2(yc,xc)
#     q0 = [q0, q0+pi] # 2 cases

    # Front case
    r = sqrt(xc**2 + yc**2) - self.a[0]
    s = zc - self.d[0]
    gamma = atan2(self.l4, self.l3)
    h2 = sqrt(self.l4**2+self.l3**2)
    h1 = sqrt(r**2 + s**2)

    C_psi = (h2**2 + self.a[1]**2 - h1**2) / (2 * h2* self.a[1])
    S_psi = sqrt(1 - C_psi**2)
    psi1 = atan2(S_psi, C_psi) # 2 cases generally
    psi2 = atan2(-S_psi, C_psi)
    psi = psi1
    q2 = pi - psi - gamma


    beta = atan2(s,r)
    S_alpha = S_psi *h2/h1
    C_alpha = sqrt(1-S_alpha**2)

    alpha1 = atan2(S_alpha, C_alpha) # still 2 cases
    alpha2 = atan2(S_alpha, -C_alpha) # still 2 cases
    alpha = alpha1

    q1 = alpha + beta

    # EE
    # Just general case
    q3 = atan2(R[1,2], R[0,2])
    q4 = atan2(R[1,2], -R[2,2] * S(q3))
    q5 = atan2(-R[2,1], R[2,0])

    return np.array([q0,q1,q2]).reshape(-1,1), [q3,q4,q5]