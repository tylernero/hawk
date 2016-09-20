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
	vals=[]
	for i in range(0,5):
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
ex_year = years[0]
var_year
for i in range(1,len(years)):
	for k, j in enumerate(ex_year):
		ex_year[k] = j+years[i][k]
for i,j in enumerate(ex_year):
	print(1+i,j/len(years))
plt.hist(port, bins=20)
plt.show()

