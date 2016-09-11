import random
import math
import matplotlib.pyplot as plt
port = []
years = []
for i in range(0,10000):
	ibm = 100000
	apple = 200000
	gp = 100000
	cash = 300000
	for i in range(0,5):
		vals = []
		ibm = ibm*(1+random.uniform(-.1,.15))
		apple = apple*(1+random.uniform(-.2,.4))
		if random.uniform(0,1) < .03:
			gp = 0
		else:
			gp = gp*1.05
		cash = cash*1.01
		vals.append(ibm+apple+gp+cash)
	port.append(ibm+apple+gp+cash)
	years.append(vals)

plt.hist(port, bins=20)
plt.show()

