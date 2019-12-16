from cube_data_structure import buildNextStates


class BidirectionalSearch:

    def __init__(self, cube, goal):
        self.cube = cube
        self.goal = goal

    def checkIfReached(self, srcFrontier, goalFrontier):
        for srcState in srcFrontier:
            for goalState in goalFrontier:
                if srcState == goalState:
                    return True, srcState
        return False, None

    def bidirectionalSearchAlgorithm(self, cube, goal):
        srcFrontier = [cube]
        goalFrontier = [goal]
        queue = []
        while True:
            checkResult = self.checkIfReached(srcFrontier, goalFrontier)
            if checkResult[0]:
                intersectionNode = checkResult[1]
                break
            for state in srcFrontier:
                for child in buildNextStates(state):
                    queue.append(child)
            while len(queue) != 0:
                srcFrontier.append(queue.pop(0))
            for state in goalFrontier:
                for child in buildNextStates(state):
                    queue.append(child)
            while len(queue) != 0:
                goalFrontier.append(queue.pop(0))
        return True, intersectionNode

    def run(self):
        print(self.bidirectionalSearchAlgorithm(self.cube, self.goal))
