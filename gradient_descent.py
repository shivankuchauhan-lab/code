# -*- coding: utf-8 -*-
"""Gradient Descent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16gTQApwr6DDrPL4sQvRncDvdbmdZ_z-p
"""

import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x,y):
  m_curr = b_curr = 0
  iterations = 10
  n = len(x)
  learning_rate = 0.08
  for i in range(iterations):
    y_predicted = m_curr * x + b_curr
    cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
    md = -(2/n)*sum(x*(y-y_predicted))
    bd = -(2/n)*sum(y-y_predicted)
    m_curr = m_curr - learning_rate * md
    b_curr = b_curr - learning_rate * bd
    print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))



x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)