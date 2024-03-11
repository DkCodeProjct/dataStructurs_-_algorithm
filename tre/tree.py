class NodeTree:
    def __init__(self,data) -> int:
        self.data = data
        self.rightRoot = None
        self.leftRoot = None

def sumValueTree(root):
    if root == None:
        return 0
    return root.data + sumValueTree(root.rightRoot) + sumValueTree(root.leftRoot)
    
#   example tree:
#         2
#       /   \
#      3     4
#     / \
#    5   6

node2 = NodeTree(2)
node3 = NodeTree(3)
node4 = NodeTree(4)
node5 = NodeTree(5)
node6 = NodeTree(6)

node2.rightRoot = node3
node2.leftRoot = node4
node3.leftRoot = node5
node3.rightRoot = node6

print('sum of tree')
print(sumValueTree(node2))