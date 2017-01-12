#          A  B  C  D  E  F
import random
import sys
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
direction = sys.argv[1]   # 0-》 up to down, 1-》 down to up
n1_state = sys.argv[2]

n1 = Node(16, 4)
CPT_temp = [[0.0878,0.0782,0.4412,0.3928],[0.0480,0.1180,0.2410,0.5930],[0.0398,0.1262,0.2002,0.6338],[0.0166,0.1494,0.0834,0.7506],[0.0074,0.0066,0.5216,0.4644],[0.0040,0.0100,0.2850,0.7010],[0.0034,0.0106,0.2366,0.7494],[0.0014,0.0126,0.0986,0.8874],[0.0503,0.0447,0.4787,0.4263],[0.0275,0.0675,0.2615,0.6435],[0.0228,0.0722,0.2172,0.6878],[0.0095,0.0855,0.0905,0.8145],[0.0033,0.0030,0.5257,0.4680],[0.0018,0.0045,0.2872,0.7065],[0.0015,0.0048,0.2385,0.7552],[0.0006,0.0057,0.0994,0.8943]]
n1.updateCPT(CPT_temp)
n1.printCPT()

n2 = Node(4, 4)
CPT_temp = [[0.0184,0.3266,0.0349,0.6201],[0.0010,0.2990,0.0023,0.6977],[0.0024,0.0426,0.0509,0.9041],[0.0003,0.0053,0.05300,9414]]
n2.updateCPT(CPT_temp)
n2.printCPT()
if direction == 0:
	nodes.append(n1)
	nodes.append(n2)
elif direction == 1:
	nodes.append(n2)
	nodes.append(n1)


def probability(p): # p is a list
	p2 = 0.0
	for i in range(len(p)):
		p2 += p[i]
		if random.randint(0, 99) < p2 * 100:
			return i # can be changed
score = [0]*num_of_targets  # Need to be adjustable!


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
