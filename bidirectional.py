from cube_data_structure import buildNextStates, printPath


class BidirectionalSearch:

    def __init__(self, cube, goal):
        self.cube = cube
        self.producedNodes = 1
        self.maxMemory = 1
        self.currentlyInMemory = 1
        self.expandedNodes = 0
        self.answerDepth = 0
        self.goal = goal

    def checkForIntersection(self, frontier, objectNode):
        for state in frontier:
            if state['state'] == objectNode['state']:
                print('Produced Nodes: ', self.producedNodes)
                print('Expanded Nodes: ', self.expandedNodes)
                print('Maximum Nodes In Memory: ', self.maxMemory)
                self.printPath(state, objectNode)
                return True
        return False

    def bidirectionalSearchAlgorithm(self, cube, goal):
        if cube == goal:
            return True
        srcFrontier = [{'state': cube, 'parent': None}]
        srcExploredSet = []
        goalFrontier = [{'state': goal, 'parent': None}]
        goalExploredSet = []
        queue = []
        while True:
            for state in srcFrontier:
                self.producedNodes += 6
                self.currentlyInMemory += 6
                self.maxMemory = max(self.currentlyInMemory, self.maxMemory)
                self.expandedNodes += 1
                for child in buildNextStates(state['state']):
                    if child in srcExploredSet:
                        self.currentlyInMemory -= 1
                        continue
                    queue.append({'state': child, 'parent': state})
                srcExploredSet.append(state['state'])
            while queue:
                srcFrontier.append(queue.pop())
            for state in goalFrontier:
                self.producedNodes += 6
                self.currentlyInMemory += 6
                self.maxMemory = max(self.currentlyInMemory, self.maxMemory)
                self.expandedNodes += 1
                if self.checkForIntersection(srcFrontier, state):
                    return True
                for child in buildNextStates(state['state']):
                    if child in goalExploredSet:
                        self.currentlyInMemory -= 1
                        continue
                    queue.append({'state': child, 'parent': state})
                goalExploredSet.append(state['state'])
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
        print('Answer Depth: ', len(path)-1)
        print('Path: ')
        for state in path:
            print(state)

    def run(self):
        self.bidirectionalSearchAlgorithm(self.cube, self.goal)
