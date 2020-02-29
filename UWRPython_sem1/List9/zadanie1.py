import numpy as np
import sys

A = np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
B = np.array([6,2,-5,17,12]).T

S =  np.linalg.solve(A,B)

print("x = {} \ny = {} \nz = {} \nt = {} \nu = {}\n".format(S[0],S[1],S[2],S[3],S[4]))