from astar import AStarAlgorithm
from bidirectional import BidirectionalSearch
from ids import IterativeDeepeningSearch

# cube data structure
cube = [[0 for i in range(4)] for j in range(6)]
goal = [[2, 2, 2, 2], [6, 6, 6, 6], [5, 5, 5, 5], [3, 3, 3, 3], [4, 4, 4, 4], [1, 1, 1, 1]]

# enriching cube data structures via inputs
for i in range(6):
    line = input()
    colors = line.split()
    for j in range(len(colors)):
        try:
            cube[i][j] = int(colors[j])
        except:
            print('Wrong input!')
            exit(0)

print('Choose algorithm:')
print('1. IDS')
print('2. Bidirectional Search')
print('3. A Star')
print('>>', end=" ")
algorithmType = int(input())

if algorithmType == 1:
    print("Enter Initial Limit:")
    firstLimit = int(input())
    IterativeDeepeningSearch(cube, firstLimit).run()
elif algorithmType == 2:
    BidirectionalSearch(cube, goal).run()
elif algorithmType == 3:
    AStarAlgorithm(cube).run()

