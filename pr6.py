import random
import math
import matplotlib.pyplot as plot

outer = []
for i in range(0,10000):
	outer.append(-math.log(random.uniform(0,1)))
plot.hist(outer, bins=20)
plot.show()

