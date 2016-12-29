
# Anni Xiong
# this script creates a histogram of angles between 0 and 90 degrees 
# following a Gaussian distribution.


import numpy as np
import matplotlib.pyplot as plt
import math

mean = 0.785  # defines the mean of Gaussian function
std = 0.2     # defines the standard deviation of Gaussian function
Angle = []    # the list of angles that will be appended with selected values later
NOfEvent = 20000 # number of events

# This loop selects out the angles that follow under the Gaussian distribution, from the uniform distribution
for i in range(NOfEvent):
	ns = np.random.uniform(0,10)
	
	x = np.random.uniform(0, (math.pi)/2)
	f_g = (1/(0.399*std))*(math.exp( (-(x-mean)**2)/(2*(std**2)) ))
	
	if ns < f_g:
		Angle.append (x)
	

# Now we have got a list of angles that follow Gaussian distribution and the following is
# plotting the list in a histogram with several optional arguments.
num_bins = 50
n, bins, patches = plt.hist(Angle, num_bins,
	                         normed = 1, facecolor='blue', alpha=0.5)

plt.xlabel('gluon emission angle')
plt.ylabel('Probability')
plt.title('Histogram of gluon energy emission angle')

plt.subplots_adjust(left=0.15)
plt.show()