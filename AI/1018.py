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

﻿
#터미널이냐? 이면 유틸리티를 불러서 씀.
#그래프를 가져왔는데 값이 있다면 자식이 있는거고 없는애는 터미널이다
#graph.get(state, None)
#값이 없다면 유틸리티에서 


def max_value(state, a, b, graph):

    ifter = graph.get(state, None)
    if ifter == None:
        v = utility.get(state,None)
    v = -1000
    for i in ifter:
        v = max(v,min_value(i, a,b,graph))
        if v >= b:
            return v
        a = max(a,v)
    return v

﻿

﻿

def min_value(state, a, b, graph):
    ifter = graph.get(state, None)
    if ifter == None:
        v= utility.get(state,None)
    v = 1000
    for i in ifter:
        v = min(v,max_value(i, a,b,graph))
        if v <= a:
            return v
        a = min(b,v)
    return v

﻿

﻿print(max_value('A', -1000, 1000, graph))
