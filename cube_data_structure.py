import copy

# you can rotate cube from 4 positions
# each one can rotate 3 times so you can reach 12
# different states from each state
positions = [[{'side': 0, 'indices': [0, 1], 'neighbourRotation': 5},
              {'side': 1, 'indices': [2, 0], 'neighbourRotation': 5},
              {'side': 4, 'indices': [3, 2], 'neighbourRotation': 5},
              {'side': 3, 'indices': [1, 3], 'neighbourRotation': 5}],
             [{'side': 0, 'indices': [2, 3], 'neighbourRotation': 2},
              {'side': 3, 'indices': [0, 2], 'neighbourRotation': 2},
              {'side': 4, 'indices': [1, 0], 'neighbourRotation': 2},
              {'side': 1, 'indices': [3, 1], 'neighbourRotation': 2}],
             [{'side': 2, 'indices': [0, 1], 'neighbourRotation': 0},
              {'side': 1, 'indices': [0, 1], 'neighbourRotation': 0},
              {'side': 5, 'indices': [3, 2], 'neighbourRotation': 0},
              {'side': 3, 'indices': [0, 1], 'neighbourRotation': 0}],
             [{'side': 2, 'indices': [2, 3], 'neighbourRotation': 4},
              {'side': 3, 'indices': [2, 3], 'neighbourRotation': 4},
              {'side': 5, 'indices': [1, 0], 'neighbourRotation': 4},
              {'side': 1, 'indices': [2, 3], 'neighbourRotation': 4}],
             [{'side': 0, 'indices': [1, 3], 'neighbourRotation': 3},
              {'side': 5, 'indices': [1, 3], 'neighbourRotation': 3},
              {'side': 4, 'indices': [1, 3], 'neighbourRotation': 3},
              {'side': 2, 'indices': [1, 3], 'neighbourRotation': 3}],
             [{'side': 2, 'indices': [0, 2], 'neighbourRotation': 1},
              {'side': 4, 'indices': [0, 2], 'neighbourRotation': 1},
              {'side': 5, 'indices': [0, 2], 'neighbourRotation': 1},
              {'side': 0, 'indices': [0, 2], 'neighbourRotation': 1}]
             ]


def buildNextStates(state):
    nextStates = []
    for position in positions:
        tmp = copy.deepcopy(state)
        for j in range(3):
            tmp2 = copy.deepcopy(tmp)
            # one single rotate started
            for i in range(3):
                tmp[position[i + 1]['side']][position[i + 1]['indices'][0]] = \
                    tmp2[position[i]['side']][position[i]['indices'][0]]
                tmp[position[i + 1]['side']][position[i + 1]['indices'][1]] = \
                    tmp2[position[i]['side']][position[i]['indices'][1]]
            tmp[position[0]['side']][position[0]['indices'][0]] = \
                tmp2[position[3]['side']][position[3]['indices'][0]]
            tmp[position[0]['side']][position[0]['indices'][1]] = \
                tmp2[position[3]['side']][position[3]['indices'][1]]
            # one single rotate ended
            # neighbour rotate ended
            neighbour = position[0]['neighbourRotation']
            tmp[neighbour][0] = tmp2[neighbour][2]
            tmp[neighbour][1] = tmp2[neighbour][0]
            tmp[neighbour][2] = tmp2[neighbour][3] #1
            tmp[neighbour][3] = tmp2[neighbour][1] #3
            # neighbour rotate started
            nextStates.append(copy.deepcopy(tmp))
    return nextStates


def checkCompletedCube(state):
    for side in state:
        if side[1:] != side[:-1]:
            return False
    return True


def printPath(goal):
    stack = []
    while goal['parent'] is not None:
        stack.append(goal['state'])
        goal = goal['parent']
    stack.append(goal['state'])
    while len(stack) != 0:
        print(stack.pop())
