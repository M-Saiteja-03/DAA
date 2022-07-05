class Graph:
	def __init__(self, vertices,graph):
		# No. of vertices
		self.V = vertices
		self.Time = 0
		self.count = 0
		self.time_ap = 0
		self.graph = graph

	def biconnected_visit(self, u, parent, low, disc, st):
		children = 0
		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1
		for v in self.graph[u]:
			if disc[v] == -1 :
				parent[v] = u
				children += 1
				st.append((u, v)) 
				self.biconnected_visit(v, parent, low, disc, st)
				low[u] = min(low[u], low[v])
				if parent[u] == -1 and children > 1 or parent[u] != -1 and low[v] >= disc[u]:
					self.count += 1 
					w = -1
					while w != (u, v):
						w = st.pop()
						print(w,end=" ")
					print()
			elif v != parent[u] and low[u] > disc[v]:#condition for backedge
				low[u] = min(low [u], disc[v])	
				st.append((u, v))
	
	def AP_Visit(self,u,visited,ap,parent,low,disc):
		children=0
		visited[u]=True
		disc[u]=self.time_ap
		low[u]=self.time_ap
		self.time_ap+=1
		for v in self.graph[u]:
			if visited[v]==False:
				parent[v]=u
				children+=1
				self.AP_Visit(v,visited,ap,parent,low,disc)
				low[u]=min(low[u],low[v])

				if parent[u]==-1 and children>1:
					ap[u]=True
				if parent[u]!=-1 and low[v]>=disc[u]:
					ap[u]=True
			elif v!=parent[u]:
				low[u]=min(low[u],disc[v])

	def Articulation_Point(self):
		visited=[False]*(self.V)
		d_ap=[-1]*(self.V)
		low_ap=[-1]*(self.V)
		parent_ap=[-1]*(self.V)
		ap=[False]*(self.V)

		for i in range(self.V):
			if visited[i]==False:
				self.AP_Visit(i,visited,ap,parent_ap,low_ap,d_ap)
		a=""
		for i in range(self.V):
			if ap[i]==True:
				a+=str(i)+" "
		print("The articulation points are: "+a)

	def BCC(self):
		disc = [-1] * (self.V)
		low = [-1] * (self.V)
		parent = [-1] * (self.V)
		st = []
		for i in range(self.V):
			if disc[i] == -1:
				self.biconnected_visit(i, parent, low, disc, st)
			if st:
				self.count = self.count + 1
				while st:
					w = st.pop()
					print(w,end=" ")
				print ()

n=int(input("Enter the number of cities: "))
graph={0:[1,2],1:[0,3],2:[0,3],3:[1,2,4,5],4:[3,6],5:[3,6],6:[4,5]}
# for i in range(n):
# 	print("Enter the connections of each node with other nodes")
# 	graph[i]=[int(x) for x in input().split()]
g = Graph(n,graph)

g.BCC();
print ("Above are % d biconnected components in graph" %(g.count));
g.Articulation_Point();
