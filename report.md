# Using the A* Algorithm
## 1.1 See code.py 
## 1.2
    python3.6 code.py -f boards/board-1-1.txt
    ....................
    ....................
    .........######.....
    ........OOOO..#..O..
    ........O######..O..
    ........OOOOOOOOOO..
    ....................
    score:  16  closed:  41 open:  29

    python3.6 code.py -f boards/board-1-2.txt
    ....OOO#............
    ...OO#O#............
    ..OO#OO#............
    OOO#.O#....OOOOOOOOO
    ....#OO#..OO#.......
    .....#OO#OO#........
    ......#OOO#.........
    score:  33  closed:  62 open:  18

    python3.6 code.py -f boards/board-1-3.txt
    .........OOOOOOOOOOO
    .........O#........O
    .......##OO#.......O
    ......#OO#O#.......O
    ......#O#OO#.......O
    ......#OOO#........O
    .......###.........O
    score:  28  closed:  73 open:  4

    python3.6 code.py -f boards/board-1-4.txt
    OO#.......#......#..
    #O#.#####.#.####.#..
    OO#OOOOO#.#....#....
    O##O###O######.#####
    OO#OO#OO#....#...#..
    #O####O##.##.#.#.##.
    .OOOOOO....#...#....
    score:  26  closed:  35 open:  2

## 2.1 See code.py
## 2.2
    python3.6 code.py -f boards/board-2-1.txt
    mmmmmffffrrrrrrrrOrrrrrrrrrrrrrrfffmmmmm
    mmmffffffffrrrrrrOOOOOOOOOOOOOrfffffmmmm
    mmfffffffffffffffffffffffffffOffffffmmmm
    mmfffffffffffffwwwwwfffffffffOfffffffmmm
    mfffffffffffffwwwwwwwffffffffOffffffmmmm
    mmffffffffffffwwwwwwwffOOOOOOOrrrrrrmmmm
    mmmffffffffffffwwwwwfffOffffffffrffffmmm
    mmfffffffffffffffffffffOffffffffrfffffmm
    mmffffffffgggggggggggggOggggggggggffffmm
    mmmffffggggggggggOOOOOOOggggggggggggffmm
    score:  79  closed:  243 open:  40

    python3.6 code.py -f boards/board-2-2.txt
    ffffffffffgggrgggggggrggggfffffffrrfffff
    ffOffffffgggrrggggggrrggffffffffrrffffff
    ffOfffgggggrrggggggrrgggffffrrrrrfffffff
    ggOOOOgggggrggggrrrrgggffffrrfffffffffff
    gggggOOOOOOOrrrrrgggggffffrrffffffffffff
    ggggrrgggggOggggggggffffffrfffffffffffff
    gggrrggggggOOggggggffffOOOOOOfffffffffff
    ggrrgggffgggOOOOggffOOOOfrffOrrrrfffffff
    ggrggffffffffffOOOOOOffffrffOfffrrffffff
    ggrgfffffffffffffffffffffrffOffffrrfffff
    score:  72  closed:  213 open:  62

    python3.6 code.py -f boards/board-2-3.txt
    gggggggggwwwgggggmmmmmmmmmmOOOOOOOOmmmmm
    gggggggggwwwwggggmmmmmmmmmmmmmmmmmOmgggg
    ggggggggggwwwwggggmmmmmmmmmmmmmmggOggggg
    ffgggggggggwwwwggggmmmOOOOmmOOOOOOOrgggg
    ffggggggggggwwwwwwwwwwOwwOOOOggggggrrrrr
    ffffggggggggggwwwwwwwwOwwwwggggggggggggg
    ffffffOOOOOOOOOOOOOOOOOwwwwwwggggggmmmmm
    fOOOOOOffffgggggggggmmmmmmwwwwmmmmmmmmmm
    fffffffffffffffmmmmmmmmmmmmmwwwmmmmmmmmm
    ffffffffffmmmmmmmmmmmmmmmmmmwwwmmmmmmmmm
    score:  596  closed:  304 open:  32

    python3.6 code.py -f boards/board-2-4.txt
    wwwwwggggggggggggggggggggggOOOOOOOgrrrrr
    wwwwwwwggggggggggggggOOOOOOOwwwwwOOrgggg
    wwwwwwwwwwwgggOOOOOOOOwwwwwwwwwwwwOwgggg
    wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOwwwww
    wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOwwwww
    wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOOwwwww
    wwwwwwwwgggggOgggggwwwwwwwwwwwwwwOwwwwww
    wwwwggggggfffOffgggggggggwwwwwwwwOwwwwww
    wwggggfffffffOffffffggggggggggggOOgwwwww
    wgggfffrrrrrrOOOOOOOOOOOOOOOOOOOOggggggg
    score:  161  closed:  173 open:  72

