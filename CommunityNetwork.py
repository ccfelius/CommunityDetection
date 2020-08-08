class Node:

    def __init__(self, name='Nameless', connections = set([])):
            """ Create a new node """
            self.name = name
            self.Ex = 0
            self.Ix = 0
            self.Dx = 0
            # self.connections = connections

    def print(self):
        print(self.name, self.Ex, self.Ix, self.Dx)


class Edge:

    def __init__(self, start, end, length, type):
            """ Create a new edge """
            self.start = start
            self.end = end
            self.type = type
            self.length = length


    def print(self):
        print([(self.start.name, self.end.name), self.length])




class Graph:

    def __init__(self, nodes=[], edges=[]):
        """ Create a new undirected graph """
        self.nodes = nodes
        self.edges = edges

    def CreateNode(self, name = 'Nameless', connections = set([])):
        node = Node(name, connections)
        self.nodes.append(node)

    def AddEdge(self, start, end, length=1, type='undirected'):

        flag = 0
        while flag == 0:
            for i in self.nodes:
                if start == i.name:
                    start = i
                    flag = 1

        if flag == 0:
            start = self.CreateNode(start)

        flag = 0
        while flag == 0:
            for i in self.nodes:
                if end == i.name:
                    end = i
                    flag = 1

        if flag == 0:
            start = self.CreateNode(end)

        edge = Edge(start, end, length, type)
        self.edges.append(edge)


