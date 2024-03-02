# // linked list -> [] -> [] -> []
#// data structure.

class LinkedList_Node:
    def __init__(self,data) -> int:
        self.nodes = data
        self.next = None

def coundNodes(headOfLink):
    
    count = 1
    currentNode = headOfLink
    while currentNode.next is not None: # // if next.node is Null stop counting and return Node Value
        currentNode = currentNode.next
        count += 1
    return count

nodeA = LinkedList_Node(1)
nodeB = LinkedList_Node(2)
nodeC = LinkedList_Node(7)
nodeD = LinkedList_Node(9)


nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD

print(f"Nodes Of linked list:{coundNodes(nodeA)} ")