from astar import AStarAlgorithm
from bidirectional import BidirectionalSearch
from ids import IterativeDeepeningSearch

# cube data structure
cube = [[0 for i in range(4)] for j in range(6)]

# you can rotate cube from 4 positions
# each one can rotate 3 times so you can reach 12
# different states from each state
positions = [[{'side': 0, 'indices': [0, 1], 'neighbourRotation': 5},
              {'side': 1, 'indices': [0, 2], 'neighbourRotation': 5},
              {'side': 4, 'indices': [2, 3], 'neighbourRotation': 5},
              {'side': 3, 'indices': [1, 3], 'neighbourRotation': 5}],
             [{'side': 0, 'indices': [2, 3], 'neighbourRotation': 2},
              {'side': 1, 'indices': [1, 3], 'neighbourRotation': 2},
              {'side': 4, 'indices': [0, 1], 'neighbourRotation': 2},
              {'side': 3, 'indices': [0, 2], 'neighbourRotation': 2}],
             [{'side': 1, 'indices': [0, 1], 'neighbourRotation': 0},
              {'side': 2, 'indices': [0, 1], 'neighbourRotation': 0},
              {'side': 3, 'indices': [0, 1], 'neighbourRotation': 0},
              {'side': 5, 'indices': [2, 3], 'neighbourRotation': 0}],
             [{'side': 1, 'indices': [2, 3], 'neighbourRotation': 4},
              {'side': 2, 'indices': [2, 3], 'neighbourRotation': 4},
              {'side': 3, 'indices': [2, 3], 'neighbourRotation': 4},
              {'side': 5, 'indices': [0, 1], 'neighbourRotation': 4}]]

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
    IterativeDeepeningSearch(cube, positions, firstLimit).run()
elif algorithmType == 2:
    BidirectionalSearch(cube, positions).run()
elif algorithmType == 3:
    AStarAlgorithm(cube, positions).run()


# 1 1 1 1
# 2 2 3 3
# 4 4 2 2
# 5 5 4 4
# 6 6 6 6
# 5 5 3 3