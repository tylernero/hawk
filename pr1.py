import matplotlib.pyplot as plt


def slope(x):
	return [x,(x+1)]


lst = []
k = 0.0
while k <= .20:
	lst.append(slope(k))
	k = k+.1

plt.plot( [x[0] for x in lst],[y[1] for y in lst])
plt.show()
