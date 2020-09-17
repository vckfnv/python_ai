# -*- coding: utf-8 -*-
"""BSF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_92rYUv_HGSlFsV9MRNXDvdc0b-pGojm
"""

map = {
'Arad': [('Zerind',75), ('Timisoara', 118), ('Sibiu', 140) ],
'Sibiu': [('Fagaras', 99), ('RV', 80), ('Oradea',151), ('Arad', 140)],
'RV':[('Sibiu',80), ('Pitesti',97), ('Craiova', 146)]
}
#print(map.get('Ara', 'no key'))

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, node):
        self.items.append(node)
    def dequeue(self):
        return self.items.pop(0)  # updated 
    def isEmpty(self):
        if len(self.items) == 0 : return True
        else: return False

class Problem:
    def __init__(self, i, g, m):
        self.initState = i
        self.goalState = g
        self.model = m

    def isGoal(self, s):
        if self.goalState == s:
            return True
        else:
            return False

    def sucFN(self, city):
        return self.model.get(city, [])

#prob = Problem('Arad', 'Sibiu', map)
#print(prob.sucFN('Arad'))

class Node:
    def __init__(self,s, p, c, d):
        self.state = s
        self.parent = p
        self.cost = c
        self.depth = d

    def solutionPath(self):
        path = self.state
        if self.depth == 0: 
            return path
        else:
            return path + ' <-- ' + self.parent.solutionPath()

    def __str__(self):
        return 'S: ' + self.state + ', depth = ' + str(self.depth) + ', cost = ' + str(self.cost)

node1 = Node('Arad', None, 0, 0)
node2 = Node('Sibiu', node1, 77, 1)
node3 = Node('Fagaras', node2, 717, 2)
print(node3.solutionPath())

class BFS:
    def __init__(self, p):
        self.numberGeneratedNodes = 0
        self.prob = p
        self.frontier = Queue()      
        self.visited = set()  #visited.add()
    def expand(self, parent):
        children = []
        for i in self.prob.sucFN(parent.state):
            s = Node(i[0], parent, i[1] + parent.cost, parent.depth + 1 )
            children.append(s)
        self.numberGeneratedNodes += len(children)
        return children
    def solution(self):
        #1. root node with initial state
        root = Node(self.prob.initState, None, 0, 0)
        #2. add the root node to frontier Queue
        self.frontier.enqueue(root)
        # while queue is not empty
        while not self.frontier.isEmpty():
            # pop a node
            parent = self.frontier.dequeue()
            print('DEBUG: PARENT - ', parent.state)
            # if the node is goal, return the node
            if self.prob.isGoal(parent.state):
                return parent
            # expand and add them to the queue
            expandedNodes = self.expand(parent)
            for i in expandedNodes:
                self.frontier.enqueue(i)
        return False
map = { 'Arad': [('Zerind',75), ('Timisoara', 118), ('Sibiu', 140) ],
        'Sibiu': [('Fagaras', 99), ('RV', 80), ('Oradea',151), ('Arad', 140)],
        'RV':[('Sibiu',80), ('Pitesti',97), ('Craiova', 146)]}
prob = Problem('Arad', 'Craiova', map)
bfs = BFS(prob)
goalNode = bfs.solution()
print(goalNode)
print(Node('arad',None,0,0))
print(bfs.numberGeneratedNodes)
print(goalNode.solutionPath())
