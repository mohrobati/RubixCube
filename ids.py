from graph import Graph
import copy


class IterativeDeepeningSearch:

    def __init__(self, cube, positions, firstLimit):
        self.cube = cube
        self.positions = positions
        self.firstLimit = firstLimit
        self.graph = Graph()

    def buildNextStates(self, state):
        nextStates = []
        for position in self.positions:
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
                tmp[neighbour][0] = tmp2[neighbour][1]
                tmp[neighbour][1] = tmp2[neighbour][3]
                tmp[neighbour][2] = tmp2[neighbour][0]
                tmp[neighbour][3] = tmp2[neighbour][2]
                # neighbour rotate started
                nextStates.append(tmp)
        return nextStates

    def dlsAlgorithm(self, state, limit):
        if self.checkCompletedCube(state):
            return True
        if limit <= 0: return False
        for nextState in self.buildNextStates(state):
            if self.dlsAlgorithm(nextState, limit - 1):
                return True
        return False

    def idsAlgorithm(self, state, limit):
        for i in range(limit, 20):
            if self.dlsAlgorithm(state, limit):
                return True
        return False

    def checkCompletedCube(self, state):
        for side in state:
            if side[1:] != side[:-1]:
                return False
        return True

    def run(self):
        print(self.idsAlgorithm(self.cube, self.firstLimit))
