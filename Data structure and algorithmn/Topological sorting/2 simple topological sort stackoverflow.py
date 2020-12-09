
'''
CHoose vertex 0
Source: 0 Neighbor : 1
Stack :  deque([])
Visited:  {0}


Source: 1 Neighbor : 2
Stack :  deque([])
Visited:  {0, 1}


Source: 2 Neighbor : 3
Stack :  deque([])
Visited:  {0, 1, 2}


Source: 1 Neighbor : 5
Stack :  deque([2, 3])
Visited:  {0, 1, 2, 3}


Source: 5 Neighbor : 3
Stack :  deque([2, 3])
Visited:  {0, 1, 2, 3, 5}


Source: 5 Neighbor : 4
Stack :  deque([2, 3])
Visited:  {0, 1, 2, 3, 5}


Source: 0 Neighbor : 2
Stack :  deque([1, 5, 4, 2, 3])
Visited:  {0, 1, 2, 3, 4, 5}


CHoose vertex 6
Source: 6 Neighbor : 1
Stack :  deque([0, 1, 5, 4, 2, 3])
Visited:  {0, 1, 2, 3, 4, 5, 6}


Source: 6 Neighbor : 5
Stack :  deque([0, 1, 5, 4, 2, 3])
Visited:  {0, 1, 2, 3, 4, 5, 6}


deque([6, 0, 1, 5, 4, 2, 3])
'''
from collections import deque

def dfs(graph,source,stack,visited):
    visited.add(source)
    #print(source)
    for neighbor in graph[source]:
        print("Source: %d Neighbor : %d"%(source,neighbor))
        print("Stack : ",stack)
        print("Visited: ",visited)
        print("\n")
        if neighbor not in visited:
            dfs(graph,neighbor,stack,visited)
    stack.appendleft(source)
    
def topological_sort(graph):
    #print(graph)
    stack=deque()
    visited=set()
    for vertex in graph.keys():
        if vertex not in visited:
            print("Choose vertex :",vertex)
            dfs(graph,vertex,stack,visited)
    return stack
    
graph={
       0:[1,2],
       1:[2,5],
       2:[3],
       3:[],
       4:[],
       5:[3,4],
       6:[1,5]
       }
topological=topological_sort(graph)
print(topological)