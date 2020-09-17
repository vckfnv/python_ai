map = {
    'A':[('Z',75), ('T', 118), ('S', 140) ],
    'O': [('Z', 171), ('S', 151)],
    'S': [('F', 99), ('R', 80), ('O',151), ('A', 140)],
    'R':[('S',80), ('P',97), ('C', 146)],
    'T':[('A', 118), ('L', 111)],
    'L':[('M',75), ('T',111)],
    'C': [('D',120), ('R', 146), ('P', 138)],
    'Z': [('A',75), ('O', 71)],
    'F': [('S', 99), ('B', 211)],
    'P': [('R', 97), ('B', 101)]  
}
#print(map.get('Ara', 'no key'))

hmap = {
    'A':366,
    'F': 178,
    'C':178,
    'D': 242,
    'E': 161,
    'B':0,
    'G':77,
    'H':151,
    'I':226,
    'L':244,
    'M':241,
    'N':234,
    'O':380,
    'P': 98,
    'R':193,
    'S':253,
    'T':329,
    'U': 80,
    'V':199,
    'Z':374
}

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

class Node:
    def __init__(self,s, p, c, d, h):
        self.state = s
        self.parent = p
        self.cost = c
        self.depth = d
        self.h = h
        self.f = self.cost + self.h

        
    def solutionPath(self):
        path = self.state
        if self.depth == 0: 
            return path
        else:
            return path + ' <-- ' + self.parent.solutionPath()

    def __str__(self):
        return 'S: ' + self.state + ', depth = ' + str(self.depth) + ', cost = ' + str(self.cost)

class AStar:
    def __init__(self, p, h):
        self.numberGeneratedNodes = 0
        self.prob = p
        self.hm = h
        self.frontier = Queue()      
        self.visited = set()  #visited.add()
    def expand(self, parent):
        children = []
        for i in self.prob.sucFN(parent.state):
            s = Node(i[0], parent, i[1] + parent.cost, parent.depth + 1,
                     self.hm[i[0]])
            children.append(s)
        self.numberGeneratedNodes += len(children)
        return children
    def solution(self):
        root = Node(self.prob.initState, None, 0, 0, self.hm[self.prob.initState])
        self.frontier.enqueue(root)
       
        while not self.frontier.isEmpty():
            parent = self.frontier.dequeue()
            print('DEBUG: PARENT - ', parent.state, parent.f)
            self.visited.add(parent.state)
            if self.prob.isGoal(parent.state):
                return parent
            expandedNodes = self.expand(parent)
            for i in expandedNodes:
                if i not in self.visited:
                    self.frontier.enqueue(i)
        return False

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, node):
        if len(self.items) == 0:
            self.items.append(node)
        else:
            
            for i in range(len(self.items)):
                if node.f < self.items[i].f:
                    self.items.insert(i, node)
                    break
        
    def dequeue(self):
        return self.items.pop(0)  # updated 
    def isEmpty(self):
        if len(self.items) == 0 : return True
        else: return False
            
prob = Problem('A', 'B', map)
astar = AStar(prob, hmap)
goalNode = astar.solution()
print(astar.numberGeneratedNodes)
print(goalNode.solutionPath())
