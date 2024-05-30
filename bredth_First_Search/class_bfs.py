class BredthFirstSearch:
    def __init__(self,node):
        self.node = node
        self.qeue = []
        self.visited = []
        self.traversal = []


    def bfs(self,tree):
        self.visited.append(self.node)
        self.qeue.append(self.node)

        while self.qeue:
            element = self.qeue.pop(0)
            self.traversal.append(element)

            for child in tree[element]:
                if child not in self.visited:
                    self.visited.append(child)
                    self.qeue.append(child)

                    
    def __str__(self):
        return " --> ".join(self.traversal)
        

graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

bfsSearch = BredthFirstSearch('5')
bfsSearch.bfs(graph)
print(bfsSearch)