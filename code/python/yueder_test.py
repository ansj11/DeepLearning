#/usr/bin/python
#-*- coding: utf-8 -*-

while 1:
    s = raw_input()
    if s !='':
        his_str = list(s)
        bin_str = []
        for char in his_str:
            if char.isalnum():
                bin_str.append('1')
            else:
                bin_str.append('0')
        raw_bin = list(raw_input())
        cnt = 0
        for x,y in zip(bin_str, raw_bin):
            if x == y:
                cnt += 1
            else:
                continue
        rat = float(cnt) / len(raw_bin)
        percent = rat * 100
        print("%.2f%%" % percent)
    else:
        continue
