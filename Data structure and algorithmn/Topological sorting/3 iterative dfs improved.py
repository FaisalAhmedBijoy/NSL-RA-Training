def iterative_dfs_improved(graph,start):
    visited=set()
    path=[]
    q=[start]
    while q:
        v=q.pop()
        if v not in graph[v]:
            visited.add(v)
            path.append(v)
            q.extend(graph[v])
    return path

graph={
       'a':['b','c'],
       'b':['d'],
       'c':['d'],
       'd':['e'],
       'e':[]
       }
start='a'
print(iterative_dfs_improved(graph,start))