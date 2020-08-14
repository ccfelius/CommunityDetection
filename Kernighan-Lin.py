from CommunityNetwork import Graph

def CreateGraph():
    return Graph()


# Example Graph
x = CreateGraph()
x.AddNodes(8)
edges_ = [[0,1,8], [4,2,3], [0,6,7], [0,2,9], [0,4,2], [2,7,9], [6,5,8], [5,7,5], [7,3,8], [3,5,8]]
# Add edges
for e in edges_:
    x.AddEdge(e[0],e[1],e[2])

x.print()

# Clusters for example
cluster1 = [3,5,2,0]
cluster2 = [6,7,4,1]

def KernighanLin(graph, initial):

    print("Clusters: " + str([initial[0], initial[1]]))

    # Method to calculate total costs
    def total_costs(graph, initial):
        cost = 0
        for edge in graph.edges:
            if edge.start.name in initial[0] and edge.end.name in initial[0]:
                continue
            elif edge.start.name in initial[1] and edge.end.name in initial[1]:
                continue
            else:
                cost += edge.length

        print("Costs: " + str(cost))
        print("---------------------------------------------")
        print()
        return cost

    # Method to calculate the best pair to swap
    def best_edge(graph, clusters, print_=True):

        swappairs = []
        graph.reset()

        for edge in graph.edges:
            if edge.start.name in initial[0] and edge.end.name in initial[0]:
                edge.start.Ix += edge.length
                edge.end.Ix += edge.length
            elif edge.start.name in initial[1] and edge.end.name in initial[1]:
                edge.start.Ix += edge.length
                edge.end.Ix += edge.length
            else:
                edge.start.Ex += edge.length
                edge.end.Ex += edge.length

        for node in graph.nodes:
            node.Dx = node.Ex - node.Ix

        # Check whether improvement is possible
        temp = len(graph.nodes)
        count = 0
        for node in graph.nodes:
            if node.Dx <= 0:
                count += 1

        if count == temp:
            print()
            print("--------- FINALIZED ---------")
            print("Clusters cannot be improved")
            return False

        if print_ == True:
            print("N Ex Ix Dx")
            for node in graph.nodes:
                node.print()

        for n in clusters[0]:
            for n_ in clusters[1]:
                swappair = (n, n_)
                counter = 0
                x = None
                y = None
                while counter < 2:
                    for i in graph.nodes:
                        if i.name == n:
                            x = i
                            counter += 1
                        elif i.name == n_:
                            y = i
                            counter += 1

                length = 0
                for j in graph.edges:
                    if x == j.start and y == j.end:
                        length = j.length
                    elif y == j.start and x == j.end:
                        length = j.length

                b_edge = x.Dx + y.Dx - 2*length
                swappairs.append([swappair, b_edge])

        if print_ == True:
            print()
            print("Possible Improvement")
            for i in swappairs:
                print(i)

        max = [(0,0),0]
        for i in swappairs:
            if i[1] > max[1]:
                max = i

        # Return for method best_edge
        return max

    # Pair swapping among clusters
    def swap(clusters, pair):

        if pair[0] in clusters[0]:
            clusters[0].remove(pair[0])
            clusters[0].append(pair[1])
            clusters[1].remove(pair[1])
            clusters[1].append(pair[0])
        else:
            clusters[0].remove(pair[1])
            clusters[0].append(pair[0])
            clusters[1].remove(pair[0])
            clusters[1].append(pair[1])

        return [clusters[0], clusters[1]]



    in_costs = total_costs(graph, initial)
    if best_edge(graph, initial) == False:
        print("Final costs: " + str(in_costs))
        print("Final clusters " + str(initial))
        return

    swap_ = best_edge(graph, initial, print_=False)[0]
    print()
    print("Pair to swap:")
    print(swap_)
    print()
    new_clusters = swap(initial, swap_)

    KernighanLin(graph, new_clusters)

print("\n---------- KERNIGHAN-LIN ALGORITHM ----------")

# Run Kernighan-Lin algorithm
KernighanLin(x, [cluster1, cluster2])
