class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
        
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    
    def __str__(self):
        return str(self.id)+'connected To'+str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
    def addVertex(self,key):
        self.numVertices=self.numVertices+1
        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        return newVertex
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertList
    def addEdge(self,source,destination,weight=0):
        if source not in self.vertList:
            nv=self.addVertex(source)
        if destination not in self.vertList:
            nv=self.addVertex(destination)
        self.vertList[source].addNeighbor(self.vertList[destination],weight)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())
g=Graph()
print(g.vertList)
for i in range(5):
    g.addVertex(i)
print(g.vertList)   

     
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
print(g.vertList.__iter__())
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))