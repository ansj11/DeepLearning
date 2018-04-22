# -*- coding: utf-8 -*-

import numpy as np
from IPython import embed

m = 8
Q = np.zeros([8,8])

def settleQueen(nums,x):
    if x==m:
        return True
    for y in range(8):
        for j in range(8):
            nums[x,j]=0
        #embed()
        if check(nums,x,y):
            nums[x,y]=1;
            if settleQueen(nums,x+1):
                return True
    return False

def check(nums, x, y):
    for i in range(x):
        if nums[i,y]==1:
            return False
        if y-1-i>=0 and nums[x-1-i,y-1-i]==1:
            return False
        if y+1+i<m and nums[x-1-i,y+1+i]==1:
            return False
    return True

for i in range(8):
    flag = settleQueen(Q,0)
    print(Q,flag)
