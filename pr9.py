import random
import math

randomVars = []
for i in range(0,100):
	randomVars.append([math.ceil(random.uniform(0,6)),math.ceil(random.uniform(0,6))])
output = []
output.append([0,0,randomVars[0][0],randomVars[0][0],0,randomVars[0][1],randomVars[0][0]+randomVars[0][1]])
i = 1
while i < len(randomVars):
	interArrival = randomVars[i][0]
	arrival = interArrival + output[i-1][2]
	start = max(output[i-1][6],arrival)
	wait = max(0,start-arrival)
	service = randomVars[i][1]
	depart = start + service
	if i > 4:
		if 
	output.append([i,interArrival,arrival,start,wait,service,depart])
	i+=1
combWait = 0
agents = 0
for i in output:
	combWait += i[4]
	agents += 1

print( combWait/agents)
