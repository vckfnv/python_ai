graph = {
    'A':('B', 'C', 'D'), 
    'B':('E', 'F'),
    'C':('G', 'H', 'I'),
    'D':('J','K'),
    'E':('L', 'M'),
    'F':('N','O'),
    'G':('P','Q'),
    'H':('R', 'S'),
    'I':('T','U'),
    'J':('V', 'W'),
    'K':('X', 'Y')
}

utility = {
    'L':4,
    'M':3,
    'N':6,
    'O':2,
    'P':2,
    'Q':1,
    'R':9,
    'S':5,
    'T':3,
    'U':1,
    'V':5,
    'W':4,
    'X':7,
    'Y':5
}
def max_value(state, a, b, graph,u):
    
    if state in u:
        v= u.get(state,None)
        #print('   leaf node',state, 'returning', v)
        return u.get(state, None)
    v = -1000
    print('max_value',state,',a =',a,',b=',b)
    for s in graph.get(state,None):
        v = max(v,min_value(s, a,b,graph,u))
        if v >= b:
            return v
        a = max(a,v)
    return v

def min_value(state, a, b, graph,u):
    if state in u:
        v= u.get(state,None)
        #print('   leaf node',state, 'returning', v)
        return u.get(state, None)
    v = 1000
    print('min_value',state,',a =',a,',b=',b)
    
    for s in graph.get(state,None):
        v = min(v,max_value(s,a,b,graph,u))
        if v <=a:
            return v
        a = min(b,v)
    return v

print(max_value('A',-1000,1000,graph,utility))
