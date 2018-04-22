#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
import theano.tensor as T
import theano

# activate function
x = T.dmatrix('x')
s = 1/(1+T.exp(-x))
logistic = theano.function([x],s)
print(logistic([[0,1],[2,3]]))

# multi output for a function
a,b = T.dmatrices('a','b')
diff = a - b
abs_diff = abs(diff)
diff_square = diff**2
f = theano.function([a,b],[diff,abs_diff,diff_square])
print(f(
    np.ones((2,2)),
    np.arange(4).reshape((2,2))
))

# name for a function
x,y,w = T.scalars('x','y','w')
z = (x + y)*w
f = theano.function([x,theano.In(y,value=1),
                     theano.In(w,value=2,name='weights')],z)

print(f(23,))


########################
# theano 先定义操作或运算，然后调用theano.function(inputs,outputs)
# 启动图运算
# 若inputs包含多个，用[x,y,w],inputs 包括参数

# 包含中文注释一定要加开头的声明 #-*- coding: utf-8 -*-s