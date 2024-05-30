graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set()
def dfs(visited,tree,node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for child in tree[node]:
            dfs(visited,tree,child)
                    

print("Following is the Depth-First Search")
j = dfs(visited, graph, '5')
print(j)