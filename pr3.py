import random
import math
import matplotlib.pyplot as plot

outer = []
outerA = []
outerC = []
for i in range(0,1000):
	I100 = []
	I100a = []
	I100c = []
	for j in range(0,100):
		a = random.uniform(0,1)
		I100.append(math.log(a))
		I100a.append(math.log(1-a))
		I100c.append(math.log(a))
		I100c.append(math.log(1-a))
	outer.append( reduce(lambda x,y: x+y,I100)/len(I100))
	outerA.append(reduce(lambda x,y: x+y,I100a)/len(I100))
	outerC.append(reduce(lambda x,y: x+y,I100c)/len(I100c))

avg = reduce(lambda x,y:x+y,outer)/len(outer)
avgA = reduce(lambda x,y:x+y,outerA)/len(outerA)
avgC = reduce(lambda x,y:x+y,outerC)/len(outerC)
print("mean = ", avg)
print("mean a = ", avgA)
print("mean comb = ", avgC)
print("var = ", reduce(lambda x,y:x+abs(avg-y),outer)/len(outer))
print("var a = ", reduce(lambda x,y:x+abs(avgA-y),outerA)/len(outerA)) 
print("var comb = ", reduce(lambda x,y:x+abs(avgC-y),(outerC))/len(outerC))	
