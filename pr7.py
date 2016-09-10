import random
import math
import matplotlib.pyplot as plot

outer = []
for i in range(0,10000):
	x = random.uniform(0,1)
	y = random.uniform(0,1)
	outer.append(x/(x-y))
plot.hist(outer, bins=20)
plot.show()

