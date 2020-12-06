'''
make set :
    disjoint set
[None, None, None, None, None, None]
Initial array parents: 
 [None, 1, 2, 3, 4, 5]
Graph parent: 
 [None, 2, 2, 2, 2, 4]
New Representives : 
 [None, 2, 2, 2, 2, 4]
3
Already friends
Representative of :  5 -> is :  2
    

'''
element=5
parent=[None] * (element+1) # create with 6 element
print(parent)
def makeset(n):
    parent[n]=n
for i in range(1,element+1):
    makeset(i)
print("Initial array parents: \n",parent)

# make a parent and representative
a=1
b=2
c=3
d=4
e=5
parent[a]=b
parent[c]=b
parent[e]=d
parent[d]=b

print("Graph parent: \n",parent)

#find the representative of a node
def find(r):
    if parent[r]==r:
        return r
    else:
        print(r)
        parent[r]=find(parent[r])
        return parent[r]
        #return find(parent[r])
# Make discount set : union
def union(a,b):
    u=find(a)
    v=find(b)
    if u==v:
        print("Already friends")
    else:
        parent[u]=v
print("New Representives : \n",parent)
union(b,c)

print("Representative of : ",e,end="" )
print(" -> is : ",b)
