from cube_data_structure import checkCompletedCube, buildNextStates


class IterativeDeepeningSearch:

    def __init__(self, cube, firstLimit):
        self.cube = cube
        self.firstLimit = firstLimit
        self.producedNodes = 1
        self.expandedNodes = 0
        self.answerDepth = 0
        self.algorithmFinished = False

    def dlsAlgorithm(self, state, limit, maxLimit):
        if not self.algorithmFinished:
            if checkCompletedCube(state):
                self.answerDepth = maxLimit - limit
                return True
            if limit <= 0:
                return False
            self.producedNodes += 12
            self.expandedNodes += 1
            for nextState in buildNextStates(state):
                if self.dlsAlgorithm(nextState, limit - 1, maxLimit):
                    self.algorithmFinished = True
                    return True
            return False

    def idsAlgorithm(self, state, limit):
        for maxLimit in range(limit, 20):
            if self.dlsAlgorithm(state, maxLimit, maxLimit):
                return True
        return False

    def run(self):
        print('Found: ', self.idsAlgorithm(self.cube, self.firstLimit))
        print('Produced Nodes: ', self.producedNodes)
        print('Expanded Nodes: ', self.expandedNodes)
        print('Answer Depth: ', self.answerDepth)
        print('Maximum Nodes In Memory: ', 12*self.answerDepth+1)
