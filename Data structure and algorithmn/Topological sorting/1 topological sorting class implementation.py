# -*- coding: utf-8 -*-
"""
Topological sorting for DAG is a linear ordering of vertices
such that for every directed edge uv, vertex u comes before v in the ordering.
Sorting is not possible if the graph is not a DAG

defaultdict(<class 'list'>, 
{5: [2, 0],
 4: [0, 1],
 2: [3],
 3: [1]})
[5, 4, 2, 3, 1, 0]

vertex :  0
Stack :  [0]
vertex :  1
Stack :  [1, 0]
vertex :  2
graph :u->v : 3
vertex :  3
graph :u->v : 1
Stack :  [3, 1, 0]
Stack :  [2, 3, 1, 0]
vertex :  4
graph :u->v : 0
graph :u->v : 1
Stack :  [4, 2, 3, 1, 0]
vertex :  5
graph :u->v : 2
graph :u->v : 0
Stack :  [5, 4, 2, 3, 1, 0]
[5, 4, 2, 3, 1, 0]
"""
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def topologicalSortUtil(self,v,visited,stack):
        visited[v]=True
        print('vertex : ',v)
        #print("visited : ",visited)
        for i in self.graph[v]:
            print("graph :u->v :",i)
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        stack.insert(0,v)
        print("Stack : ",stack)
                
    def topologicalSort(self):
        visited=[False]*self.V
        stack=[]
        for i in range(self.V):
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        print(stack)
        
        


g=Graph(6)
g.addEdge(5, 2) 
g.addEdge(5, 0) 
g.addEdge(4, 0) 
g.addEdge(4, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1)
print(g.graph)
g.topologicalSort()

