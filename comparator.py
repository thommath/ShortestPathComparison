import argparse
from typing import List
import random
import math
from code import A


def generate_graph() -> List[List[str]]:
    x: int = round(random.random()*100)
    y: int = round(random.random()*100)
    options: str = "wmfgr"

    graph: List[List[str]] = []
    for n in range(y):
        line = [] 
        for m in range(x):
            rand = random.random()
            elem = None
            if rand < 0.3 and n > 0:
                elem = graph[n-1][m]
            elif rand < 0.6 and n > 0 and m > 0:
                elem = line[-1]

            # If not elem set, pick random elem
            if not elem:
                elem = options[math.floor(random.random()*len(options))]

            line.append(elem)
        graph.append(line)


    graph[math.floor(y*random.random())][math.floor(x*random.random())] = 'A'
    graph[math.floor(y*random.random())][math.floor(x*random.random())] = 'B'

    return graph


def main(uncertain: bool, output: str) -> None:
    """Main run function"""
    grid: List[List[str]] = generate_graph()

    # Make an environement for the algorithms
    a = A(grid, uncertain)

    # Write the map to file
    if output != '':
        with open(output, 'w') as f:
            for l in grid:
                s = ''
                for i in l:
                    s+=i
                f.write(s + '\n') 

    # Run algorithms
    res_a = a.best_first_search(lambda x: x.f)
    res_d = a.best_first_search(lambda x: x.g)
    res_b = a.best_first_search(lambda x: 0)

    # Print result
    print('A*\t', res_a[0].g, '\tclosed nodes:\t', len(res_a[2]))
    print('Dji.\t', res_d[0].g, '\tclosed nodes:\t', len(res_d[2]))
    print('BFS\t', res_b[0].g, '\tclosed nodes:\t', len(res_b[2]))


if __name__ == "__main__":
    # Define arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default='', help="Path to output file")
    parser.add_argument("-u", "--uncertain", action='store_const', const=True, default=False, help="Pay accuracy for speed")

    # Parse arguments
    args = parser.parse_args()

    # Run the program
    main(args.uncertain, args.output)

