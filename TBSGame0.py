# coding: utf-8

import os
import sys
from IPython import embed

def func(HP,AP,HM,AM):
	hp = HP
	n = 0
	if AM >= HP and AP<HM:
		return 0
	while HM > 0:
		if AP >= HM:
			return n+1
		elif hp <= AM:
			hp = HP
			n += 1
		else:
			HM -= AP
			hp -= AM
		n += 1
	return n

while True:
	lst = input('input HP,AP,HM,AM:').split()
	#embed()
	HP,AP,HM,AM = [int(i) for i in lst]
	n = func(HP,AP,HM,AM)
	if n==0:
		print("IMPOSSIBLE")
	else:
		print("You need %d times to defeat the monster!" % n)
