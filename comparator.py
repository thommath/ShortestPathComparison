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
    for n in range(x):
        line: List[str] = [] 
        for m in range(y):
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

    a = (0, 0)
    b = (0, 0)
    while a == b:
        a = (math.floor(x*random.random()), math.floor(y*random.random()))
        b = (math.floor(x*random.random()), math.floor(y*random.random()))

    graph[a[0]][a[1]] = 'A'
    graph[b[0]][b[1]] = 'B'

    return graph


def run_algorithms(grid, penelty_for_suboptimal_solution:int = 200):
    a = A(grid)

    # Run algorithms

    a.h = lambda n: (n - a.goal)
    res_a = a.best_first_search(lambda x: x.f)

    a.h = lambda n: (n - a.goal) * (n.g / (n-a.start)) if n-a.start > 0 else n-a.goal
    res_a2 = a.best_first_search(lambda x: x.f)

    a.h = lambda n: (n - a.goal) * 1.001
    res_a3 = a.best_first_search(lambda x: x.f)

    res_d = a.best_first_search(lambda x: x.g)

    score: List[int] = []

    score.append((res_a[0]-res_d[0])*penelty_for_suboptimal_solution + len(res_a[2]))
    score.append((res_a2[0]-res_d[0])*penelty_for_suboptimal_solution + len(res_a2[2]))
    score.append((res_a3[0]-res_d[0])*penelty_for_suboptimal_solution + len(res_a3[2]))
    score.append(len(res_d[2]))
#    score_d = len(res_d[2])
#    score_b = (res_b[0]-res_d[0])*penelty_for_suboptimal_solution + len(res_b[2])
    
    return score


def write_file(grid: List[List[str]], file: str):
    # Write the map to file
    with open(file, 'w') as f:
        for l in grid:
            s = ''
            for i in l:
                s+=i
            f.write(s + '\n') 


def main(uncertain: bool, output: str) -> None:
    """Main run function"""

    score: List[int] = []
    victories: List[int] = []

    for i in range(100):
        print('Iteration ', i)

        grid: List[List[str]] = generate_graph()
        write_file(grid, 'boards/compare-' + str(i) + '.txt')

        res = run_algorithms(grid)

        if score == []:
            score = res
        else: 
            score = [score[i]+res[i] for i in range(len(res))]

        if victories == []:
            victories = [0 for i in range(len(res))]
        victories[res.index(min(res))] += 1

        # Print result
        print('A*\t', score[0], victories[0])
        print('A*g\t', score[1], victories[1])
        print('A*2\t', score[2], victories[2])
        print('Dji.\t', score[-1], victories[-1])
#        print('BFS\t', score[3], victories[3])
        print()


    # Write the map to file
#    if output != '':
#        with open(output, 'w') as f:
#            for l in grid:
#                s = ''
#                for i in l:
#                    s+=i
#                f.write(s + '\n') 

    # # Run algorithms
    # res_a = a.best_first_search(lambda x: x.f)
    # res_d = a.best_first_search(lambda x: x.g)
    # res_b = a.best_first_search(lambda x: 0)

    # # Print result
    # print('A*\t', res_a[0].g, '\tclosed nodes:\t', len(res_a[2]))
    # print('Dji.\t', res_d[0].g, '\tclosed nodes:\t', len(res_d[2]))
    # print('BFS\t', res_b[0].g, '\tclosed nodes:\t', len(res_b[2]))


if __name__ == "__main__":
    # Define arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default='', help="Path to output file")
    parser.add_argument("-u", "--uncertain", action='store_const', const=True, default=False, help="Pay accuracy for speed")

    # Parse arguments
    args = parser.parse_args()

    # Run the program
    main(args.uncertain, args.output)

