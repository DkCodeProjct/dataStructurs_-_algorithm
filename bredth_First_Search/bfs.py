tree = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8', '9'],
  '2' : [],
  '4' : ['8'],
  '8' : [],
  '9':[]
}

visited = []
qeue = []

def bfs(visited,tree,node):
    visited.append(node)
    qeue.append(node)

    while qeue:
        elemnt = qeue.pop(0)
        print(elemnt, end=" ")

        for child in tree[elemnt]:
            if child not in visited:
                visited.append(child)
                qeue.append(child)


print("bfs traversal ----> ")
res = bfs(visited,tree,'5')

print(res)