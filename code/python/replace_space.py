# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        l = s.split(" ")
        str = l[0]
        for i in range(1,len(l)):
        	str = str+"%20"+l[i]
        
        return str
