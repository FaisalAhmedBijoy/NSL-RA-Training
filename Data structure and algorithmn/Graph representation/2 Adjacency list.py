# -*- coding: utf-8 -*-
"""
An adjacency list represents a graph as an array of linked list
the index of the array represents a vertex and each element in its 
linked list represents the other vertices that
form an edges with the vertex
5
[None, None, None, None, None]
Vertex 0:-> 3-> 2-> 1

Vertex 1:-> 2-> 0

Vertex 2:-> 1-> 0

Vertex 3:-> 0

Vertex 4:

None
"""

class AdjNode:
    def __init__(self,value):
        self.vertex=value
        self.next=None
class Graph:
    def __init__(self,num):
        self.V=num
        self.graph=[None]* self.V
    def add_edge(self,source,dist):
        node=AdjNode(dist)
        node.next=self.graph[source]
        self.graph[source]=node
        
        node=AdjNode(source)
        node.next=self.graph[dist]
        self.graph[dist]=node
    def print_graph(self):
        for i in range(self.V):
            print("Vertex "+str(i)+":",end="")
            temp=self.graph[i]
            while temp:
                print("-> {}".format(temp.vertex),end="")
                temp=temp.next
            print("\n")
g=Graph(5)
print(g.V)
print(g.graph)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,2)
print(g.print_graph())



        
