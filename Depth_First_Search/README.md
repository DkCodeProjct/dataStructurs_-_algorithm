# Depth-First Search  aka DFS 

    - another fundamental algorithm in computer science used to traverse or search through the nodes of a graph or tree. Unlike BFS, which explores all nodes at the present depth level before moving to the next level, DFS explores as far as possible along each branch before backtracking.

+ ###  Initialization:

    * Start with a stack (can be implemented using recursion) and a list (or another data structure) to keep track of visited nodes.
    
    * Push the starting node onto the stack and mark it as visited.

+ ### Traversal:

    - While the stack is not empty:

    * Pop a node from the top of the stack.
    
    * Process the popped node (e.g., print it or check if it’s the target node).
    
    * Push all adjacent nodes that have not been visited yet onto the stack and mark them as visited.
    
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

            - A -> B -> D -> D -> E -> C -> F

    -----------------------------------------------

   

## Applications of DFS in AI

- Pathfinding and Navigation:
       * Solving Mazes: DFS can be used to find a path from the start to the end of a maze. Although it does not guarantee the shortest path, it is effective in exploring all possible paths.

        * Game Maps: In video game AI, DFS can help explore and navigate complex game maps.

    -  Puzzle Solving:
        * Sudoku Solver: DFS can be applied to solve puzzles like Sudoku by trying out possible solutions in a systematic manner.
        
        * N-Queens Problem: DFS can be used to place N queens on an N×N chessboard such that no two queens attack each other.

    - Tree and Graph Traversal:
        * Decision Trees: DFS can be used to traverse decision trees in applications like game playing and automated planning.
        
        * Topological Sorting: In directed acyclic graphs, DFS is used to * 
        
        * perform topological sorting, which is important in scheduling tasks and resolving dependencies.