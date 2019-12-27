from cube_data_structure import checkCompletedCube, buildNextStates, printPath
import math


class AStarAlgorithm:

    def __init__(self, cube):
        self.cube = cube
        self.producedNodes = 1
        self.maxMemory = 1
        self.currentlyInMemory = 1
        self.expandedNodes = 0
        self.answerDepth = 0
        self.goal = None

    def getMinFromFrontier(self, frontier):
        min = math.inf
        bestNode = None
        for node in frontier:
            f = self.getHeuristic(node['state']) + node['depth']
            if f < min:
                min = f
                bestNode = node
        return bestNode

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

    def aStarAlgorithm(self, cube):
        frontier = [{'state': cube, 'depth': 0, 'parent': None}]
        exploredSet = []
        while frontier:
            currNode = self.getMinFromFrontier(frontier)
            exploredSet.append(currNode['state'])
            frontier.remove(currNode)
            if checkCompletedCube(currNode['state']):
                self.goal = currNode
                break
            self.producedNodes += 6
            self.currentlyInMemory += 6
            self.maxMemory = max(self.currentlyInMemory, self.maxMemory)
            self.expandedNodes += 1
            for child in buildNextStates(currNode['state']):
                if child in exploredSet:
                    if self.getHeuristic(currNode['state']) + currNode['depth'] < self.getHeuristic(child) + currNode['depth'] + 1:
                        continue
                else:
                    self.currentlyInMemory += 1
                    frontier.append({'state': child, 'depth': currNode['depth'] + 1, 'parent': currNode})

    def run(self):
        self.aStarAlgorithm(self.cube)
        print('Produced Nodes: ', self.producedNodes)
        print('Expanded Nodes: ', self.expandedNodes)
        print('Answer Depth: ', self.goal['depth'])
        print('Maximum Nodes In Memory: ', self.maxMemory)
        print('Path: ')
        printPath(self.goal)
