"""
simple DFS implementation

Queue:  ['a']
u : a
Queue:  ['b', 'c']
u : b
Queue:  ['d', 'c']
u : d
Queue:  ['e', 'c']
u : e
Queue:  ['c']
u : c
Queue:  ['d']
['a', 'b', 'd', 'e', 'c']
"""
def iterative_dfs(graph,start):
    visited=[]
    q=[start]
    
    while q:
        print('Queue: ',q)
        u= q.pop(0)
        
        if u  not in visited:
            print("u :",u)
            visited.append(u)
            q=graph[u]+q
    return visited


graph={
       'a':['b','c'],
       'b':['d'],
       'c':['d'],
       'd':['e'],
       'e':[]
       }
start='a'
print(iterative_dfs(graph,start))