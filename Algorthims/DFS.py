# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visit = set() # Set to keep track of visited nodes of graph.

def dfs(visit, graph, node):  #function for dfs 
    if node not in visit:
        print (node)
        visit.add(node)
        for neighbour in graph[node]:
            dfs(visit, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visit, graph, '5')
