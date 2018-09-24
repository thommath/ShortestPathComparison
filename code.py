import argparse
from typing import Dict, List, Tuple, NewType

class Node:
    """Minimal Node class"""

    def __init__(self, pos: Tuple[int, int], grid):
        """Save grid and pos and define default values"""
        self.grid = grid
        self.pos: Tuple[int, int] = pos
        self.parent = None
        self.kids = []
        self.f: int = 0 # f equals g + h
        self.g: int = 0 # g is the cost to get to this node
        self.h: int = 0 # h is the estimated cost to get to the goal
 
    @property
    def val(self) -> str:
        """Return the string value of the node for wall and value cheching"""
        return self.grid[self.pos[0]][self.pos[1]]

    def succ(self) -> List:
        """Find all adjacent cols"""
        # defining neighbour fields
        x = [0, 1, 0, -1]
        y = [1, 0, -1, 0]

        # Loop over neighbour fields
        arr = []
        for i in range(0, len(x)):
            # Check if the neighbour is outside the grid
            if self.pos[0] + x[i] < len(self.grid) and self.pos[0] + x[i] >= 0 and \
                self.pos[1] + y[i] < len(self.grid[self.pos[0] + x[i]]) and self.pos[1] + y[i] >= 0:
                node = Node((self.pos[0] + x[i], self.pos[1] + y[i]), self.grid)
                # Check that the node is not a wall
                if node.val != '#':
                    arr.append(node)
        return arr

    def __eq__(self, other) -> bool:
        """Nodes are equal when in the same position"""
        return self.pos[0] == other.pos[0] and self.pos[1] == other.pos[1]

    def __sub__(self, other) -> int:
        """Redefining subtraction to how far it is between them"""
        return abs(self.pos[0] - other.pos[0]) + abs(self.pos[1] - other.pos[1])

    def __str__(self) -> str:
        return str(self.pos)

    def get_parents(self) -> List:
        """Get the list of all parents from top to bottom"""
        if self.parent is not None:
            return self.parent.get_parents() + [self]
        else:
            return [self]


    def print_tree(self) -> str:
        """Return a string of all parents from top to bottom"""
        if self.parent is not None:
            return self.parent.print_tree() + ' - ' + str(self)
        else:
            return str(self)

class A:
    """A* Class to be able to run multiple shortest path algoritms at once"""

    def __init__(self, grid: List[List[str]], uncertain: bool = False):
        self.grid: List[List[str]] = grid
        self.h = None
    
    @property
    def goal(self) -> Node:
        """Define a goal node"""
        return self.find_char('B')

    @property
    def start(self) -> Node:
        """Define a start node"""
        return self.find_char('A')

    def find_char(self, c: str) -> Node:
        """Helper function to find start and goal"""
        for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid[x])):
                if self.grid[x][y] == c:
                    return Node((x, y), self.grid)


    def best_first_search(self, order=lambda x: x.f) -> Tuple[Node, bool, List[Node], List[Node]]:
        """Shortest path function"""
        # Keep track of open and closed nodes
        self.OPEN: List[Node] = []
        self.CLOSED: List[Node] = []

        # Initialize start node
        n0 = self.start
        n0.f = 0 + self.h(n0)
        self.OPEN.append(n0)

        while 1:
            # Return None if there is no path to goal
            if self.OPEN == []:
                return (None, False, None, None)
            
            # Get next node
            x = self.OPEN.pop(0)
            self.CLOSED.append(x)

            # If next is goal return true
            if x.val == 'B':
                return (x, True, self.CLOSED, self.OPEN)
            
            # Loop over all adjacent nodes to the next node
            for s in x.succ():
                # If it's a new node include it in node tree, add to open and resort open
                if not s in self.OPEN + self.CLOSED:
                    self.attach_and_eval(s, x)
                    self.OPEN.append(s)
                    self.OPEN = sorted(self.OPEN, key=order)

                # Else check if this path is faster to the node and update that node and all children
                elif x.g + A.arc_cost(x, s) < s.g:
                    self.attach_and_eval(s, x)
                    if s in self.CLOSED:
                        self.propagate_path_improvements(s)

    def h(self, n:Node) -> int:
        """Best case estimate of shortest possible path to goal"""
        # We can make the search faster by making a prediction that is not minimum but might not get the optimal route
        if self.h:
            return h(n)
        # Each node to goal has a value of 1
        return (n - self.goal)*1

    def arc_cost(c: Node, p: Node) -> int:
        """Defining the cost of going to the next node"""
        # Ignores cost of current node and only use cost of using the next node
        if p.val == 'w':
            return 100
        elif p.val == 'm':
            return 50
        elif p.val == 'f':
            return 10
        elif p.val == 'g':
            return 5
        return 1

    def attach_and_eval(self, c:Node, p:Node) -> None:
        """Setting p as parent for c and reevaluates c values"""
        # Set parent/child relation
        c.parent = p
        p.kids.append(c)
        # Update values
        c.g = p.g + A.arc_cost(p, c)
        c.f = c.g + self.h(c)

    def propagate_path_improvements(self, p: Node) -> None:
        """Updates values for all the kids for the parent""" 
        for c in p.kids:
            # If the new cost is less than the child value update values
            if p.g + arc_cost(p,c) < c.g:
                # Update values
                c.g = p.g + A.arc_cost(p,c)
                c.f = c.g + self.h(c)
                self.propagate_path_improvements(c)


    def visualize_results(self, res = None, include_lists = False) -> None:
        """Print the grid to screen"""

        grid = [x[:] for x in self.grid]

        # include what nodes are visited
        if include_lists:
            for n in self.OPEN:
                grid[n.pos[0]][n.pos[1]] = '*'

            for n in self.CLOSED:
                grid[n.pos[0]][n.pos[1]] = 'x'

        if res:
            for n in res[0].get_parents():
                grid[n.pos[0]][n.pos[1]] = 'O'

        for l in grid:
            s = ''
            for i in l:
                s+=i
            print(s)
        if res:
            print('score: ', res[0].g, ' closed: ', len(self.CLOSED), 'open: ', len(self.OPEN))
        print()


def main(file: str, verbose: bool, algorithm: str, uncertain: bool) -> None:
    """Main run function"""
    # Read the map from file
    grid: List[List[str]] = []
    with open(file, 'r') as f: 
        for l in f:
            grid.append(list(l.rstrip()))

    # Make an environement for the algorithm
    a = A(grid, uncertain)

    # Print the map
    if verbose:
        a.visualize_results()

    if algorithm in ['A*', 'a*', 'a', 'A']:
        alg = lambda x: x.f
    elif algorithm in ['Djikstra', 'djikstra', 'dikstra', 'd']:
        alg = lambda x: x.g
    elif algorithm in ['bfs', 'BFS']:
        alg = lambda x: 0
    else:
        print('ERROR: invalid algorithm')
        return

    # Run the algorithm
    res = a.best_first_search(alg)

    # Print the result on the map if it succeded
    # Else just print the result
    if res[1]:
        a.visualize_results(res, verbose)
    else:
        print(res)


if __name__ == "__main__":
    # Define arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default='boards/board-1-1.txt', help="Path to input file")
    parser.add_argument("-v", "--verbose", action='store_const', const=True, default=False, help="Include open and closed nodes in output")
    parser.add_argument("-a", "--algorithm", default='A*', help="Choose an algorith: A*, Djikstra, BFS")
    parser.add_argument("-u", "--uncertain", action='store_const', const=True, default=False, help="Pay accuracy for speed")

    # Parse arguments
    args = parser.parse_args()

    # Run the program
    main(args.file, args.verbose, args.algorithm, args.uncertain)


