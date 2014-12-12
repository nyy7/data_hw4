import math
arr = [[2,4],[3,3],[3,4],[5,4],[5,6],[5,8],[6,4],[6,5],[6,7],[7,3],[7,4],[8,2],[9,4],[10,6],[10,7],[10,8],[11,5],[11,8],[12,7],[13,6],[13,7],[14,6],[15,4],[15,5]]
label = ['p','v','q','r','h','a','s','k','d','w','t','x','l','i','e','b','m','c','f','j','g','n','u','o']
index = 0
core_list = []
for ele in arr:
	nei_count = 0
	nei_arr = []
	nei_index = 0
	for nei in arr:
		dist = math.sqrt((nei[0] - ele[0])**2 + (nei[1] - ele[1])**2)
		if ele != nei and dist <= 2:
			nei_count += 1
			nei_arr.append(label[nei_index])
		nei_index += 1
	if nei_count >= 3:
		core_list.append(label[index])
		print label[index],': ',nei_arr
	index += 1
print sorted(core_list)

def ind_label(p1):
	ind = 0
	for i in label:
		if i == p1:
			return ind
		ind += 1
def ind_arr(p1):
	ind = 0
	for i in arr:
		if i == p1:
			return ind
def dir_reach(p1,p2):
	dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
	if dist <= 2:
		return 'true'
print dir_reach(arr[ind_label('a')],arr[ind_label('d')])

