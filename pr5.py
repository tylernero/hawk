import matplotlib.pyplot as plt
from random import uniform as U
import math
results = []
for i in range(1,15):
	results.append([i,0])
	for j in range(1,2**i):
		if((U(0,1)-1.0/2.0)**2 +(U(0,1)-1.0/2.0)**2+(U(0,1)-1.0/2.0)**2 <=1.0/4.0):
			results[i-1][1]+=1
print( results)
print(float(results[-1][1])/float((2**results[-1][0])))
plt.plot( [x[0] for x in results],[float(y[1])/float(2**y[0]) for y in results])
#plt.plot( [x[0] for x in results],[math.sqrt(1.0*y[1]/(2**y[0])-(1-y[1]/(2**y[0]))/2**y[0]) for y in results])
#print( [math.sqrt(y[1]/(2**y[0])-(1-y[1]/(2**y[0]))/2**y[0]) for y in results])
#plt.legend(["pie est.","conf. inv."], loc='upper left')
plt.show()
