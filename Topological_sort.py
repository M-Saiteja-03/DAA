
class Graph:
    def __init__(self,V,adj):
        self.V=V
        self.Matrix=adj
    # def addedge(self,i,j):
    #     self.Matrix[i][j]=1
def Topological_sort(G):
    indegree=[0]*n
    for x in range(n):
        for y in range(n):
            indegree[y]+=G.Matrix[x][y]
    queue=[];order=[];visited=[]
    for x in range(n):
        if indegree[x]==0:
            queue.append(x)
            visited.append(x)
    while(queue):
        u=queue.pop(0)
        order.append(u)
        for x in range(n):
            indegree[x]-=G.Matrix[u][x]
            G.Matrix[u][x]=0
        for x in range(n):
            if indegree[x]==0 and x not in visited:
                queue.append(x)
                visited.append(x)
    print("Topological order is:" ,order)
    
n=int(input("Enter no of vertices: "))

adj=[[0]*(n) for _ in range(n)]
for i in range(n):
    print("Enter the dependencies of %d DLL with other DLLs (if no dependency(no indegree), click enter)"%(i))
    l=[int(x) for x in input().split()]
    for j in l:
        adj[j][i]=1
    
G=Graph(n,adj)
print(G.Matrix)
Topological_sort(G)