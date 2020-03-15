import collections

class graph():
    def __init__(self):
        self.graph = collections.defaultdict(list)
    
    def addEdge(self, u, v): #creating adj list only 
        self.graph[u].append(v)
    

    def _DFSUtil(self, n, visited):

        visited[n] = True
        print(n)

        for nei in self.graph[n]:
            if visited[nei] == False:
                self._DFSUtil(nei, visited)

    def DFS(self,  u):

        visited = [False]*(len(self.graph) + 1) 
        print(u)

        for v in self.graph[u]:
            if visited[v] == False:
                self._DFSUtil(v,  visited)
    
    def BFS(self, u):
        q = []
        
        visited = [False]*(len(self.graph) + 1)
        
        q.append(u)
        visited[u] = True

        while q: 
            s = q.pop(0)
            print(s)
            for v in self.graph[s]:
                if visited[v] == False:
                    q.append(v)
                    visited[v] = True
    





# Another way to implementt he  grapg first

class Node():
    def __init__(self,  data):
        self.visited  = False
        self.data = data
        self.adj =  []

class traverseTrees():
    def DFS(self, startNode):
        
        print(startNode.data)
        startNode.visited = True

        for v in startNode.adj:
            if not v.visited:
                self.DFS(v)
    
    def  BFS(self,  startNode):
        queue = []
        queue.append(startNode)

        while queue:
            s = queue.pop(0)
            print(s.data)
            for v in s.adj:
                if  v.visited  == False:
                    v.visited = True
                    queue.append(v)



if __name__=="__main__":
    # g = graph()
    # g.addEdge(0,1)
    # g.addEdge(0,2)
    # g.addEdge(0,3)
    # g.addEdge(1,3)
    # g.addEdge(2,4)
    # g.addEdge(3,1)

    # g.DFS(0)
    # g.BFS(0)

    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')

    n1.adj.append(n2)
    n1.adj.append(n3)
    n1.adj.append(n4)
    n2.adj.append(n3)
    n3.adj.append(n4)
    n5.adj.append(n3)
    n5.adj.append(n1)
    n4.adj.append(n5)

    graph = traverseTrees()
    graph.BFS(n1)
    print("ho")
    graph.DFS(n1)









