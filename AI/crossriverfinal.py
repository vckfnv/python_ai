class Problem:
    def __init__(self, init, goal):
        self.initState = init
        self.goalState = goal

    def isGoal(self, s):
        if self.goalState == s:
            return True
        else:
            return False

    def sucFN(self, state):
        sucli = []
        #state[0]가 False일때 나머지가 True -> False 안된다
        #state[0]가 True일 때 나머지가 False -> True 안된다
        
        sucli.append([not state[0],state[1],state[2],state[3]])
        sucli.append([not state[0],not state[1],state[2],state[3]])
        sucli.append([not state[0],state[1],not state[2],state[3]])
        sucli.append([not state[0],state[1],state[2],not state[3]])        

        for i in sucli:
            if i[0] == True:
                for j in range(1,4):
                    if state[j] == True:
                        if not i[j]:
                            sucli.remove(i)
            else:
                for k in range(1,4):
                    if state[k] == False:
                        if i[k]:
                            sucli.remove(i)
        return sucli
    
class Node:
    def __init__(self,s, p, c, d):
        self.state = s
        self.parent = p
        self.cost = c
        self.depth = d

    def solutionPath(self):
        path = self.state
        if self.depth == 0: 
            print(path)
        else:
            print(path)
            self.parent.solutionPath()

    #def __str__(self):
    #    return 'S: ' + self.state + ', depth = ' + str(self.depth) + ', cost = ' + str(self.cost)

class DFS:
    def __init__(self, p):
        self.numberGeneratedNodes = 0
        self.prob = p
        self.frontier = Stack()      
        self.visited = []
        self.eaten = [[False, False, True, True],
                      [False, True, True, False],
                      [True, False, False, True],
                      [True, True, False, False],
                      [True,False,False,False],
                      [False,True,True,True]]
    def expand(self, parent):
        children = []
        for i in self.prob.sucFN(parent.state):
            s = Node(i, parent, parent.cost + 1, parent.depth + 1 )
            children.append(s)
        
        self.numberGeneratedNodes += len(children)
        return children

    def solution(self):
        root = Node(self.prob.initState, None , 0, 0)
        self.frontier.pushh(root)
        while not self.frontier.isEmpty():
            parent = self.frontier.popp()
            #print('DEBUG: PARENT - ', parent.state)
            self.visited.append(parent.state)
            if self.prob.isGoal(parent.state):
                return parent
            expandedNodes = self.expand(parent)
            for i in expandedNodes:
                if i.state not in self.visited and i.state not in self.eaten:
                    self.frontier.pushh(i)
        return False
    
class Stack:
    def __init__(self):
        self.items = []
    def pushh(self, node):
        self.items.append(node)
    def popp(self):
        return self.items.pop()   
    def isEmpty(self):
        if len(self.items) == 0 : return True
        else: return False

prob = Problem([False,False,False,False],[True,True,True,True])
print(prob.sucFN([True,True,False,True]))
dfs = DFS(prob)
goalNode = dfs.solution()
print(goalNode)
print('Nodes Generated',dfs.numberGeneratedNodes)
print(goalNode.solutionPath())