## 3.1 See code.py
## 3.2
### Running the algorithms on board 1-4

    python3.6 code.py -f boards/board-1-4.txt -v -a "A*"
    OO#.......#......#..
    #O#*#####.#.####.#..
    OO#OOOOO#.#....#....
    O##O###O######.#####
    OO#OO#OO#xx*.#...#..
    #O####O##x##.#.#.##.
    xOOOOOOxxxx#...#....
    score:  26  closed:  35 open:  2


    python3.6 code.py -f boards/board-1-4.txt -v -a Djikstra
    OO#x*.....#......#..
    #O#x#####.#.####.#..
    OO#OOOOO#.#....#....
    O##O###O######.#####
    OO#OO#OO#xxxx#...#..
    #O####O##x##x#*#.##.
    xOOOOOOxxxx#xxx#....
    score:  26  closed:  43 open:  2


    python3.6 code.py -f boards/board-1-4.txt -v -a BFS    
    OO#x*.....#......#..
    #O#x#####.#.####.#..
    OO#OOOOO#.#....#....
    O##O###O######.#####
    OO#OO#OO#xxxx#...#..
    #O####O##x##x#*#.##.
    xOOOOOOxxxx#xxx#....
    score:  26  closed:  43 open:  2


### Running the algorithms on board 2-4

    python3.6 code.py -f boards/board-2-4.txt -v -a "A*"
    wwww*xxxxxxxxxxxxxxxxxxxxxxOOOOOOOxxxxxx
    wwwww*xxxxxxxxxxxxxxxOOOOOOO*****OOxxxxx
    wwwwww*xxxxxxxOOOOOOOOx*****wwwww*O*xxxx
    wwwwwww****xxxxxxxxxxx*wwwwwwwwww*O*****
    wwwwwwwwwww***********wwwwwwwwwww*O*wwww
    wwwwwwwwwwwwwwww***wwwwwwwwwwwww*OO*wwww
    wwwwwwwwgggggO**xxx******wwwwwww*O*wwwww
    wwwwggggg****Oxxxxxxxxxxx********O*wwwww
    wwggggf**xxxxOxxxxxxxxxxxxxxxxxxOOx*wwww
    wgggff*xxxxxxOOOOOOOOOOOOOOOOOOOOxxx*ggg
    score:  161  closed:  173 open:  72


    python3.6 code.py -f boards/board-2-4.txt -v -a Djikstra
    www*xxxxxxxxxxxxxxxxxxxxxxxOOOOOOOOxxxxx
    wwww*xxxxxxxxxxxxxxxxOOOOOOO*****xOxxxxx
    wwwww**xxxxxxxOOOOOOOOxxxx**wwwww*O*xxxx
    wwwwwww****xxxxxxxxxxx****wwwwwww*O*****
    wwwwwwwwwww***********wwwwwwwwwww*O*wwww
    wwwwwwwwwwwwwwww***wwwwwwwwwwwww*OO*wwww
    wwwwwww***gg*O**xxx******wwwwwww*O*wwwww
    wwwwgg*xxx**xOxxxxxxxxxxx********O*wwwww
    wwgggg*xxxxxxOxxxxxxxxxxxxxxxxxxOOx*****
    wgggf*xxxxxxxOOOOOOOOOOOOOOOOOOOOxxxxxxx
    score:  161  closed:  189 open:  78

    python3.6 code.py -f boards/board-2-4.txt -v -a BFS
    wwwwwgggggg*xxxxxx*ggggggggggggggggrrrrr
    wwwwwwwggg*xxxxxxxx*ggggggggwwwwwgrrgggg
    wwwwwwwww*xxxxOxxxxx*gwwwwwwwwwwwwrwgggg
    wwwwwwwwww*xxxOxxxx*wwwwwwwwwwwwwwrwwwww
    wwwwwwwwwww*xxOxxx*wwwwwwwwwwwwwwwrwwwww
    wwwwwwwwwwww*xOxx*wwwwwwwwwwwwwwwrrwwwww
    wwwwwwwwgggggOOx*ggwwwwwwwwwwwwwwrwwwwww
    wwwwggggggfff*x*gggggggggwwwwwwwwrwwwwww
    wwggggffffffff*fffffggggggggggggrrgwwwww
    wgggfffrrrrrrrrrrrrrrrrrrrrrrrrrrggggggg
    score:  306  closed:  46 open:  16

## 3.3
The biggest difference is the BFS because it has similar stats to Djikstra in the first, but are a lot worse on the last map.
They are based on the same prinsiple but BFS doesn't use the cost of terrain when analyzing the path. 
This results in fewer nodes opened and closed, but worse score. 

A* is superior in all aspects over djiksta and bfs because it has superior prioritizing. 
A* is the only algorithm using the information about the goals position.
Nodes closer to the goal have probably a shorter path to the goal and therefor has higher priority. 
It will go more straight to the goal than the other algorithms while maintaining a minimum score and will therefor have a lower amount of open and closed nodes.
The maintaining of minimum score is only if it assumes best case prediction, if it predicts a cost bigger than it really is it might not return the best possible score. 


The advantage/disadvantage over djikstra is based on how good the prediction is (the function h).
When it uses that each step has 1 it wins over djikstra by a bit on every attempt. 
When it uses that each step forward has avg of previous it wins by more on 2-4, but 1-4 is a bit worse (still better than Djikstra). 
The higher cost it predicts the faster and more risky it gets. 
If it assumes each field costs 100 it stright crosses the river and get's a score of 306. 
