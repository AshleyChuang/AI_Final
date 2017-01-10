#          A  B  C  D  E  F
import random
num_of_nodes = 2
num_of_targets = 4
num_of_loop = 1000

class Node:
	def __init__(self, num_row, num_col):
		self.CPT = [[0 for x in range(num_row)] for y in range(num_col)] 
	def getCPT(self, row, col):
		return self.CPT[row][col]
	def updateCPT(self, list):
		self.CPT = list;
	def printCPT(self):
		print self.CPT
	def getNumOfNextStates(self):
		return len(self.CPT[0])
	def getNumOfCurrentStates(self):
		return len(self.CPT)
nodes = []

n1 = Node(2, 3)
CPT_temp = [ [0.2, 0.4, 0.4], [0.1, 0.2, 0.7]]
n1.updateCPT(CPT_temp)
n1.printCPT()
nodes.append(n1)

n2 = Node(3, 4)
CPT_temp = [ [0.1, 0.5, 0.2, 0.2], [0.45, 0.2, 0.1, 0.25], [0.1, 0.2, 0.4, 0.3]]
n2.updateCPT(CPT_temp)
n2.printCPT()
nodes.append(n2)

def probability(p): # p is a list
	p2 = 0.0
	for i in range(len(p)):
		p2 += p[i]
		if random.randint(0, 99) < p2 * 100:
			return i # can be changed
score = [0]*num_of_targets  # Need to be adjustable!


n1_state = 0
for i in range(0, num_of_loop, 1):
	print str(i) + " times:"
	current_state = n1_state
	for n in range(0, len(nodes), 1):
		p = []
		for k in range(0, nodes[n].getNumOfNextStates(), 1):
			p.append(nodes[n].getCPT(current_state, k))
		next_state = probability(p)
		print str(current_state) + "-> " + str(next_state)
		current_state = next_state
	score[next_state] += 1
	print score
for i in range(len(score)):
	score[i] = float(score[i])/float(num_of_loop);
print score
