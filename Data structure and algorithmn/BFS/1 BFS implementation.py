# -*- coding: utf-8 -*-
"""
create a queue Q 
mark v as visited and put v into Q 
while Q is non-empty 
    remove the head u of Q 
    mark and enqueue all (unvisited) neighbours of u
{0: [1, 2],
 1: [2],
 2: [3],
 3: [1, 2]}

{0, 1, 2, 3}

Complexities : V+E
"""
from collections import deque
def BFS(graph,start):
    print(graph)
    q=deque()
    q.append(start)
    visited=set()
    visited.add(start)
    while q:
        vertex=q.pop()
        for u in graph[vertex]:
            if u not in visited:
                visited.add(u)
                q.append(u)
    return visited
                
graph={0:[1,2],
       1:[2],
       2:[3],
       3:[1,2]
       }
start_node=0
print(BFS(graph,start_node))
