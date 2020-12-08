# -*- coding: utf-8 -*-
"""
An Adjacency matrix is a way of representing a graph G={V,E}
the size of the matrix is VXV where V is the number of vertices 
and the value of an entry Aij is either 1 or 0 depending on vertex i to j
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]

5

0 1 1 1 0 

1 0 1 0 0 

1 1 0 0 0 

1 0 0 0 0
"""

class Graph:
    def __init__(self,size):
        self.AdjMatrix=[]
        for i in range(size):
            self.AdjMatrix.append([0 for i in range(size)])
        self.size=size
    def add_edge(self,v1,v2):
        if v1==v2:
            print("Same node")
        self.AdjMatrix[v1][v2]=1
        self.AdjMatrix[v2][v1]=1
    def delete_edge(self,v1,v2):
        if v1==v2:
            print("Same node")
        self.AdjMatrix[v1][v2]=0
        self.AdjMatrix[v2][v1]=0
    def print_graph(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.AdjMatrix[i][j],end=" ")
            print("\n")
            
    def graph_show(self):
        for row in self.AdjMatrix:
            for val in row:
                print("{:4}".format(val))
            print()
            
        

g=Graph(5)
print(g.AdjMatrix)
print(g.size)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,2)
g.print_graph()
#g.graph_show()