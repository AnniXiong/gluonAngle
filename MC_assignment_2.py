# Author : Anni Xiong
#
# Description :Put a descriptions here
#

import numpy as np
import matplotlib.pyplot as plt
import math

# comment to describe these observables so that people can read the code more easily
# "a" and "s" mean nothing to me
a = 0.785
s = 0.2
L = []
i = 0
NOfEvent = 20000

# comment to describe what you are doing with this loop
while i < NOfEvent:
    ns = np.random.uniform(0,10)

    x = np.random.uniform(0, (math.pi)/2)
    f_g = (1/(0.399*s))*(math.exp( (-(x-a)**2)/(2*(s**2)) ))

    if ns < f_g:
        L.append (x)
    i = i+1


# again, a small comment here to say that you are done with the important stuff and you
# are now just plotting would be very helpful
num_bins = 50
n, bins, patches = plt.hist(L, num_bins, normed = 1, facecolor='blue', alpha=0.5)

plt.xlabel('gluon emission angle')
plt.ylabel('Probability')
plt.title('Histogram of gluon energy emission angle')

plt.subplots_adjust(left=0.15)
plt.show()