# Shortest Path Comparison

## What it is

It runs a shortest path algorithm on a file and shows you the result with number of nodes opened and closed in addition to the cost.

This was made to see the differences between the algorithms A*, BFS and Djikstra.

## How to run it

It uses python static typing released in python3.6 so you need that to run this program.

If you don't have it on linux install it with 

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.6

And to run the script simply run

    python3.6 code.py

### Flags

| Flag | Example | Usage |
|------|---------|-------|
| -v | python3.6 code.py -v | Visualizes all nodes that are open and closed in addition to the best route. |
| -u | python3.6 code.py -u  | Uses a better prediction of cost to goal, but might overestimate and return a suboptimal result (only for A*). |
| -f path | python3.6 code.py -f boards/board-2-4.txt | Spesifies the input file. |
| -a algorithm | python3.6 code.py -a Djikstra | Spesifies the algorithm to run. |

## The difference between the algorithms

There is only one this that is different between the algorithms - the sort function in best_first_search. 

So BFS checks all the nodes in order for when they get discovered. The list of nodes not checked (the open nodes) is never sorted. 
The Djikstra orders them on the cost to get to that node so it is sorted on that, here it's called g. 
A* orders them on the cost to get to that node and estimated cost to the goal, g+h.

So in this code we run different algorithms by defining the lambda function for the sort.

## h - The estimated cost

This is the cool function that can make or break the A* algorithm. In theory it should never be over the minimum cost of going to the goal. The reason for this is if it estimates too high it might then prioritize unoptimal paths because it assumes there are noe better options. In some cases it is most important to get the right answer, but in other cases speed are more important and an unoptimal solution is more feasible.

In this case I defined two versions of h, one that is the minimum best path where it assumes everything costs 1 and one uncertain that estimates based on previous cost.
This might fail if the previous cost is very high and the rest is low, but on the test-cases it has delivered very good results with big improvements on number of nodes closed nodes.
