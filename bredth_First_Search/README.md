#Breadth-First Search aka BFS

    -  is a fundamental algorithm in computer science used to traverse or search through the nodes of a graph or tree. It explores all nodes at the present depth level before moving on to nodes at the next depth level. 

    + ###Initialization:

    -Start with a queue and a list (or another data structure) to keep track of visited nodes.
    Enqueue the starting node and mark it as visited.

    + ###Traversal:

    - While the queue is not empty:
        Dequeue a node from the front of the queue.
        Process the dequeued node (e.g., print it or check if it's the target node).
        Enqueue all adjacent nodes that have not been visited yet and mark them as visited.

    
    ---------------------------------------------

        * bfs Graph
        //
               A
              / \
             B   C
            / \   \
           D   E   F
                      //
        ####Order;

            - A -> B -> C -> D -> E -> F

    -----------------------------------------------

   

    #Breadth-First Search (BFS) is used in artificial intelligence (AI) 
    
        - primarily related to its properties of completeness and optimality in certain contexts. Here are the main applications of BFS in AI:
        
        ####1. Pathfinding Algorithms
        - BFS is frequently used in pathfinding and graph traversal algorithms, which are common in AI applications such as:

            * Game AI: Finding the shortest path for a character to move from one point to another on a grid.
            Robotics: Navigating a robot through a grid-like environment, ensuring it reaches its destination efficiently.

        ####2. Solving Puzzles

        - BFS can be employed to solve puzzles where the goal is to find the shortest sequence of moves to reach a desired configuration, such as:

            * Maze Solving: Finding the shortest path from the entrance to the exit.
            Sliding Puzzles: Finding the minimum number of moves to arrange tiles in a particular order