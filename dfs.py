
def dfs(vertices, edges, g, start, visited):
    visited[start]=1
    print(start,end='') # end =' ' is used to print in the same line
    for x in g[start]: 
        if visited[x]!=1:
            print("->",end='')
            dfs(vertices,edges,g,x,visited)
            
vertices=int(input("Enter the number of vertices: "))
edges=int(input("Enter the number of edges: "))
visited = [0]*vertices # visited list which has all the vertices and value -> 0
g = [[] for _ in range(vertices)] # nested list -> 

for i in range (0,edges,1): 
    print("Enter the source and the destination: ")
    u, v = map(int, input().split())
    # u->source, v->destination using map function common value is taken using split value is seperated
    g[u].append(v) # vertex no 1 is connected to vertex no 2
    g[v].append(u)
    print(g)
start=int(input("Enter the starting vertex: "))
dfs(vertices,edges,g,start,visited)


#                                              EXPLANATION

#...........................................................................................................................

# -> vertices of the graph      0          1       2         3         4     (0,1,2,3,4 are the vertices of the graph)

# -> g[[]] values-> u=0 v=1     1          0       _         _         _     (0->1) and (1->0) are connected
# -> g[[]] values-> u=0 v=2     1,2        0       0         _         _     (0->2) and (2->0) are connected
# -> g[[]] values-> u=0 v=3     1,2,3      0       0         0         _     (0->3) and (3->0) are connected
# -> g[[]] values-> u=2 v=3     1,2,3      0       0,3       0,2       _     (2->3) and (3->2) are connected
# -> g[[]] values-> u=2 v=4     1,2,3      0       0,3,4     0,2       2     (2->4) and (4->2) are connected
# -> g[[]] values-> u=3 v=4     1,2,3      0       0,3,4     0,2,4     2,3   (3->4) and (4->3) are connected

#...........................................................................................................................