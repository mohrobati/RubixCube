from cube_data_structure import buildNextStates
from copy import deepcopy

class BidirectionalSearch:

    def __init__(self, cube, goal):
        self.cube = cube
        self.goal = goal

    def checkForIntersection(self, frontier, objectNode):
        for state in frontier:
            if state['state'] == objectNode['state']:
                self.printPath(state, objectNode)
                return True
        return False

    def bidirectionalSearchAlgorithm(self, cube, goal):
        if cube == goal:
            return True
        srcFrontier = [{'state': cube, 'parent': None}]
        goalFrontier = [{'state': goal, 'parent': None}]
        queue = []
        while True:
            for state in srcFrontier:
                for child in buildNextStates(state['state']):
                   queue.append({'state': child, 'parent': state})
                srcFrontier.remove(state)
            while queue:
                srcFrontier.append(queue.pop())
            for state in goalFrontier:
                if self.checkForIntersection(srcFrontier, state):
                    return True
                for child in buildNextStates(state['state']):
                    queue.append({'state': child, 'parent': state})
                goalFrontier.remove(state)
            while queue:
                goalFrontier.append(queue.pop())

    def printPath(self, intersectionFromSource, intersectionFromGoal):
        pathToSource = []
        pathToGoal = []
        while intersectionFromSource['parent'] is not None:
            pathToSource.append(intersectionFromSource['state'])
            intersectionFromSource = intersectionFromSource['parent']
        pathToSource.append(intersectionFromSource['state'])
        while intersectionFromGoal['parent'] is not None:
            pathToGoal.append(intersectionFromGoal['state'])
            intersectionFromGoal = intersectionFromGoal['parent']
        pathToGoal.append(intersectionFromGoal['state'])
        pathToSource.reverse()
        pathToSource.pop(len(pathToSource)-1)
        path = pathToSource + pathToGoal
        print('Path: ')
        for state in path:
            print(state)

    def run(self):
        self.bidirectionalSearchAlgorithm(self.cube, self.goal)
