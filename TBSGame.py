# coding: utf-8

import os
import sys
from IPython import embed

def func(HP,AP,HM,AM,B,D):
	hp = HP
	n = 0
	if HP <= AM:
		return "IMPOSSIBLE"
	while HM > 0:
		if hp < AM:
			hp = HP
		elif hp <= AM and AP >= HM:
			return n+1
		else:
			HM -= AP
			hp -= AM
		n += 1
	return n

while True:
	lst = input('input HP,AP,HM,AM,B,D:').split()
	#embed()
	HP,AP,HM,AM,B,D = [int(i) for i in lst]
	n = func(HP,AP,HM,AM,B,D)
	if n==0:
		print("IMPOSSIBLE")
	else:
		print("You need %d times to defeat the monster!" % n)
