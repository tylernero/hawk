import random
import math
import matplotlib.pyplot as plot

outer = []
for i in range(0,1000):
	I100 = []
	for j in range(0,100):
		I100.append(math.exp(-(random.uniform(0,1)**2)/2))
	outer.append( reduce(lambda x,y: x+y,I100)/len(I100))
#plot.hist(outer, bins=20)
#plot.show()

avg = reduce(lambda x,y:x+y,outer)/len(outer)
#print( max(float(v) for v in outer ))
print("mean = ", avg)
print("var = ", reduce(lambda x,y:x+abs(avg-y),outer)/len(outer))	
