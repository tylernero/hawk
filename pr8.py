import random
import math

outer = []
for q in range(0,10000):
	randomVars = []
	randomVars.append([math.ceil(random.uniform(0,6)),math.ceil(random.uniform(0,6))])
	output = []
	output.append([0,0,randomVars[0][0],randomVars[0][0],0,randomVars[0][1],randomVars[0][0]+randomVars[0][1]])
	x = 1
	i = 1
	while x == 1 :
		randomVars.append([math.ceil(random.uniform(0,6)),math.ceil(random.uniform(0,6))])
		interArrival = randomVars[i][0]
		arrival = interArrival + output[i-1][2]
		start = max(output[i-1][6],arrival)
		wait = max(0,start-arrival)
		service = randomVars[i][1]
		depart = start + service
		output.append([i,interArrival,arrival,start,wait,service,depart])
		if i > 4:
			if arrival < output[i-4][3]:
				x = 0
				outer.append(i) 
		i+=1
print(float(sum(outer))/float(len(outer)))
