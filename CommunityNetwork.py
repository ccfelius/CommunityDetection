class Node:

    def __init__(self, name='Nameless', connections = set([])):

            """
            Create a new node object
             """

            self.name = name
            self.Ex = 0
            self.Ix = 0
            self.Dx = 0
            # self.connections = connections

    def print(self):

        """
        Print node
         """

        print(self.name, self.Ex, self.Ix, self.Dx)


class Edge:

    def __init__(self, start, end, length, type):

            """
            Create edge object
             """

            self.start = start
            self.end = end
            self.type = type
            self.length = length

    def print(self):

        """
        Print edge
         """

        print([(self.start.name, self.end.name), self.length])




class Graph:

    """
    Create graph object
     """

    def __init__(self, nodes=[], edges=[]):
        """ Create a new undirected graph """
        self.nodes = nodes
        self.edges = edges

    def CreateNode(self, name = 'Nameless'):

        """
        Create node object and add to graph
         """

        node = Node(name)
        self.nodes.append(node)

    def reset(self):

        """
        Reset Ex, Ix, Dx from every node in graph to 0
         """

        for node in self.nodes:
            node.Ex = 0
            node.Ix = 0
            node.Dx = 0

    def AddEdge(self, start, end, length=1, type='undirected'):

        """
        Add new egdes to graph
         """

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

    def AddNodes(self, amount=2):

        """
        Add new nodes to graph
         """

        for i in range(amount):
            self.CreateNode(i)

    def print(self):

        """
        Print nodes and edges from graph
         """

        print("\nNodes:")
        for i in self.nodes:
            print(i.name)
        print("\nEdges:")
        for i in self.edges:
            print([(i.start.name, i.end.name), i.length])
        print("")


