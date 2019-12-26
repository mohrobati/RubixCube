from cube_data_structure import checkCompletedCube, buildNextStates, printPath
import math


class AStarAlgorithm:

    def __init__(self, cube):
        self.cube = cube
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
            for child in buildNextStates(currNode['state']):
                jump = False
                for node in frontier:
                    if node['state'] == child:
                        if self.getHeuristic(node['state']) + node['depth'] < self.getHeuristic(child) + node['depth'] + 1:
                            jump = True
                if not jump:
                    if child in exploredSet:
                        if self.getHeuristic(currNode['state']) + currNode['depth'] < self.getHeuristic(child) + currNode['depth'] + 1:
                            continue
                    else:
                        frontier.append({'state': child, 'depth': currNode['depth'] + 1, 'parent': currNode})

    def run(self):
        self.aStarAlgorithm(self.cube)
        print('Path: ')
        printPath(self.goal)
