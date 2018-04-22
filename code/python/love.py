# -*- coding: utf-8 -*-

print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else ' ') for x in range(-30,30)]) for y in range(30,-30,-1)]))

import time
words = input('please enter the word you want to say:')
for item in words.split():
    print('\n'.join([''.join([(item[(x-y) % len(item)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else ' ') for x in range(-30,30)]) for y in range(30,-30,-1)]))
    time.sleep(1.5)

