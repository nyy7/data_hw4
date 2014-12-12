import numpy
from scipy import cluster
from scipy import spatial
import matplotlib.pylab as plt
n00 = 0.0
n01 = 0.0
n10 = 0.0
n11 = 0.0
mx = [[1,0,1,1,0],[1,1,0,1,0],[0,0,1,1,0],[0,1,0,1,0],[1,0,1,0,1],[0,1,1,0,0]]
mx2 = numpy.zeros((6,6))
for t in range(0,5):
	for i in range(t+1,6):
		for j in range(5):
			if mx[t][j] == 1 and mx[i][j] == 1:
				n11 += 1
			elif mx[t][j] == 0 and mx[i][j] == 0:
				n00 += 1
			elif mx[t][j] == 1 and mx[i][j] == 0:
				n10 += 1
			elif mx[t][j] == 0 and mx[i][j] == 1:
				n01 += 1
		mx2[t][i] = 1 - (n11)/(n11 + n10 + n01)
		mx2[i][t] = mx2[t][i]
		n00 = 0.0
		n01 = 0.0
		n10 = 0.0
		n11 = 0.0
print mx2
mx_condense = spatial.distance.squareform(mx2)
print mx_condense
mx3 = cluster.hierarchy.linkage(mx_condense,method='average')
mx4 = cluster.hierarchy.dendrogram(mx3,labels=['x1','x2','x3','x4','x5','x6'],leaf_font_size=30)
plt.show()


