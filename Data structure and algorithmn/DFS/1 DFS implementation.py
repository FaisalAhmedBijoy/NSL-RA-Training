# -*- coding: utf-8 -*-
"""
DFS(G, u)
    u.visited = true
    for each v ∈ G.Adj[u]
        if v.visited == false
            DFS(G,v)
     
init() {
    For each u ∈ G
        u.visited = false
     For each u ∈ G
       DFS(G, u)
}

0
2
1
3
4
{'0', '2', '1', '4', '3'}
"""
def DFS(graph,start,visited=None):
    #print(graph)
    if visited is None:
        visited= set()
    visited.add(start)
    print(start)
    
    for next in graph[start]-visited:
        DFS(graph,next,visited)
    return visited
    
graph={'0': set(['1','2']),
       '1': set(['0','3','4']),
       '2': set(['0']),
       '3': set(['1']),
       '4': set(['2','3'])
       }
start_node='0'
print(DFS(graph,start_node))
 