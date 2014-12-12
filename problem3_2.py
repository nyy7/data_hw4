
from math import sqrt, pow  

class DBSCAN:  
	#Density-Based Spatial Clustering of Application with Noise -> http://en.wikipedia.org/wiki/DBSCAN  
	def __init__(self):  
		self.name = 'DBSCAN'
		self.DB = []
		self.esp = 2
		self.MinPts = 3 
		self.cluster_inx = -1
		self.cluster = []
		self.core = []
		self.neighbor = []

	def DBSCAN(self):  
	    for i in range(len(self.DB)):  
			p_tmp = self.DB[i]  
			if (not p_tmp.visited):  
			#for each unvisited point P in dataset  
				p_tmp.visited = True  
				NeighborPts = self.regionQuery(p_tmp) 
				if(len(NeighborPts) >= self.MinPts):  
					self.core.append(p_tmp)
					self.cluster.append([])  
					self.cluster_inx = self.cluster_inx + 1  
					self.expandCluster(p_tmp, NeighborPts)     

	def expandCluster(self, P, neighbor_points):  
		self.cluster[self.cluster_inx].append(P) 
		iterator = iter(neighbor_points)  
		while True:  
			try:   
				npoint_tmp = iterator.next()  
			except StopIteration:  
	    # StopIteration exception is raised after last element 
		 		break  
			if (not npoint_tmp.visited):  
		#for each point P' in NeighborPts   
				npoint_tmp.visited = True
				NeighborPts_ = self.regionQuery(npoint_tmp)  
				if (len(NeighborPts_) >= self.MinPts):  
			  		for j in range(len(NeighborPts_)):  
				   		neighbor_points.append(NeighborPts_[j])
			for n in neighbor_points:
				self.neighbor.append(n)
			if (not self.checkMembership(npoint_tmp)):  
		#if P' is not yet member of any cluster  
				self.cluster[self.cluster_inx].append(npoint_tmp)
			for i in range(len(self.cluster)):
				if self.cluster_inx != i:
					for j in self.cluster[i]:
						if npoint_tmp == j:
							print npoint_tmp, "is belong to some cluster"

	def checkMembership(self, P):  
	  #will return True if point is belonged to some cluster  
	  ismember = False  
	  for i in range(len(self.cluster)):  
		  for j in range(len(self.cluster[i])):  
			if (P.x == self.cluster[i][j].x and P.y == self.cluster[i][j].y):  
				ismember = True  
	  return ismember  

   	def regionQuery(self, P):  
   	#return all points within P's eps-neighborhood, except itself  
		pointInRegion = []  
		for i in range(len(self.DB)):  
			p_tmp = self.DB[i]  
			if self.dist(P, p_tmp) <= self.esp:  
				if not P.equal(p_tmp):
					pointInRegion.append(p_tmp)  
	  	return pointInRegion  

   	def dist(self, p1, p2):  
    	#return distance between two point  
		dx = (p1.x - p2.x)  
		dy = (p1.y - p2.y)  
		return sqrt(pow(dx,2) + pow(dy,2))  

	def check_noise(self,P):
		for i in self.core:
			if P.equal(i):
				return False
		for j in self.neighbor:
			if P.equal(j):
				return False
		return True
 
class Point:  
	def __init__(self, x = 0, y = 0, label = 'null',visited = False, isnoise = False):  
		self.x = x  
		self.y = y
		self.label = label  
		self.visited = False  
		self.isnoise = False  
   	def show(self):  
		return self.label  
	def equal(self,P):
		if self.x == P.x and self.y == P.y:
			return True

if __name__=='__main__':  
#this is a mocking data just for test  
	vecPoint = [Point(2,4,'p'), Point(3,3,'v'), Point(3,4,'q'), Point(5,4,'r'), Point(5,6,'h'), Point(5,8,'a'), Point(6,4,'s'), Point(6,5,'k'), Point(6,7,'d'), Point(7,3,'w'),Point(7,4,'t'),Point(8,2,'x'),Point(9,4,'l'),Point(10,6,'i'),Point(10,7,'e'),Point(10,8,'b'),Point(11,5,'m'),Point(11,8,'c'),Point(12,7,'f'),Point(13,6,'j'),Point(13,7,'g'),Point(14,6,'n'),Point(15,4,'u'),Point(15,5,'o')]  
#Create object  
dbScan = DBSCAN()  
#Load data into object  
dbScan.DB = vecPoint;  
#Do clustering  
dbScan.DBSCAN()  
#Show result cluster
print "result for DBSCAN:"
for i in range(len(dbScan.cluster)): 
	final_cluster = []
   	print 'Cluster: ', i  					
	for j in range(len(dbScan.cluster[i])): 
		final_cluster.append(dbScan.cluster[i][j].show())
	for k in sorted(final_cluster):
		print k,
	print '\n'
print "noise point: ",
for i in dbScan.DB:
	if dbScan.check_noise(i):
		print i.label
		
