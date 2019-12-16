from cube_data_structure import checkCompletedCube, buildNextStates, printPath
import math


class AStarAlgorithm:

    def __init__(self, cube):
        self.cube = cube
        self.goal = None
        self.exploredSet = []

    def getMinFromFrontier(self, frontier):
        min = math.inf
        bestNode = None
        for node in frontier:
            if node not in self.exploredSet:
                if self.getHeuristic(node['state']) + node['depth'] < min:
                    min = self.getHeuristic(node['state']) + node['depth']
                    bestNode = node
        return bestNode

    def aStarAlgorithm(self, cube):
        frontier = [{'state': cube, 'depth': 0, 'parent': None}]
        while True:
            currNode = self.getMinFromFrontier(frontier)
            print(currNode)
            if checkCompletedCube(currNode['state']):
                self.goal = currNode
                break
            self.exploredSet.append(currNode['state'])
            for child in buildNextStates(currNode['state']):
                frontier.append({'state': child, 'depth': currNode['depth']+1, 'parent': currNode})
            frontier.remove(currNode)

    def getHeuristic(self, state):
        heuristic = 0
        for side in state:
            differentColors = len(set(side))
            if differentColors == 4:
                heuristic += 4
            elif differentColors == 3:
                heuristic += 2
            elif differentColors == 2:
                heuristic += 1
        return heuristic

    def run(self):
        self.aStarAlgorithm(self.cube)
        print('Path: ')
        printPath(self.goal)
