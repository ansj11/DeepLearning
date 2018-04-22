from PIL import Image
from pylab import *

im = array(Image.open('test.jpg'))
imshow(im)
print 'click 3 points'
x = ginput(3)

print 'you click:',x
show()
