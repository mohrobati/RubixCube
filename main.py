from astar import AStarAlgorithm
from bidirectional import BidirectionalSearch
from ids import IterativeDeepeningSearch

# cube data structure
cube = [[0 for i in range(4)] for j in range(6)]
goal = [[1, 1, 1, 1], [5, 5, 5, 5], [3, 3, 3, 3], [4, 4, 4, 4], [2, 2, 2, 2], [6, 6, 6, 6]]

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

# one in depth
# 1 1 1 1
# 2 2 3 3
# 4 4 2 2
# 5 5 4 4
# 6 6 6 6
# 5 5 3 3

# 1 1 1 1
# 2 2 3 3
# 4 4 5 5
# 3 3 2 2
# 6 6 6 6
# 4 4 5 5

# two in depth
# 1 4 1 5
# 2 2 3 3
# 4 6 5 6
# 2 3 2 3
# 6 4 6 5
# 4 1 5 1

# 1 2 3 3
# 3 4 3 5
# 2 2 4 4
# 1 6 2 6
# 6 6 4 5
# 5 1 5 1

# three in depth
# 6 1 2 2
# 1 5 4 6
# 6 6 4 2
# 4 5 3 5
# 1 4 3 2
# 1 3 5 3

# four in depth
# 1 3 1 2
# 3 3 6 5
# 4 5 6 2
# 6 5 4 3
# 1 6 4 2
# 1 4 5 2

# six in depth
# goal = [[1, 1, 1, 1], [5, 5, 5, 5], [3, 3, 3, 3], [4, 4, 4, 4], [2, 2, 2, 2], [6, 6, 6, 6]]
# 4 4 6 2
# 3 5 3 6
# 1 3 4 2
# 5 3 6 4
# 1 5 5 2
# 1 6 1 2
