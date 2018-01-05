#!/usr/bin/env python 2.7
# waloo le encoding: utf-8 de malade

import numpy as np 
import matplotlib.pyplot as plt 

def graph(formula, x1, x2):
	plt.plot([x1, x2],[0, 0])
	x = np.array(range(x1, x2))  
	y = eval(formula)
	plt.plot(x, y)
	plt.title(formula)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()