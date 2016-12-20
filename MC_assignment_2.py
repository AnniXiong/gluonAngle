import numpy as np
import matplotlib.pyplot as plt
import math


a = 0.785
s = 0.2
L = []
i = 0
NOfEvent = 20000


while i < NOfEvent:
	ns = np.random.uniform(0,10)
	
	x = np.random.uniform(0, (math.pi)/2)
	f_g = (1/(0.399*s))*(math.exp( (-(x-a)**2)/(2*(s**2)) ))
	
	if ns < f_g:
		L.append (x)
	i = i+1



num_bins = 50
n, bins, patches = plt.hist(L, num_bins,
	                         normed = 1, facecolor='blue', alpha=0.5)

plt.xlabel('gluon emission angle')
plt.ylabel('Probability')
plt.title('Histogram of gluon energy emission angle')

plt.subplots_adjust(left=0.15)
plt.show()