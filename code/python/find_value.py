# -*- coding:utf-8 -*-
class Solution:
    
    def Find(self,target,array):
        if len(array)==1 and len(array[0])==0:
            return False
        
        has_value = 0
        for i in array:
            for j in i:
                if j==target:
                    has_value += 1
                else:
                    has_value +=0
        
        if has_value==0:
            return False
        else:
            return True
        
